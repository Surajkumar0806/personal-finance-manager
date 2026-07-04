import json, csv
import os


project_folder=os.path.dirname(__file__)
csv_path=os.path.join(project_folder, "transactions.csv")
json_path=os.path.join(project_folder, "transactions.json")




def load_data():
    try:
        with open(json_path, "r") as file:
            return json.load(file)
    except( FileNotFoundError, json.JSONDecodeError):
        return []
    

def export_data(transactions):
        with open(csv_path, "w", newline="") as file:
            writer= csv.writer(file)
            header=["date", "type", "amount", "description"]
            writer.writerow(header) 
            for transaction in transactions:
                details=[transaction["date"],
                        transaction["type"],
                        transaction["amount"],
                        transaction["description"] ]    
                writer.writerow(details)
        print("Transactions exported successfully.")
            


def save_data(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)


