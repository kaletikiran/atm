import os
from time import sleep
from random import choice   # to create a random Card Number
from python_mysql_dbconfig import read_db_config,read_db_config_cbs
from db_lib import MySQLDataBase    # to store customer informations
import time
import sys
from tabulate import tabulate

# create a database object for mysql
conn = MySQLDataBase().connection(read_db_config())
cursor = conn.cursor()

# create a database object for cbsmysql
connCbs = MySQLDataBase().connection(read_db_config_cbs())
cursorCbs = connCbs.cursor()

# create a table
cursor.execute(''' CREATE TABLE IF NOT EXISTS customers
(cardNumber INT PRIMARY KEY, name TEXT, surname TEXT, pin INT, mail TEXT, money REAL)''')
conn.commit()



# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

# This function provides to exit the program
def exitProgram():
    print("Logging Out...")
    time.sleep(1)
    #signIn()
    sys.exit(0)

# ATM Main Menu
def mainMenu(cardNumber):
    cardNum = cardNumber
    print('''
    #############################################################
    #                                                           #
    # *  Select the bank transaction you want to make. (1-8)    #
    #                                                           #
    # 1. View account information                               #
    # 2. Change your pin                                        #
    # 3. Cash withdrawal                                        #                
    # 4. Deposit your cash                                      #
    # 5. Transfer funds between linked bank accounts            #
    # 6. Mini Statement                                         #
    # 7. Logout                                                 #        
    # 8. Quit                                                   #
    #                                                           #
    #############################################################
    ''')
    select = int(input("Select: "))

    if select <= 8:
        if select == 1:
            viewAccount(cardNum) # new
        elif select == 2:
            changePin(cardNum)
        elif select == 3:
            withdraw(cardNum)
        elif select == 4:
            deposit(cardNum)
        elif select == 5:
            transfer(cardNum)
        elif select == 6:
            ministmt(cardNum)    
        elif select == 7:
            home()
        elif select == 8:
            exitProgram()
    else:
        print("Please enter an integer (1-8)")
        mainMenu(cardNumber)

# This function provides to write amount of money.
def amountOfMoney(cardNumber):
    	
    fetchBal = cursorCbs.execute("select c.balance AS bal from customer c,atmcards a where a.cardNumber = '%s' and a.accountNo = c.acno"%(cardNumber))
    custBal = cursorCbs.fetchone()
    for bal in custBal:
    	print("\nAmount of current balance(CBS):", bal)

# This function provides to write amount of money.
def amountOfMoneyInCbs(cardNumber):
    fetchBal = cursorCbs.execute("select c.balance AS bal from customer c,atmcards a where a.cardNumber = '%s' and a.accountNo = c.acno"%(cardNumber))
    custBal = cursorCbs.fetchone()
    for bal in custBal:
    	return bal

# This function return the value based on given table name, coulumn name and where condition

def getRecordFromTable(tableValues):
    #return tableValues
    fetchBal = cursorCbs.execute("select "+tableValues[1]+" AS bal from "+tableValues[0]+" where "+tableValues[2]+" = '%s'"%(tableValues[3]))
    custBal = cursorCbs.fetchone()
    for bal in custBal:
    	return bal
    	
# This function display last n txns of customer

def ministmt(cardNumber):
    sleep(2)
    screen_clear()
    print("Last 5 transactions from your card:\n")
    # execute your query
    cursor.execute("SELECT * FROM atm_txns WHERE cardNumber='%s' order by dot DESC limit 5"%(cardNumber,))
  
    # fetch all the matching rows 
    result = cursor.fetchall()
    print(tabulate(result, headers=['RR No', 'Card No', 'Amount', 'To Card No', 'TXN Type', 'Date of txn'], tablefmt='psql')) 
    '''# loop through the rows
    for row in result:
      print(row)
      print("\n") '''
    mainMenu(cardNumber)
    
    
# This function shows customer informations
def viewAccount(cardNumber):
    sleep(2)
    screen_clear()
    cbsBalance = amountOfMoneyInCbs(cardNumber)
    infoCustomer = cursor.execute("SELECT * FROM customers WHERE cardNumber='%s'"%(cardNumber))
    for (cardNumber, name, surname,pin,mail,money) in cursor:
	    print("\nPersonal Information")
	    print("----------------------------------")
	    print("\nCard Number:", cardNumber)
	    print("Name:", name)
	    print("Surname:", surname)
	    print("PIN:", pin)
	    print("Mail:", mail)
	    print("Money:", cbsBalance)
	    print("----------------------------------\n")
	    
    mainMenu(cardNumber)

