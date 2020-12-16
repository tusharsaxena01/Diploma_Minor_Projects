'''

Simple CUI based Banking Application with the Basic Banking Operations
Which are listed Below:
- Creating a Account
- Deposit
- Withdraw
- Message after each transaction on the screen

'''
import sys

# The Function to call the Team Members if quiting

def Quit():
	teamMembers()
	print("*"*12+" Thank You "+"*"*12)
	return

# Banner Function to make the program more attractive

def banner():
	print("*"*36)
	print("\tBanking Application")
	print("*"*36)

# Team Members and the print operation of their names

def teamMembers():
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

# The Main Function to call each operation as per the need

def bank():
	Account = createAcc()
	order = ['Account Number','Name','Account Type','Balance']
	while True:
		choices = {1:'Deposit',2:'Withdraw',3:'Display',4:'Quit'}
		print("\nOptions\n")
		for num in range(1,len(choices)+1):
			print(num,")",choices[num])
		choice = int(input("\nEnter Your Choice: "))
		if choice == 1:
			Account = Deposit(Account)
		elif choice == 2:
			Account =Withdraw(Account)
		elif choice == 3:
			Display(Account,order)
		elif choice == 4:
			Quit()
			break
		else:
			print("\n\nInvalid Input! Try again...")
	return
		
# An Function for verification of account number

def verify(accInfo):
	userInput = int(input("Enter Your Account Number: "))
	if userInput == accInfo[0]:
		return True
	else:
		return False
# The Deposit function to let the user deposit the amount of money he wants

def Deposit(accInfo):
	if verify(accInfo):
		amount=int(input("Enter the Amount you want to Deposit (In Rs.): "))
		accInfo[3]+=amount
		print("\nUpdated Balance: Rs.",accInfo[3])
	else:
		print("Account Verification Failed!")
	return accInfo
# The withdraw function to let the user withdraw the amount from the money he owns
# Operations for both savings and current accounts'

def Withdraw(accInfo):
	if verify(accInfo):
		amount = int(input("Enter the Amount to want to Withdraw: "))
		if accInfo[2] == "Savings":
			if accInfo[3] < amount:
				print("\nInsufficient Balance!")
				print("\nCurrent Balance: Rs.",accInfo[3])
			elif accInfo[3] >= amount:
				accInfo[3]-=amount
				print("\nUpdated Balance: Rs.",accInfo[3])
		elif accInfo[2] == "Current":
			accInfo[3]-=amount
			print("\nUpdated Balance: Rs.",accInfo[3])
	else:
		print("Account Verification Failed!")
	return accInfo

# The Display function to print all the account details with their correspoding label

def Display(accInfo,order):
	if verify(accInfo):
		print("\nAccount Information:")
		for index in range(0,len(order)):
			print(order[index]+": "+str(accInfo[index]))
	else:
		print("Account Verification Failed!")

# The function to create a new account at the starting of the program

def createAcc():
	print("\nAccount Creation Procedure")
	name = input("\nENTER YOUR FULL NAME: ")
	accType = 0
	while not (accType > 0 and accType < 3):
		accType = int(input("\nSelect Account Type:\n1. Savings\t2. Current\n> "))
	if accType == 1:
		accType = str("Savings")
	elif accType == 2:
		accType = str("Current")
	accNum = int(input("\nENTER YOUR ACCOUNT NUMBER: "))
	bal = int(input("\nENTER THE BALANCE AMOUNT (in Rs.): "))
	accInfo = []
	accInfo.append(accNum)
	accInfo.append(name)
	accInfo.append(accType)
	accInfo.append(bal)
	return accInfo

# The Starting call of the functions are here

banner()
bank()
