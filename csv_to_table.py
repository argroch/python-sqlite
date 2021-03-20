import csv, sqlite3

# connect to database
my_db = sqlite3.connect("customers.sqlite")
# a cursor object is needed to execute SQL commands in Python
cursorObj = my_db.cursor()
# clear out current table data
cursorObj.execute("DELETE FROM Customer")
# setting CSV file name to a variable - not really need here, but could be applied if we want to ask the user to input the CSV file name
# filename = "customers.csv"

# initially was saving the first row of the CSV (the field names) in a list
# and then the rest of the rows is a separate list. I found a more DRY solution, but are keeping these here for posterity
# fields = [] 
# rows = [] 
  
# The process: first, reading csv file 
with open("customers.csv", 'r') as csvfile: 
  # Next, creating a csv reader object 
  csvreader = csv.reader(csvfile)   
  # After that, skip the first row, because that's just the field names of the db table 
  next(csvreader) 
  # Then, we go row by row of the CSV, adding to the db table.
  # We use a count to repopulate the customerID column.
  count = 1
  for row in csvreader:
 		cursorObj.execute("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
 		count += 1

# Lastly, we commit (save) the changes to the database!
my_db.commit()

# Everything below is a previous version of how I approached the program,
# in which the rows from the csvreader were saved in a list I had initialized back at line 15.
# The below process has been folded into loop-through of the csvreader, seen above

# count = 1
# for row in rows:
	# first_name = row[0]
	# last_name = row[1]
	# company = row[2]
	# address = row[3]
	# city = row[4]
	# province = row[5]
	# postal = row[6]
	# cursorObj.execute("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (count, row[0], row[1], row[2], row[3], row[4], row[5], row[6])) 
	# count += 1
	# my_db.commit()

