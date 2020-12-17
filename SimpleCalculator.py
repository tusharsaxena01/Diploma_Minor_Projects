'''
Simple CUI Calculator
Operation:
1. Addition
2. Substraction
3. Multiplication
4. Division
'''

def Quit():
	teamMembers()
	print("*"*12+" Thank You "+"*"*12)
	return

# Banner Function to make the program more attractive

def banner():
	print("*"*36)
	print("\tSimple Calculator")
	print("*"*36)

# Team Members

def teamMembers():
	# Members List
	members = ['Abhi Saxena','Shivani Singh','Baby Yadav','Siddharth Mani Tiwari','Punam Singh','Ankit Yadav','Shailesh']
	branch = "CSE"
	year = 3
	print("-" * 12 + "Team Members" + "-" * 12)
	for index in range(0,7):
		print("\tName: ", members[index])
		print("\tBranch: " + branch)
		print("\tYear: "+str(year)+"rd Year")
		print("-"*36)
	return

# Main calculator function

def calc():
	while True:
		try:
			num1 = float(input("\nEnter First Number: "))
			operation = int(input("\nOperation to Perform:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Quit\n\nEnter Your Choice: "))
			if operation == 1:
				operation = add
			elif operation == 2:
				operation = sub
			elif operation == 3:
				operation = multiply
			elif operation == 4:
				operation = div
			elif operation == 5:
				Quit()
				break
			else:
				print("Invalid Input! Retry...")
				continue
			num2 = float(input("Enter Second Number: "))
			print("Answer = ",operation(num1,num2))
			
		except ValueError:
			print("Invalid Input! Only A Number allowed!")
			continue

# Addition Function

def add(num1,num2):
	return num1+num2

# Substractiom Function

def sub(num1,num2):
	return num1-num2

# Multiplication Function

def multiply(num1,num2):
	return num1*num2

# Division Function

def div(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		return "Error! Could Not Divide by Zero"

banner()
calc()
