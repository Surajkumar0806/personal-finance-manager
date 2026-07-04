
from validation import *



#funcntion of questions to collect required data 
def add_transaction(tratype, transactions):
        
            transaction={}
            
            valid_date(transaction)
            print()
            transaction['type']=tratype
            print()
            amountinput(transaction)
            print()
            descriptioninput(transaction)
            print()
            transactions.append(transaction)
            print("       Entry done")

def print_transaction(transaction):
    for key, value in transaction.items():
        print(f"   {key} : {value}")
    print("-----------------")

#function to disply all transactions             
def viewalltransaction(transactions):
        if transactions:
                for index, transaction in enumerate(transactions):
                    print(f"Transaction {index + 1}")
                    print_transaction(transaction)
        else:
            print("        No transactions entered")


#function to delete transaction 
def delete_Transacttion(transactions):
    if transactions:
        viewalltransaction(transactions)
        deletein=int(input("Enter the serial number of the transaction: "))-1
        if deletein >= 0 and deletein<len(transactions):
            deletevalue=transactions[deletein]
            print_transaction(deletevalue)
            response=input("press y/n: ")
            if response=="y":     
                transactions.pop(deletein)
                viewalltransaction(transactions)
            elif response=="n":
                print("Delete request canceled")
        else:
             print("Please enter correct serial number")


#function to edit transaction
def edit_Transaction(transactions):
    if transactions:
        viewalltransaction(transactions)
        editin=int(input("Enter the serial number of the transaction: "))-1
        if editin >= 0 and editin<len(transactions):
            editvalue=transactions[editin]
            print_transaction(editvalue)
            editvaluein=input("what do you want to edit Date, Amount, Transaction Type or Description: ")
            if editvaluein=="date":
                editvalue["date"]=input("Edit date: ")
            elif editvaluein=="amount":
                amountinput(editvalue)
            elif editvaluein=="type":
                typein=input("Edit as income/expense")
                if typein=="income" or typein=="expense":
                    editvalue["type"]=typein
                else:
                    print("Enter only income/ expense")
            elif editvaluein=="description":
                descriptioninput(editvalue)
            else:
                print("Invalid action enter date, amount, type or description as input")
            viewalltransaction(transactions)
    else:
        print("No Transaction")


def monthly(transactions):
    month_found=False
    total_income=0
    total_expense=0
    month=input("Enter the Month: ")
    month=month.strip().title()
    if transactions:
        for transaction in transactions:
            searchmonth=transaction["date"].split()
            if month==searchmonth[0]:
                month_found=True
                if transaction["type"]=="income":
                    total_income+=transaction["amount"]
                elif transaction["type"]=="expense":
                    total_expense+=transaction["amount"]
        if not month_found:
            print(f"No transaction found for {month}")
        else:
            print(f"Your this month's total income {total_income}\n your this month's total expense is {total_expense}\n and your current balance is {total_income-total_expense} ")
    else:
        print("No transactions")            
        



#search function
def search_Transaction(thing, transactions):
        found=False
        if transactions:
            for transaction in transactions:
                if thing in transaction.values():
                    found=True
                    print_transaction(transaction)

            if found==False:
                print("Search failed, result not found")


def filter_Transaction(filterin, transactions):
    if filterin=="income" or filterin=="expense":
        search_Transaction(filterin, transactions)
    elif filterin=="month":
        month_name=input("enter the month")
        month_found=False
        month_name=month_name.title()
        if transactions:
            for transaction in transactions:
                searchmonth=transaction["date"].split()
                if month_name==searchmonth[0]:
                    month_found=True
                    print_transaction(transaction)
            if month_found== False:
                print("No related transaction")
        else:
            print("No transactions")
    else:
        print("Invalid action, you can only filter based on income/expense and month")

