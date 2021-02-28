# Going to have all my non-SQL-related code in here
# This will be the program to run, and will pull SQL-related methods
# from "sqlite_cmds.py"

from sqlite_cmds import *
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
		sleep(3)
		clearscreen()
		main_menu()
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
			print(str(count) + ". " + table)
			count += 1
			table_choices.append(table)
		choice = int(input("Choose table by number: "))
		table_name = table_choices[choice-1]
	# modify table here


def new_table(db, cursorObj):
	print("Let's create a new table in this database!")
	table_name = input("Name the table: ")
	number_of_fields = input("How many fields/columns will this table have? ")
	count = 1
	fields_arr = []
	while count <= number_of_fields:
		column_arr = [] # !!! Maybe better to create a Column class with properties of name, datatype, and primary_key
		# ask for field name
		# ask for data type
		# ask if primary key; set as True or False
		# create instance of Column,
		# add to fields_arr



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