# This function provides to send money to other bank account.
def transfer(cardNumber):
    amountOfMoney(cardNumber)
    transferCardNumber = input("\nEnter the card number of the account you will send money to: ")
    if transferCardNumber.isdigit() == True:
        transferCardNumber = int(transferCardNumber)
        cursor.execute("SELECT * FROM customers WHERE cardNumber='%s'"%(transferCardNumber))
        if cursor.fetchone() is not None:
            question = input("\nAre you sure you have entered the correct Card Number? (yes: y / no: n): ").lower()
            if question == "y":
                transferMoney = input("\nEnter an amount of money to send: ")
                if transferMoney.isdigit() or transferMoney.isdecimal() == True:   
                    rr_num = choice(range(100000, 999999))
                    txn_type = "ATMTFR"              
                    cursor.execute("UPDATE customers SET money = money + ('%s') WHERE cardNumber = '%s'"%(transferMoney, transferCardNumber))
                    cursor.execute("UPDATE customers SET money = money - ('%s') WHERE cardNumber = '%s'"%(transferMoney, cardNumber))
                    cursor.execute(''' INSERT INTO `atm_txns` (`rr_num`, `cardNumber`, `amount`,`to_cardNumber`, `txn_type`) VALUES ('%s','%s','%s','%s','%s')'''%(rr_num, cardNumber, transferMoney,transferCardNumber, txn_type))
                    conn.commit()
                    screen_clear()
                    print("\nFunds transfer transaction is Successful!\n")
                    mainMenu(cardNumber)
                else:
                    print("Please enter INTEGER or DECIMAL numbers")
                    transfer(cardNumber)
            elif question == "n":
                transfer(cardNumber)
            else:
                print("Invalid Answer. Try Again.")
                transfer(cardNumber)
        else:
            #sleep(2)
            #screen_clear()
            #mainMenu(cardNumber)
            print("Invalid Card Number, Please Try Again.")
            transfer(cardNumber)
    else:
        #sleep(2)
        #screen_clear()
        #mainMenu(cardNumber)
        print("WRONG Card Number. Please enter the INTEGER Card Number!")
        transfer(cardNumber)

# This function provides to change your PIN
def changePin(cardNumber):
    try:
        newPin = int(input("Enter your new PIN: "))
        cnewPin = int(input("Confirm your new PIN: "))
        if newPin != cnewPin:
              sleep(2)
              screen_clear()
              print("\n#############################")
              print("PIN mismatch")
              print("#############################\n")
              #mainMenu(cardNumber)
              
        else:
              cursor.execute("UPDATE customers SET pin = '%s' WHERE cardNumber='%s'", (newPin, cardNumber))
              sleep(2)
              screen_clear()
              print("\n#############################")
              print("Your new pin:", newPin)
              print("#############################\n")
              conn.commit()
    except:
        print("\nPlease enter integer PIN\n")
        changePin(cardNumber)
    else:
        mainMenu(cardNumber)

# This function provides to deposit your cash
def deposit(cardNumber):
    amountOfMoney(cardNumber)
    cbsBalance = amountOfMoneyInCbs(cardNumber)
    try:
        rr_num = choice(range(10000, 99999))
        txn_type = "ATMDEP"
        
        addMoney = float(input("\nHow much money do you want to deposit into your account?: "))
        print("\nThe money is deposited into your account...\n")
        tableValues = ["atmcards","accountNo","cardNumber",cardNumber]
        accountNo = getRecordFromTable(tableValues)
        #print(accountNo)        
        time.sleep(2)
        screen_clear()
        
        cursor.execute("UPDATE customers SET money = '%s' + ('%s') WHERE cardNumber='%s'"%(cbsBalance, addMoney, cardNumber))
        cursor.execute(''' INSERT INTO `atm_txns` (`rr_num`, `cardNumber`, `amount`, `txn_type`) VALUES ('%s','%s','%s','%s')'''%(rr_num, cardNumber, addMoney,txn_type))
        conn.commit()
        
        cbs_type = txn_type + "/" + str(rr_num) + "/" + str(cardNumber)
        cursorCbs.execute("UPDATE customer,atmcards SET customer.balance = customer.balance + ('%s') WHERE atmcards.cardNumber='%s' and atmcards.accountNo = customer.acno"%(addMoney, cardNumber))
        cursorCbs.execute(''' INSERT INTO `transaction` (`amount`, `type`,  `acno`) VALUES ('%s','%s','%s')'''%(addMoney, cbs_type, accountNo))
        connCbs.commit()
        
        amountOfMoney(cardNumber)
    except:
        print("\nInvalid Value. Please Try Again.")
        deposit(cardNumber)
    else:
        mainMenu(cardNumber)

