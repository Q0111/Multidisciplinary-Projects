import pyodbc
import matplotlib.pyplot as plt

# Connect to the database
conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path;') #path = Replace with path to database EX: C:\\example.accdb

# Create a cursor
cursor1 = conn.cursor()

# Execute a query
##############################################################
cursor1.execute("SELECT Organic FROM Waste_Tracking WHERE EntryDate = 'day'") #day = Enter the required date Ex: 29/07/2023 or 01/08/2023

x =[]
for row in cursor1:
    # Append
    x.append(row[0])
# Close the cursor
cursor1.close()
sumx = sum(x)
##############################################################
cursor2 = conn.cursor()
cursor2.execute("SELECT Paper FROM Waste_Tracking WHERE EntryDate = 'day'") #day = Enter the required date Ex: 29/07/2023 or 01/08/2023
# Create a list to store the values
y = []

# Iterate over the rows in the result set
for row in cursor2:
    # Append
    y.append(row[0])

# Close the cursor
cursor2.close()
sumy=sum(y)
######################################################
cursor3 = conn.cursor()
cursor3.execute("SELECT Glass FROM Waste_Tracking WHERE EntryDate = 'day'") #day = Enter the required date Ex: 29/07/2023 or 01/08/2023
# Create a list to store the values
z = []

# Iterate over the rows in the result set
for row in cursor3:
    # Append
    z.append(row[0])

# Close the cursor
cursor3.close()
sumz=sum(z)
######################################################
cursor4 = conn.cursor()
cursor4.execute("SELECT Metal FROM Waste_Tracking WHERE EntryDate = 'day'") #day = Enter the required date Ex: 29/07/2023 or 01/08/2023
# Create a list to store the values
g = []

# Iterate over the rows in the result set
for row in cursor4:
    # Append
    g.append(row[0])

# Close the cursor
cursor4.close()
sumg=sum(g)
######################################################
cursor5 = conn.cursor()
cursor5.execute("SELECT Plastic FROM Waste_Tracking WHERE EntryDate = 'day'") #day = Enter the required date Ex: 29/07/2023 or 01/08/2023
# Create a list to store the values
h = []

# Iterate over the rows in the result set
for row in cursor5:
    # Append
    h.append(row[0])

# Close the cursor
cursor5.close()
sumh=sum(h)

namewaste = ['Organic', 'Paper', 'Glass', 'Metal', 'Plastic']
numberwaste = [sumx, sumy, sumz, sumg, sumh]

colors = ['red', 'orange', 'yellow', 'green', 'blue']

plt.bar(namewaste, numberwaste, color = colors)


# Add a title to the graph
plt.title('Daily bar chart')

# Add labels to the x-axis
plt.xlabel('Name of waste')

# Add labels to the y-axis
plt.ylabel('Number')

# Show the graph
plt.show()
