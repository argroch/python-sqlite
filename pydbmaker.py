# Going to have all my non-SQL-related code in here
# This will be the program to run, and will pull SQL-related methods
# from "sqlite_cmds.py"

from sqlite_cmds import *
from pydb_classes import *
from os import system, name, path
from time import sleep
import glob, os

def main_menu():
	print("Welcome to Aaron's Python DB Builder!")
	print("Please choose from the following:")
	print("=================================")
	print("1. Create a Database\n2. Modify a Database\n3. Quit")
	choice = int(input(""))

	if choice == 1:
		clearscreen()
		db_create()
	elif choice == 2:
		clearscreen()
		db_list()
	elif choice == 3:
		clearscreen()
		print("Okay... see you later, then!")
	elif choice == 4:
		clearscreen()
		print("Secret testing area!")
		testing()
	else:
		print("Oops! Invalid entry! Let's try that again!")
		sleep(1)
		clearscreen()
		main_menu()

# A method to clear the command prompt/terminal screen
def clearscreen(): 
  # for windows 
  if name == 'nt': 
      _ = system('cls') 
  # for mac and linux(here, os.name is 'posix') 
  else: 
      _ = system('clear')

# A method for creating a new database 
def db_create():
	print("Let's create a database!")
	db_name = input("Give your database a name: ")
	current_db = sql_connection(db_name + ".db")
	print("Congrats! Your database (" + db_name + ") has been created!")
	print("Please note: if a database by that name already existed, it will not have been duplicated.\nCheck 'Modify Database' to see if this database has existing tables.")
	sleep(3)
	db_create_menu(current_db)

# A method for dealing with menu after DB creation.
# Put it here on its own due to recursive property of invalid response. 
def db_create_menu(db):
	print("Now what?\n1. Modify Database\n2. Return to Main Menu\n3. Quit")
	choice = int(input(""))
	if choice == 1:
		clearscreen()
		db_modify(db)
	elif choice == 2:
		clearscreen()
		main_menu()
	elif choice == 3:
		clearscreen()
		print("It's been fun! Catch ya later!")
	else:
		clearscreen()
		print("What?! Invalid response! Try again, please.")
		sleep(1)
		db_create_menu(db)

# A method to list the databases in the project,
# and allow user to choose one to modifying
def db_list():
	print("Which database do you want to modify?")
	print("=====================================")
	cur_dir = os.getcwd()
	os.chdir(cur_dir)
	count = 1
	db_names = []
	for file in glob.glob("*.db"):
		print(str(count) + ". " + file)
		count += 1
		db_names.append(file)
	choice = int(input("Choose database by number: "))
	db_name = db_names[choice-1]
	current_db = sql_connection(db_name)
	db_modify(current_db)

# A method for modifying a datbase
def db_modify(db):	
	cursorObj = db.cursor()
	cursorObj.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
	table_list = cursorObj.fetchall() # list of the tables
	if len(table_list) == 0:
		# no tables
		print("There currently no tables in this database.")
		choice = input("Do you want to create a new one now? (y/n) ")
		if choice == "y" or choice == "Y":
			clearscreen()
			table_name = new_table(db, cursorObj)
		else:
			clearscreen()
			print("Well... then... to the Main Menu with you!")
			sleep(1)
			main_menu()
	# there is at least one table:
	else:
		print("Current list of tables in this database:")
		count = 1
		table_choices = []
		for table in table_list:
			print(str(count) + ". " + table[0])
			count += 1
			table_choices.append(table)
		choice = int(input("Choose table by number: "))
		table_name = table_choices[choice-1][0]
	add_data(db, cursorObj, table_name) # move on to add data to table 

