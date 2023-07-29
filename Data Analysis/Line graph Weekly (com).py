import pyodbc
import matplotlib.pyplot as plt
import numpy as np

# Connect to the database
conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path;') #path = Replace with path to database EX: C:\\example.accdb

###################################Organic Waste#######################################

# Create a cursor
cursor1x = conn.cursor()

# Execute a query

cursor1x.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

x =[]
for row in cursor1x:
    # Append
    x.append(row[0])
# Close the cursor
cursor1x.close()

sumx = sum(x)

cursor1y = conn.cursor()
cursor1y.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

y =[]
for row in cursor1y:
    # Append
    y.append(row[0])
# Close the cursor
cursor1y.close()

sumy = sum(y)

cursor1z = conn.cursor()
cursor1z.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

z =[]
for row in cursor1z:
    # Append
    z.append(row[0])
# Close the cursor
cursor1z.close()

sumz = sum(z)

cursor1g = conn.cursor()
cursor1g.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

g =[]
for row in cursor1g:
    # Append
    g.append(row[0])
# Close the cursor
cursor1g.close()

sumg = sum(g)

cursor1h = conn.cursor()
cursor1h.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

h =[]
for row in cursor1h:
    # Append
    h.append(row[0])
# Close the cursor
cursor1h.close()

sumh = sum(h)

cursor1e = conn.cursor()
cursor1e.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

e =[]
for row in cursor1e:
    # Append
    e.append(row[0])
# Close the cursor
cursor1e.close()

sume = sum(e)


