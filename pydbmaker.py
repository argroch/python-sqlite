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
		print("Let's modify that database!")
		print("Under construction!")
		sleep(1)
		main_menu()
		# sql_connection(db_name)
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
	current_db = sql_connection(db_name)
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
		modify_db(db)
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

def modify_db(db):
	print("Still working on this one. Try again later!")
	sleep(3)
	main_menu()


# My secret testing area! Shhh!
def testing():
	cur_dir = os.getcwd()
	os.chdir(cur_dir)
	for file in glob.glob("*.py"):
		print(file)
	sleep(3)
	main_menu()



# The call that starts it all
main_menu()