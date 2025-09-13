
print("\nActivity 1")
print("Welcome to Bank System!")
print("*******************************");

balance = 0;
exit = True;
choice = 0;

def check_balance():
    print(f"Your balance is: {balance}");
def deposit():
    global balance
    deposit_amount = float(input("Enter the amount you want to deposit in (pesos): "))
    balance += deposit_amount;
    print(f"{deposit_amount} has been added to your balance.");
    print(f"Your new balance is {balance}");
def withdraw():
    global balance
    withdraw_amount = float(input("Enter the amount you want to withdraw in (pesos): "))
    if withdraw_amount > balance:
        print("Insufficient balance.");
    else:
        balance -= withdraw_amount
        print(f"{withdraw_amount} has been deducted to your balance.");
        print(f"Remaining balance: {balance}");



while exit:
    print("\nWelcome to the Bank")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using the bank. Goodbye!")
        exit = False;
    else:
        print("Invalid option. Please try again.")