cursor1f = conn.cursor()
cursor1f.execute("SELECT Organic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

f =[]
for row in cursor1f:
    # Append
    f.append(row[0])
# Close the cursor
cursor1f.close()

sumf = sum(f)

organicwaste = [sumx, sumy, sumz, sumg, sumh, sume, sumf]

dayinweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


plt.plot(dayinweek, organicwaste, marker='o', markerfacecolor='red')

plt.axhline(np.mean(organicwaste), color='green', label='Mean')
plt.axhline(np.median(organicwaste), color='black', label='Median')
plt.legend()

plt.title('Weekly line graph for Organic waste')

# Add labels to the x-axis
plt.xlabel('Day in week')

# Add labels to the y-axis
plt.ylabel('Number')

plt.show()

###################################Paper Waste#######################################

# Create a cursor
cursor1x = conn.cursor()

# Execute a query

cursor1x.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

x =[]
for row in cursor1x:
    # Append
    x.append(row[0])
# Close the cursor
cursor1x.close()

sumx = sum(x)

cursor1y = conn.cursor()
cursor1y.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

y =[]
for row in cursor1y:
    # Append
    y.append(row[0])
# Close the cursor
cursor1y.close()

sumy = sum(y)

cursor1z = conn.cursor()
cursor1z.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

z =[]
for row in cursor1z:
    # Append
    z.append(row[0])
# Close the cursor
cursor1z.close()

sumz = sum(z)

cursor1g = conn.cursor()
cursor1g.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023
g =[]
for row in cursor1g:
    # Append
    g.append(row[0])
# Close the cursor
cursor1g.close()

sumg = sum(g)

cursor1h = conn.cursor()
cursor1h.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

h =[]
for row in cursor1h:
    # Append
    h.append(row[0])
# Close the cursor
cursor1h.close()

sumh = sum(h)

cursor1e = conn.cursor()
cursor1e.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

e =[]
for row in cursor1e:
    # Append
    e.append(row[0])
# Close the cursor
cursor1e.close()

sume = sum(e)


cursor1f = conn.cursor()
cursor1f.execute("SELECT Paper FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

f =[]
for row in cursor1f:
    # Append
    f.append(row[0])
# Close the cursor
cursor1f.close()

sumf = sum(f)

paperwaste = [sumx, sumy, sumz, sumg, sumh, sume, sumf]

dayinweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


plt.plot(dayinweek, paperwaste, marker='o', markerfacecolor='red')

plt.axhline(np.mean(paperwaste), color='green', label='Mean')
plt.axhline(np.median(paperwaste), color='black', label='Median')
plt.legend()

plt.title('Weekly line graph for Paper waste')

# Add labels to the x-axis
plt.xlabel('Day in week')

# Add labels to the y-axis
plt.ylabel('Number')

plt.show()

###################################Glass Waste#######################################

# Create a cursor
cursor1x = conn.cursor()

# Execute a query

cursor1x.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

x =[]
for row in cursor1x:
    # Append
    x.append(row[0])
# Close the cursor
cursor1x.close()

sumx = sum(x)

cursor1y = conn.cursor()
cursor1y.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

y =[]
for row in cursor1y:
    # Append
    y.append(row[0])
# Close the cursor
cursor1y.close()

sumy = sum(y)

cursor1z = conn.cursor()
cursor1z.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

z =[]
for row in cursor1z:
    # Append
    z.append(row[0])
# Close the cursor
cursor1z.close()

sumz = sum(z)

cursor1g = conn.cursor()
cursor1g.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

g =[]
for row in cursor1g:
    # Append
    g.append(row[0])
# Close the cursor
cursor1g.close()

sumg = sum(g)

cursor1h = conn.cursor()
cursor1h.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

h =[]
for row in cursor1h:
    # Append
    h.append(row[0])
# Close the cursor
cursor1h.close()

sumh = sum(h)

cursor1e = conn.cursor()
cursor1e.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

e =[]
for row in cursor1e:
    # Append
    e.append(row[0])
# Close the cursor
cursor1e.close()

sume = sum(e)


cursor1f = conn.cursor()
cursor1f.execute("SELECT Glass FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

f =[]
for row in cursor1f:
    # Append
    f.append(row[0])
# Close the cursor
cursor1f.close()

sumf = sum(f)

glasswaste = [sumx, sumy, sumz, sumg, sumh, sume, sumf]

dayinweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


plt.plot(dayinweek, glasswaste, marker='o', markerfacecolor='red')

plt.axhline(np.mean(glasswaste), color='green', label='Mean')
plt.axhline(np.median(glasswaste), color='black', label='Median')
plt.legend()

plt.title('Weekly line graph for Glass waste')

# Add labels to the x-axis
plt.xlabel('Day in week')

# Add labels to the y-axis
plt.ylabel('Number')

plt.show()

###################################Metal Waste#######################################

# Create a cursor
cursor1x = conn.cursor()

# Execute a query

cursor1x.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

x =[]
for row in cursor1x:
    # Append
    x.append(row[0])
# Close the cursor
cursor1x.close()

sumx = sum(x)

cursor1y = conn.cursor()
cursor1y.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

y =[]
for row in cursor1y:
    # Append
    y.append(row[0])
# Close the cursor
cursor1y.close()

sumy = sum(y)

cursor1z = conn.cursor()
cursor1z.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

z =[]
for row in cursor1z:
    # Append
    z.append(row[0])
# Close the cursor
cursor1z.close()

sumz = sum(z)

cursor1g = conn.cursor()
cursor1g.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

g =[]
for row in cursor1g:
    # Append
    g.append(row[0])
# Close the cursor
cursor1g.close()

sumg = sum(g)

cursor1h = conn.cursor()
cursor1h.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

h =[]
for row in cursor1h:
    # Append
    h.append(row[0])
# Close the cursor
cursor1h.close()

sumh = sum(h)

cursor1e = conn.cursor()
cursor1e.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

e =[]
for row in cursor1e:
    # Append
    e.append(row[0])
# Close the cursor
cursor1e.close()

sume = sum(e)


cursor1f = conn.cursor()
cursor1f.execute("SELECT Metal FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

f =[]
for row in cursor1f:
    # Append
    f.append(row[0])
# Close the cursor
cursor1f.close()

sumf = sum(f)

metalwaste = [sumx, sumy, sumz, sumg, sumh, sume, sumf]

dayinweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


plt.plot(dayinweek, metalwaste, marker='o', markerfacecolor='red')

plt.axhline(np.mean(metalwaste), color='green', label='Mean')
plt.axhline(np.median(metalwaste), color='black', label='Median')
plt.legend()

plt.title('Weekly line graph for Metal waste')

# Add labels to the x-axis
plt.xlabel('Day in week')

# Add labels to the y-axis
plt.ylabel('Number')

plt.show()

###################################Plastic Waste#######################################

# Create a cursor
cursor1x = conn.cursor()

# Execute a query

cursor1x.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = day AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

x =[]
for row in cursor1x:
    # Append
    x.append(row[0])
# Close the cursor
cursor1x.close()

sumx = sum(x)

cursor1y = conn.cursor()
cursor1y.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

y =[]
for row in cursor1y:
    # Append
    y.append(row[0])
# Close the cursor
cursor1y.close()

sumy = sum(y)

cursor1z = conn.cursor()
cursor1z.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

z =[]
for row in cursor1z:
    # Append
    z.append(row[0])
# Close the cursor
cursor1z.close()

sumz = sum(z)

cursor1g = conn.cursor()
cursor1g.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

g =[]
for row in cursor1g:
    # Append
    g.append(row[0])
# Close the cursor
cursor1g.close()

sumg = sum(g)

cursor1h = conn.cursor()
cursor1h.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

h =[]
for row in cursor1h:
    # Append
    h.append(row[0])
# Close the cursor
cursor1h.close()

sumh = sum(h)

cursor1e = conn.cursor()
cursor1e.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") #Enter the week

e =[]
for row in cursor1e:
    # Append
    e.append(row[0])
# Close the cursor
cursor1e.close()

sume = sum(e)


cursor1f = conn.cursor()
cursor1f.execute("SELECT Plastic FROM Waste_Tracking WHERE WeekID = week AND EntryDate = 'day' ") # week = Enter the week Ex: 1 or 2, day = Enter the required date Ex: 29/07/2023 or 01/08/2023

f =[]
for row in cursor1f:
    # Append
    f.append(row[0])
# Close the cursor
cursor1f.close()

sumf = sum(f)

plasticwaste = [sumx, sumy, sumz, sumg, sumh, sume, sumf]

dayinweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


plt.plot(dayinweek, plasticwaste, marker='o', markerfacecolor='red')

plt.axhline(np.mean(plasticwaste), color='green', label='Mean')
plt.axhline(np.median(plasticwaste), color='black', label='Median')
plt.legend()

plt.title('Weekly line graph for Plastic waste')

# Add labels to the x-axis
plt.xlabel('Day in week')

# Add labels to the y-axis
plt.ylabel('Number')

plt.show()