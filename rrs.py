import mysql.connector as sql 
conn = sql.connect(host="sql6.freesqldatabase.com", 
user="sql6470083", passwd="G4HqJ3xy9V", 
database="sql6470083") 
cursor = conn.cursor() 

#searches for trainnames that match a part of query 
def searchTrain(): 
  x = input("Enter search query: ") 
  cursor.execute('SELECT * FROM Trains WHERE trainname LIKE "%{}%"'.format(x)) 
  printTable() 
  
#creates new record in Tickets table 
def bookTicket(): 
  name = input("Enter Traveller's name: ") 
  train_id = input("Enter Train ID: ") 
  date = input("Enter date of travel (YYYY-MM-DD): ") 
  cursor.execute('INSERT INTO Tickets(name, train_id, date) VALUES("{}", {}, "{}")'.format(name, train_id, date)) 
  conn.commit() 
  print("Ticket booked!") 

#deletes record in Tickets table 
def cancelTicket(): 
  pnr = int(input("Enter PNR: ")) 
  cursor.execute('DELETE FROM Tickets WHERE pnr={}'.format(pnr)) 
  conn.commit() 
  print("Ticket cancelled!") 

#outputs PNR from details 
def checkPNR(): 
  name = input("Enter Traveller's name: ") 
  train_id = input("Enter Train ID: ") 
  date = input("Enter date of travel (YYYY-MM-DD): ") 
  cursor.execute('SELECT * FROM Tickets WHERE name="{}" AND train_id={} AND date="{}"'.format(name, train_id, date)) 
  printTable() 
 
def admin(): 
  #authenticate admin credentials
  user = input("Enter username: ") 
  passwd = input("Enter password: ") 
  if (user, passwd) != ('admin', '12345678'): 
    print("Incorrect username or password!") 
    return 
  print() 
 
  #admin menu
  print("Administrator settings") 
  print("1. Add Train") 
  print("2. Change Train Stations") 
  print("3. Delete Train") 
  print("0. Logout") 
  print() 
  while True: 
    x = int(input("Enter an option (0-3): ")) 
 
  #add a new train
  if x == 1: 
    trainname = input("Enter trainname: ") 
    departure = input("Enter departure: ") 
    arrival = input("Enter arrival: ") 
    price = int(input("Enter price: ")) 
    day = input("Enter day of the week: ") 
    cursor.execute('INSERT INTO Trains(trainname, departure, arrival, price, day) VALUES("{}", "{}", "{}", {}, "{}")'.format(trainname, departure, arrival, price, day)) 
    conn.commit() 
    print("Success!") 
 
  #change destination and arrival
  elif x == 2: 
    train_id = int(input("Enter train_id: ")) 
    departure = input("Enter new departure: ") 
    arrival = input("Enter new arrival: ") 
    cursor.execute('UPDATE Trains SET departure="{}", arrival="{}" WHERE train_id={}'.format(departure, arrival, train_id)) 
    conn.commit() 
    print("Success!") 
 
  #delete a train 
  elif x == 3: 
    train_id = int(input("Enter train_id: ")) 
    cursor.execute('DELETE FROM Trains WHERE train_id={}'.format(train_id)) 
    print("Success!") 
  
  else: 
    print("Logged out") 
    return 
  print() 
 
#prints the result table with a fixed width 
def printTable(): 
  table = cursor.fetchall() 
  if cursor.rowcount == 0: 
    print("No search results") 
    return 
 
  print() 
  for i in cursor.column_names: 
    print(i, end=' '*(11-len(i))) 
  print() 
  for row in table: 
    for i in row: 
      print(i, end=' '*(11-len(str(i)))) 
    print() 

#menu 
print("Welcome to Railway Reservation System!") 
print("1. Search Trains") 
print("2. Book Tickets") 
print("3. Cancel Tickets") 
print("4. Check PNR") 
print("5. Admin") 
print("0. Exit") 
print() 
while True: 
  x = int(input("Enter an option (0-5): ")) 
  if x == 1:  
    searchTrain() 
  elif x == 2: 
    bookTicket() 
  elif x == 3: 
    cancelTicket() 
  elif x == 4: 
    checkPNR() 
  elif x == 5: 
    admin() 
  else: 
    break 
  print() 
conn.close()