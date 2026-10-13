import sys
import os
import json

EXPENSEFILE = "expense.json"


#------------STORAGE LAYER------------------------>

def load_expense():
    if os.path.exists(EXPENSEFILE):
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
    return task

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

    expense = load_expense()
    expense = {
        "description": args[1],
        "amount": args[3]
    }
    save_expense(expense)
    print(f"successsfully added expense {args1}")

def main():
    add_expense(sys.argv[2:])

if __name__ == "__main__":
    main()
