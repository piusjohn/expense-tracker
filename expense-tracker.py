import sys
import os
import json
from datetime import datetime

EXPENSEFILE = "expense.json"
#------------HELPER FUNCTIONS--------------------->
def now():
    return datetime.now().isoformat(timespec="hours")

def next_id(expenses):
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses)+1


#------------STORAGE LAYER------------------------>

def load_expense():
    if not os.path.exists(EXPENSEFILE):
        return []
    try:
        with open(EXPENSEFILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content == "":
                return []
            expense = json.loads(content)
    except json.JSONDecodeError:
        print(f"Error: {EXPENSEFILE} is not valid, fix or delete it")
        sys.exit()
    except OSError:
        print(f"Error: {EXPENSEFILE} could not read file")
        sys.exit()
    if not isinstance(expense, list):
        print(f"Error: {EXPENSEFILE} must be a list")
        sys.exit()
    return expense

def save_expense(expense):
    temp = EXPENSEFILE + ".tmp"
    try:
        with open(temp, "w", encoding="utf-8") as f:
            json.dump(expense, f, indent=2)
        os.replace(temp, EXPENSEFILE)
    except OSError as e:
        print(f"could not write file: {e}")
        sys.exit()
    
#----------------LOGIC----------------------->

def add_expense(args):
    timestamp = now()
    expense = load_expense()
    list = {
        "id": next_id(expense),
        "description": args[1],
        "amount": args[3],
        "createdAt": timestamp
    }
    expense.append(list)
    save_expense(expense)
    print(f"Expense added successfully (ID: {list["id"]})")

def list_expense():
    expenses = load_expense()
    # ID  Date       Description  Amount
    print("ID  Date       Description  Amount")
    for expense in expenses:
        
        print(f"{expense["id"]}  {expense["createdAt"]}    {expense["description"]}  {expense["amount"]}")

def summary_expense():
    expenses = load_expense()
    print(sum(int(expense["amount"]) for expense in expenses))
    
def delete_expense(args):
    id = args[1]
    expenses = load_expense()
    temp = []
    for expense in expenses:
        if expense["id"] != int(id):
            temp.append(expense)
    save_expense(temp)
    print("deleted successfully")
            


def main():
    if sys.argv[1] == "add":
        add_expense(sys.argv[2:])
    if sys.argv[1] == "list":
        list_expense()
    if sys.argv[1] == "summary":
        summary_expense()
    if sys.argv[1] == "delete":
        delete_expense(sys.argv[2:])


if __name__ == "__main__":
    main()
