current_balance=0
def deposit(amount):
        global current_balance
        current_balance += amount
        return current_balance
def withdraw(amount):
        global current_balance
        current_balance -= amount
        if (amount>current_balance):
            return None
            print("Insufficient balance for withdrawal.")
            return current_balance
print("Your current balance is:",current_balance)
while True:
    print("Choose an option: ")
    print("1.deposit")
    print("2.withdraw")
    print("3.Check Balance")
    print("4.Exit")
    try:
        choice=int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    if choice==1:
        deposit_amount=int(input("Enter amount to deposit: "))
        new_balance=deposit(deposit_amount)
        print("Your balance after deposit is:",new_balance)
    elif choice==2:
        withdraw_amount=int(input("Enter amount to withdraw: "))
        new_balance=withdraw(withdraw_amount)
        if new_balance is None:
            print("Insufficient balance for withdrawal.")
        else:
            print("Your balance after withdrawal is:",new_balance)
    elif choice==3:
        print("Your current balance is:",current_balance)
    elif choice==4:
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    print("Your current balance is:",current_balance)

