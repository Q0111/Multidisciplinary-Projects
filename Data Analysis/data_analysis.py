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


def calculate_weekly_statistics():
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
    print("week_ids: ", week_ids)

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

            medians = []
            for i in range(2, len(weekly_data[0])):
                quantities = [data[i] for data in weekly_data]
                median_value = statistics.median(quantities)
                medians.append(median_value)

            std_devs = []
            for i in range(2, len(weekly_data[0])):
                quantities = [data[i] for data in weekly_data]
                std_dev_value = statistics.pstdev(quantities)
                std_devs.append(std_dev_value)
            query = """
            INSERT INTO Weekly_Tracking (
                WeekID, Mean_Organic, Mean_Paper, Mean_Glass, Mean_Metal, Mean_Plastic, Mean_Total,
                Median_Organic, Median_Paper, Median_Glass, Median_Metal, Median_Plastic, Median_Total,
                STD_Organic, STD_Paper, STD_Glass, STD_Metal, STD_Plastic, STD_Total
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, week_id, *means, *medians, *std_devs)
    conn.commit()


def calculate_daily_bin_tracking():
    cursor = conn.cursor()
    waste_types = ["Organic", "Paper", "Glass", "Metal", "Plastic"]

    # Get the EntryDate for yesterday
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday.EntryDate()

    # Fetch data for yesterday
    cursor.execute("SELECT * FROM Daily_Bin_Tracking WHERE EntryDate = ?", yesterday_date)
    daily_data = cursor.fetchone()

    if daily_data:
        # Calculate total quantity for yesterday
        total_quantity = sum(daily_data[i] for i in range(1, len(daily_data)))

        # Calculate fill level
        fill_level = 0 # check sau
        # Insert the data into Daily_Bin_Tracking
        sql_insert_data = f"""
            INSERT INTO Daily_Bin_Tracking (EntryDate, TotalQuantity, FillLevel, {', '.join(waste_types)})
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql_insert_data, yesterday_date, total_quantity, fill_level, *daily_data[1:])

        conn.commit()


def main():
    calculate_weekly_statistics()
    calculate_daily_bin_tracking()


if __name__ == "__main__":
    main()
