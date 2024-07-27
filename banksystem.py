import json

def load_accounts(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_accounts(filename, accounts):
    with open(filename, 'w') as f:
        json.dump(accounts, f)

def create_account(accounts, account_number, owner):
    if account_number not in accounts:
        accounts[account_number] = {
            'owner': owner,
            'balance': 0.0
        }
        return True
    return False

def deposit(accounts, account_number, amount):
    if account_number in accounts and amount > 0:
        accounts[account_number]['balance'] += amount
        return True
    return False

def withdraw(accounts, account_number, amount):
    if account_number in accounts and 0 < amount <= accounts[account_number]['balance']:
        accounts[account_number]['balance'] -= amount
        return True
    return False

def check_balance(accounts, account_number):
    if account_number in accounts:
        return accounts[account_number]['balance']
    return None

if __name__ == "__main__":
    filename = 'accounts.json'
    accounts = load_accounts(filename)

    while True:
        print("\nBank System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            owner = input("Enter owner name: ")
            if create_account(accounts, account_number, owner):
                print("Account created successfully.")
                save_accounts(filename, accounts)
            else:
                print("Account already exists.")
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if deposit(accounts, account_number, amount):
                print("Deposit successful.")
                save_accounts(filename, accounts)
            else:
                print("Failed to deposit.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if withdraw(accounts, account_number, amount):
                print("Withdrawal successful.")
                save_accounts(filename, accounts)
            else:
                print("Failed to withdraw or insufficient funds.")
        elif choice == '4':
            account_number = input("Enter account number: ")
            balance = check_balance(accounts, account_number)
            if balance is not None:
                print(f"Account balance: ${balance:.2f}")
            else:
                print("Account not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
