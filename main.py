import sqlite3

# method to establish a connection to our database
# will create database file if none exists
def sql_connection():
	connection = sqlite3.connect('mydatabase.db')
	return connection

# method to create a table within the database
# database is passed as a parameter
def create_table(db):
	# a cursor object is needed to execute SQL commands in Python
	# here we create one using .cursor() pre-written method
	cursorObj = db.cursor()
	# the .execute() method (pre-written) takes SQL commands as a parameter and runs (executes) it
	cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
	# then we'll use .commit() method to save to the database
	db.commit()

# method to add to the table we created in the database
# it takes the database and the table name as arguments
def add_to_table(db, table):
	# create a new cursor object
	cursorObj = db.cursor()
	# use .execute to run a SQL INSERT command
	cursorObj.execute("INSERT INTO " + table + " VALUES(1, 'Joe Schmoe', 120000, 'Engineering', 'Lead Engineer', '2015-11-15')")
	# commit the changes to the database
	db.commit()

# making our method calls:
my_db = sql_connection() # database connected
create_table(my_db) # table created if not already existing
add_to_table(my_db, "employees") # adding a new table