
# function to get valid amount 
def amountinput(transaction):
    while True:
        try: 
            amount=int(input("Please enter the amount: "))
            if amount>0:
                transaction['amount']=amount
                break
            else:
                print("Invalid amount. Please enter a positive number.")
                continue
        except (ValueError, TypeError):
            print("Please enter valid amount")
            continue


# function to get valid desciption
def descriptioninput(transaction):
    while True:
        discription=input("What is the transaction about: ")
        if not discription:
            print("Can not return empty input")
            continue
        else:
            transaction['description']=discription
            break

def valid_date(transaction):
    name_of_months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
                     )
    while True:
        date= input("Please enter the date: ")
        
        if not date:
            print("Can not return empty input")
            continue
        else:
            date=date.strip().title()
            parts= date.split()
            if len(parts)==2:
                if parts[0] in name_of_months and parts[1].isdigit() and int(parts[1]) <= 31:
                    transaction['date']=date
                    break
                else:
                    print("Invalid month or day. Please try again.")
            else:
                print("Please enter the date in the format: Jan 01")
                continue
