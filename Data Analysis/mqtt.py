from data_analysis import get_last_week_id, calculate_daily, calculate_weekly
import pyodbc
import statistics
from datetime import datetime, timedelta
import time
from Adafruit_IO import MQTTClient

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=D:\WasteManagement.accdb;' # Path to database
)
conn = pyodbc.connect(conn_str)

AIO_USERNAME="Group_X"
AIO_KEY="aio_ohZj58L5NCwcGm0pGHeev13PayiT"


def connected(client):
    print("Connected")
    client.subscribe("daily_tracking")
    client.subscribe("total_week")
    client.subscribe("glass_week")
    client.subscribe("paper_week")
    client.subscribe("plastic_week")
    client.subscribe("metal_week")
    client.subscribe("orgainc_week")
    client.subscribe("ai_camera")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed")

def disconnected(client):
    print("Disconecting...")
    sys.exit (1)

def message(client, feed_id, payload):
    print(f"Received data from feed {feed_id}: {payload}")
    if feed_id == "ai_camera":
        trash_class = payload
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
    

        # Print out the updated quantity
        cursor.execute("SELECT [{0}] FROM Waste_Tracking WHERE EntryDate = ?".format(trash_class), today)
        quantity = cursor.fetchone()[0]
        daily_tracking = f"{trash_class}: {quantity}"
        conn.commit()
        time.sleep(5)
        calculate_daily()
        time.sleep(5)
        
    
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

def main():
    while True:
        pass
    
if __name__ == "__main__":
    main()
