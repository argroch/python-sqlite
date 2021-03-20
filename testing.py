names = ['id', 'first_name', 'last_name', 'city']

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
	print(data[0])

	choice = input("Add another? (y/n) ")
	if choice == "n":
		cont = False

# q_marks = ""
# for i in range(0,(len(names))):
# 	q_marks += "?, "

# q_marks = q_marks[:-2]
# print(q_marks)