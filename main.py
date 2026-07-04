import json
import csv
from storage import load_data , save_data, export_data
from transaction import *
from validation import *
#welcome message

print("============Welcome to your personal Finance manager=================")




#list of transations 
transactions=load_data()




#main menu function 
def menu():
    print()
    print("       1. Add Income")
    print()
    print("       2. Add Expenses")
    print()
    print("       3. Delete Transactions")
    print()
    print("       4. View Transactions")
    print()
    print("       5. Search Transactions")
    print()
    print("       6. Edit Transactions")
    print()
    print("       7. monthly Summary")
    print()
    print("       8. Filter The Transactions")
    print()
    print("       9. Export to csv format")
    print()
    print("       0. Exit")
    print()



#main loop 
while True:
    menu()
    choice=input("please choose one option: ")

    if choice=="1":
        print("you can add your income here")
        add_transaction("income", transactions)
    elif choice=="2":
        print("you can add your expenses here")
        add_transaction("expense", transactions)
    elif choice=="3":
        print("you can delete the transaction here")
        delete_Transacttion(transactions)
    elif choice=="4":
        print("here is the details of the transaction: ")
        viewalltransaction(transactions)
    elif choice=="5":
        if transactions:
            searchin=input("input 1 to search based on date\n" \
            "input 2 to search based on amount\n" \
            "input 3 to search based on type of transaction\n" \
            "input 4 to search based on purposes of transaction\n")
            if searchin=="1":
                searchvalue=input("enter the date you are looking for: ")
                searchvalue=searchvalue.title()
                search_Transaction(searchvalue, transactions)
            elif searchin=="2":
                searchvalue=int(input("enter the amount: "))
                search_Transaction(searchvalue, transactions)
            elif searchin=="3":
                searchvalue=input("are you looking for income/expense ") 
                search_Transaction(searchvalue, transactions)
            elif searchin=="4":
                searchvalue=input("what was the purpose of the transaction  ")
                search_Transaction(searchvalue, transactions)
        else:
            print("no transaction")
    elif choice=="6": 
        print("edit transaction")
        edit_Transaction(transactions)
    elif choice=="7":
        monthly(transactions)
    elif choice=="8":
        filterin=input("type income to fliter based on income\n" \
        "type expense to filter based on expense\n" \
        "Enter the month to filter based on month\n Enter ")
        filterin=filterin.strip()
        filter_Transaction(filterin, transactions)
    elif choice=="9":
        export_data(transactions)
    elif choice=="0":
        print("Thank you for chosing personal finance manager")
        save_data(transactions)
        break
    else:
        print("Invalid menu choice. Please try again.")


