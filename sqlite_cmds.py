# 

import sqlite3
import os

# A method to establish a connection to a database;
# will create database file if none exists
def sql_connection(db):
	connection = sqlite3.connect(db)
	return connection

# A method to create a table within the database
# database is passed as a parameter
def create_table(db, cursorObj, table_name, fields):
	# the .execute() method (pre-written) takes SQL commands as a parameter and runs (executes) it
	# cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

	cursorObj.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + fields + ");")
	# then we'll use .commit() method to save to the database
	db.commit()

# A method to add to the table we created in the database
# it takes the database and the table name as arguments
def add_to_table(db, table, cursorObj):
	# taking user input for table data
	empId = table_size(db, cursorObj) + 1
	name = input("Employee name: ")
	salary = input("Salary: ")
	dept = input("Department: ")
	position = input("Position: ")
	hireDate = input("Hire date (yyyy-mm-dd): ")
	# use .execute to run a SQL INSERT command
	cursorObj.execute("INSERT INTO " + table + " VALUES(?, ?, ?, ?, ?, ?)", (empId, name, salary, dept, position, hireDate))
	# commit the changes to the database
	db.commit()

# A method to determine a table's size,
# basically to determine ID values for new entries
def table_size(db, cursorObj):
	cursorObj.execute("SELECT * FROM employees")
	rows = cursorObj.fetchall()
	return len(rows)

# making our method calls:
# my_db = sql_connection() # database connected
# a cursor object is needed to execute SQL commands in Python
	# here we create one using .cursor() pre-written method
# cursorObj = my_db.cursor()
# create_table(my_db, cursorObj) # table created if not already existing
# add_to_table(my_db, "employees", cursorObj) # adding a new table