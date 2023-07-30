import pyodbc
import statistics
from datetime import datetime, timedelta

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=path;'  # Replace with path to database
)

conn = pyodbc.connect(conn_str)

def get_last_week_id(cursor):
    cursor.execute("SELECT MAX(WeekID) FROM Weekly_Tracking")
    last_week_id = cursor.fetchone()[0]
    return last_week_id or 0


def calculate_weekly():
    cursor = conn.cursor()
    waste_types = ["Organic", "Paper", "Glass", "Metal", "Plastic"]
    # GEt the first entry date in Waste_Tracking table
    cursor.execute("SELECT MIN(EntryDate) FROM Waste_Tracking")
    first_entry_date = cursor.fetchone()[0]
    # Calculate the first WeekID as 1
    week_id = 1
    # Loop through all entries in the Waste_Tracking table and calculate the WeekID
    cursor.execute("SELECT EntryDate FROM Waste_Tracking ORDER BY EntryDate ")
    for entry_date in cursor.fetchall():
        entry_date = entry_date[0]
        if entry_date >= first_entry_date + timedelta(weeks=1):
            week_id += 1
            first_entry_date = entry_date
        
        # Update the WeekID for the corresponding entry in the Waste_Tracking table
        cursor.execute("UPDATE Waste_Tracking SET WeekID = ? WHERE EntryDate = ?", week_id, entry_date)
    conn.commit()

    # Fetch all unique week IDs
    cursor.execute("SELECT DISTINCT WeekID FROM Waste_Tracking")
    week_ids = [row[0] for row in cursor.fetchall()]

    # Calculate statistics for each week
    for week_id in week_ids:
        cursor.execute("SELECT * FROM Waste_Tracking WHERE WeekID = ?", week_id)
        weekly_data = cursor.fetchall()
        # Check if there's data available
        if weekly_data:
            means = []
            for i in range(2, len(weekly_data[0])):
                quantities = [data[i] for data in weekly_data]
                mean_value = statistics.mean(quantities)
                means.append(mean_value)

            query = """
                INSERT INTO Weekly_Tracking (
                    WeekID, Mean_Organic, Mean_Paper, Mean_Glass, Mean_Metal, Mean_Plastic, Mean_Total
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        cursor.execute(query, week_id, *means)
    conn.commit()


def calculate_daily():
    cursor = conn.cursor()
    waste_types = ["Organic", "Paper", "Glass", "Metal", "Plastic"]

    # Get the EntryDate for current date
    today = datetime.now().date()

    # Fetch data from Daily_Bin_Tracking for current date
    cursor.execute("SELECT * FROM Waste_Tracking WHERE EntryDate = ?", today)
    waste_data = cursor.fetchone()

    total_quantity = 0
    for i in range(2, 7):
        total_quantity += waste_data[i]
    cursor.execute("UPDATE Waste_Tracking SET TotalQuantity = ? WHERE EntryDate = ?", total_quantity, today)

  
    # Check if record from daily_bin_tracking table exists
    cursor.execute("SELECT * FROM Daily_Bin_Tracking WHERE EntryDate = ?", today)
    data_today = cursor.fetchone()
    if(data_today):
        # Update the data in Daily_Bin_Tracking table
        sql_update_data = f"""
            UPDATE Daily_Bin_Tracking
            SET TotalQuantity = ?
            WHERE EntryDate = ?
        """
        cursor.execute(sql_update_data, total_quantity, today)
    else:
        insert_query = f"""
        INSERT INTO Daily_Bin_Tracking (EntryDate, TotalQuantity)
        VALUES (?, ?)
    """
        cursor.execute(insert_query, today, total_quantity)
    conn.commit()