# A method to collect info about a new table and create it
def new_table(db, cursorObj):
	print("Let's create a new table in this database!")
	table_name = input("Name the table: ")
	number_of_fields = int(input("How many fields/columns will this table have? "))
	clearscreen()
	print("Now we will create the table's columns, please provide a column NAME and a DATA TYPE for each column, as well as whether that column will hold the PRIMARY KEY (by answering with 'y' for yes, or 'n' for no. The prompts will end once you have provided the requested info for the number of columns specified on the previous screen.")
	sleep(0.5)
	count = 1
	fields_list = []
	while count <= number_of_fields:
		# Create a Column class with properties of name, datatype, and primary_key
		# ask for field name
		name = input("Field name: ")
		# ask for data type
		dt = input("Data type: ")
		# ask if primary key; set as True or False
		pk = False
		primary = input("Will it be the primary key? (y/n) ")
		if primary == "y" or primary == "Y":
			pk = True
		# create instance of Column
		col = Column(name, dt, pk)
		# add to fields_arr
		if col.pk == True: # Primary Key column will be at the front of the list
			fields_list.insert(0, col)
		else: # every other column added to the end
			fields_list.append(col)
		# incrementing count
		count += 1
	# so now fields_arr should have some cols in it [col, col, col]
	# the col at index 0 should be the Primary Key

	# Creating a String of columns' elements in order to add that to a SQL command
	# The String will start with the column at index 0 (Primary Key column)
	fields_str = fields_list[0].name + " " + fields_list[0].dt + " PRIMARY KEY, "
	# now to add the other columns to that string, looping through the list
	count = 1
	while count < len(fields_list):
		# is the column last in the list? - no comma
		if count == (len(fields_list) - 1):
			fields_str = fields_str + fields_list[count].name + " " + fields_list[count].dt
		# any other column gets a comma and a space after it
		else:
			fields_str = fields_str + fields_list[count].name + " " + fields_list[count].dt + ", "
		# incrementing count
		count += 1

	# okay, so we should now have a String that resembles part of a SQL command
	# something like: "id text PRIMARY KEY, name text, age real"
	# Now we can pass that, along with the db, cursorObj, and table_name to the
	# create_table method imported from sqlite_cmds
	create_table(db, cursorObj, table_name, fields_str)
	print("The " + table_name + " table has been successfully created!\nNow what?")
	new_table_menu(db, cursorObj, table_name)

# A method to house menu for after creating a new table
def new_table_menu(db, cursorObj, table_name):
	print("1. Add data to table\n2. Create another table\n3. Return to Main Menu")
	choice = int(input("Choose by number: "))

	if choice == 1:
		clearscreen()
		add_data(db, cursorObj, table_name)
	elif choice == 2:
		create_table(db, cursorObj, table_name)
	elif choice == 3:
		main_menu()
	else:
		clearscreen()
		print("Invalid repsonse. Please try again. Like an adult.")
		new_table_menu(db, cursorObj, table_name)

# A method to add data to a table
def add_data(db, cursorObj, table_name):
	print("Add data to the " + table_name + " table.\n")
	columns = cursorObj.execute("SELECT * FROM " + table_name)
	names = list(map(lambda x: x[0], columns.description))
	print(names)
	# find last id number, if id is a column in this table
	# otherwise, I'm going to assume they have specific custom ID numbers to enter
	if 'id' in names:
		cursorObj.execute("SELECT MAX(id) FROM " + table_name)
		last_id = cursorObj.fetchone()
		# print(last_id)
		print("For reference, the current final ID number is: " + str(last_id[0]))

	# user will add data for one entry, then say whether or not they want to continue adding a second data set
	print("Follow the prompts!")
	cont = True
	while cont == True:
		data = []
		count = 0
		while count < len(names):
			data_pt = input(names[count] + ": ")
			data.append(data_pt)
			count += 1
		
		# now format the data to fit in a SQL command and execute that command, then commit to the db
		#################
		data_str = ','.split(data) # BUT WHAT IF THERE'S A COMMA IN THE data_pt? IT WILL READ AN ADDITIONAL data_pt. THAT'S BAD.
		#################
		# determine the amount of question marks needed for the Values() section
		q_marks = ""
		for i in range(0,(len(names))):
			q_marks += "?, "
		q_marks = q_marks[:-2] # removing final comma and space from end of string

		cursorObj.execute("INSERT INTO " + table + " VALUES(" + q_marks + ")", ())
		db.commit()


	main_menu()

# My secret testing area! Shhh!
def testing():
	# cur_dir = os.getcwd()
	# os.chdir(cur_dir)
	# for file in glob.glob("*.py"):
	# 	print(file)
	sleep(3)
	main_menu()



# The call that starts it all
main_menu()