# This function provides to withdraw from your account
def withdraw(cardNumber):
    amountOfMoney(cardNumber)
    cbsBalance = amountOfMoneyInCbs(cardNumber)
    try:
        rr_num = choice(range(1000, 9999))
        txn_type = "ATMWDL"
        
        addMoney = float(input("\nHow much money do you want to withdraw from your account?: "))
        if addMoney <= cbsBalance :
            print("\nThe money is being drawn ...\n")
            tableValues = ["atmcards","accountNo","cardNumber",cardNumber]
            accountNo = getRecordFromTable(tableValues)
            #print(accountNo)
            cursor.execute("UPDATE customers SET money = '%s' - ('%s') WHERE cardNumber='%s'"%(cbsBalance, addMoney, cardNumber))
            cursor.execute(''' INSERT INTO `atm_txns` (`rr_num`, `cardNumber`, `amount`,  `txn_type`) VALUES ('%s','%s','%s','%s')'''%(rr_num, cardNumber, addMoney, txn_type))
            conn.commit()
            
            cbs_type = txn_type + "/" + str(rr_num) + "/" + str(cardNumber)
            cursorCbs.execute("UPDATE customer,atmcards SET customer.balance = customer.balance - ('%s') WHERE atmcards.cardNumber='%s' and atmcards.accountNo = customer.acno"%(addMoney, cardNumber))
            cursorCbs.execute(''' INSERT INTO `transaction` (`amount`, `type`,  `acno`) VALUES ('%s','%s','%s')'''%(addMoney, cbs_type, accountNo))
            connCbs.commit()
            time.sleep(2)
	    #sleep(2)
            screen_clear()
            amountOfMoney(cardNumber)
        else:
            time.sleep(2)
            screen_clear()
            print("\nThere is no sufficient balance in your account. Please check and try lesser amount ...\n")
    
    except:
        print("\nInvalid Value. Please Try Again.")
        mainMenu(cardNumber)
    else:
        mainMenu(cardNumber)

# This function creates an account for customer
def signUp():
    try:
        cardNumber = choice(range(1000, 10000))
        name = input("Enter your name: ").capitalize()
        surname = input("Enter your surname: ").capitalize()
        
        while True:
            pin = input("Enter a pin: ")
            if pin.isdigit() == True:
                break
            else:
                print("\nYou should enter only integer value for pin.\n")
        while True:
            mail = input("Enter a mail (gmail): ")
            if "@gmail.com" in mail:
                break
            else:
                print("\nYou should use Gmail ('@gmail.com') account.\n")
        money = float(input("Enter the amount of money: "))
        cursor.execute(''' INSERT INTO customers VALUES 
        ('%s', '%s', '%s', '%s', '%s', '%s')'''%(cardNumber, name, surname, pin, mail, money))
        conn.commit()
        #infoCustomer = cursor.execute("SELECT * FROM customers WHERE cardNumber='%s'"%(cardNumber))
        print("\nRegistration Successful!\n")
        print("\nYour Card Number:",cardNumber,"\n")
        print("\nYour PIN Number:",pin,"\n")
        #viewAccount(cardNumber)
    except:
        print("Invalid Value. Please Try Again.")
        signUp()
    else:
        sleep(5)
        screen_clear()
        mainMenu(cardNumber)

# This function provides to sign in to your account. 
def signIn():
    cardNumber = int(input("Enter your Card Number: "))
    pin = int(input("Enter your PIN: "))
    cursor.execute("SELECT * FROM customers WHERE cardNumber='%s' AND pin='%s'"%(cardNumber,pin))
    if cursor.fetchone() is not None:
        welcomeName = cursor.execute("SELECT name FROM customers WHERE cardNumber='%s'"%(cardNumber))
        #print(welcomeName)
        myIter = cursor.fetchone()
        sleep(2)
        screen_clear()
        for name in myIter:
        	print("\nWelcome Dear,", name)
        
        mainMenu(cardNumber)
    else:
        print("\nWRONG Card Number or PIN, Please Try Again.\n")
        signIn()

def home():
    while True:
        screen_clear()
        print("\n", "-"*20, "Welcome to our IDRBT ATM", "-"*20, "\n\n")
        print('''
        ###################################################
        #                                                 #
        #  SIGN IN (enter 'I')        SIGN UP (enter 'U') # 
        #                                                 #
        #                 EXIT (enter 'E')                #
        #                                                 #
        ###################################################
        '''.upper())
        
        question = input("Select: ").lower()

        if question == "i":
            signIn()
            break
        elif question == "u":
            signUp()
            break
        elif question == 'e':
            exitProgram()
        else:
            print("Invalid Keyword, Please Try Again.")

home()
