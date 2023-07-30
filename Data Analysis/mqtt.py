from data_analysis import get_last_week_id, calculate_daily, calculate_weekly
import pyodbc
import datetime
import time
from Adafruit_IO import MQTTClient

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=path;' # Path to database
)
conn = pyodbc.connect(conn_str)

AIO_USERNAME=""
AIO_KEY=""


def connected(client):
    print("Connected")
    client.subscribe("daily_tracking")
    client.subscribe("total_week")
    client.subscribe("glass_week")
    client.subscribe("paper_week")
    client.subscribe("plastic_week")
    client.subscribe("metal_week")
    client.subscribe("organic_week")
    client.subscribe("ai_camera")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed")

def disconnected(client):
    print("Disconecting...")
    sys.exit (1)

def message(client, feed_id, payload):
    if feed_id == "ai_camera":
        print(f"Received data from feed {feed_id}: {payload}")
        trash_class = payload.rstrip()
        cursor = conn.cursor()
        today = datetime.now().date()
        
        # Check if there's already an entry for the current date
        cursor.execute("SELECT * FROM Waste_Tracking WHERE EntryDate = ?", today)
        existing_data = cursor.fetchone()
        current_week = get_last_week_id(cursor) + 1

        if existing_data:
            # Update the existing record with new quantity
            update_query = f"UPDATE Waste_Tracking SET [{trash_class}] = [{trash_class}] + 1 WHERE EntryDate = ? AND WeekID = ?"
            cursor.execute(update_query, today, current_week)
        else:
            # Insert a new record
            insert_query = f"INSERT INTO Waste_Tracking (EntryDate, WeekID, [{trash_class}]) VALUES (?, ?, 1)"
            cursor.execute(insert_query, today, current_week)
    

        # Save database
        conn.commit()
        # Calculate for daily_bin_tracking table
        calculate_daily()

        # Print out the quantity of each trash class
        trash_types = ["Organic", "Paper", "Glass", "Metal", "Plastic"]
        cursor.execute(f"SELECT {', '.join(trash_types)} FROM Waste_Tracking WHERE EntryDate = ?", today)
        quantities = cursor.fetchone()
        trash_sendback = " ".join(f"{trash_type} {quantity}" for trash_type, quantity in zip(trash_types, quantities))
        # Publish the trash types and their quantities to the "daily_tracking" feed
        client.publish("daily_tracking", trash_sendback)
    cursor.close()

def publish_weekly_data(cursor, client, current_week_id, feed_id, waste_type):
    # Fetch the values for the week
    cursor.execute(f"SELECT {waste_type} FROM Waste_Tracking WHERE WeekID = ?", current_week_id)
    weekly_values = [str(row[waste_type]) for row in cursor.fetchall()]

    # Fetch the Mean value from weekly_tracking
    cursor.execute(f"SELECT Mean_{waste_type} FROM weekly_tracking WHERE WeekID = ?", current_week_id)
    mean_value = str(cursor.fetchone()[0])

    # Publish the values to the specified feed
    values_to_publish = " ".join(weekly_values) + " " + mean_value
    client.publish(feed_id, values_to_publish)
        
    
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

def main():
    last_processed_week = 0  # Initialize the last processed WeekID as 0

    while True:
        cursor = conn.cursor()

        # Check and call calculate_weekly if a new week has started (WeekID 1 -> 2)
        current_week_id = get_last_week_id(cursor)
        if current_week_id > last_processed_week:
            calculate_weekly()
            last_processed_week = current_week_id
            conn.commit()
            publish_weekly_data(cursor, client, current_week_id, "total_week", "TotalQuantity")
            publish_weekly_data(cursor, client, current_week_id, "glass_week", "Glass")
            publish_weekly_data(cursor, client, current_week_id, "paper_week", "Paper")
            publish_weekly_data(cursor, client, current_week_id, "metal_week", "Metal")
            publish_weekly_data(cursor, client, current_week_id, "organic_week", "Organic")

        cursor.close()

        # Calculate the time remaining until end of current week
        now = datetime.datetime.now()
        end_of_week = now + datetime.timedelta(days=(6 - now.weekday()))

        # Calculate the time remaining until end of week
        time_remaining = (end_of_week - now).total_seconds()

        # Sleep until the end of the current week
        time.sleep(time_remaining)
    
if __name__ == "__main__":
    main()
