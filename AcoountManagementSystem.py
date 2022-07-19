from managers.ManagersManager import ManagersManager
from managers.AccountHolderManager import AccountHolderManager
from managers.AccountManager import AccountManager
from managers.LoanManager import LoanManger
from managers.OverdraftManager import OverdraftManager

account_holder_manager = AccountHolderManager()
manager_system = ManagersManager()
account_manager = AccountManager()
loan_manager = LoanManger()
overdraft_manager = OverdraftManager()


def main_menu():
    print("""Welcome to CodeBank
    Enter 1 to Access Account Holder Menu
    Enter 2 to Access Manager Menu
    Enter 0 to Quit
    -->""")


def sub_menu(option):
    if option == 0:
        print("Thank you for using CodeBank")
    elif option == 1:
        holder_register_login_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            holder_sub_menu(action)
    elif option == 2:
        manager_register_login_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            manager_sub_menu(action)


def holder_register_login_menu():
    print("""Account Holder Menu:
    Enter 1 to create bank account
    Enter 2 to login account holder
    Enter 0 to go back
    -->""")


def manager_register_login_menu():
    print("""Manager Menu:
    Enter 1 to create manager account
    Enter 2 to login manager
    Enter 0 to go back
    -->""")


def holder_sub_menu(action):
    if action == 1:
        print("REGISTER ACCOUNT HOLDER")
        first_name = str(input("Enter your first name: "))
        last_name = str(input("Enter your last name: "))
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        confirm_password = str(input("Enter your password again: "))
        pin = int(input("Enter your pin: "))
        phone_number = str(input("Enter your phone number: "))
        holder = account_holder_manager.create_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name,
            last_name=last_name, phone_number=phone_number)
        if holder is False:
            print("password must match")
        else:
            account = account_manager.create_account(account_holder=holder, pin=pin)
            if account:
                print("You have successfully registered your account and your account number is",
                      account)
            else:
                print("Password must match")

    elif action == 2:
        print("ACCOUNT HOLDER LOGIN")
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        login = account_holder_manager.login_account_holder(email=email, password=password)
        if login is False:
            print('Incorrect password')
        else:
            show_holder_menu()
            action = int(input())
            if action == 0:
                holder_register_login_menu()
            else:
                handle_holder_menu(action)

    sub_menu(1)


def manager_sub_menu(option):
    if option == 1:
        print("REGISTER MANAGER")
        first_name = str(input("Enter your first name: "))
        last_name = str(input("Enter your last name: "))
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        confirm_password = str(input("Enter your password again: "))
        phone_number = str(input("Enter your phone number: "))
        manager = manager_system.create_manager(
            email=email, password=password,confirm_password=confirm_password, first_name=first_name,
            last_name=last_name, phone_number=phone_number)
        if manager is False:
            print("incorrect password")
        else:
            print("registration successful")

    elif option == 2:
        print("MANAGER LOGIN")
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        login = manager_system.login_manager(email=email, password=password)
        if login is True:
            show_manager_menu()
            action = int(input())
            if action == 0:
                manager_register_login_menu()
            else:
                handle_manager_menu(action)

    sub_menu(2)


def show_holder_menu():
    print("""Account Holder Menu:
    Enter 1 for account transactions
    Enter 2 to loan transactions
    Enter 3 to overdraft transactions
    Enter 0 to go back
    -->""")


def show_manager_menu():
    print("""Manager Menu:
    Enter 1 for account transactions
    Enter 2 to loan transactions
    Enter 3 to overdraft transactions
    Enter 0 to go back
    -->""")


def handle_holder_menu(action):
    if action == 1:
        holder_account_menu()
        action = int(input())
        if action == 0:
            holder_register_login_menu()
        else:
            handle_holder_account_menu(action)
    if action == 2:
        holder_loan_menu()
        action = int(input())
        if action == 0:
            holder_register_login_menu()
        else:
            handle_holder_loan_menu(action)
    if action == 3:
        holder_overdraft_menu()
        action = int(input())
        if action == 0:
            holder_register_login_menu()
        else:
            handle_holder_overdraft_menu(action)


def handle_manager_menu(action):
    if action == 1:
        manager_account_menu()
        action = int(input())
        if action == 0:
            manager_register_login_menu()
        else:
            handle_manager_account_menu(action)

    if action == 2:
        manager_loan_menu()
        action = int(input())
        if action == 0:
            manager_register_login_menu()
        else:
            handle_manager_loan_menu(action)
    if action == 3:
        manager_overdraft_menu()
        action = int(input())
        if action == 0:
            manager_register_login_menu()
        else:
            handle_manager_overdraft_menu(action)


def holder_account_menu():
    print("""Account Holder: Account:
    Enter 1 to update details
    Enter 2 to change password
    Enter 3 to change pin
    Enter 4 to make deposit
    Enter 5 to make withdrawal
    Enter 0 to go back
    -->""")


def holder_loan_menu():
    print("""Account Holder: Loan:
    Enter 1 to obtain a loan
    Enter 2 to check loan balance
    Enter 3 to pay back a loan
    Enter 0 to go back
    -->""")


def holder_overdraft_menu():
    print("""Account Holder: Overdraft:
    Enter 1 to get overdraft
    Enter 
    Enter 0 to go back
    -->""")


def manager_account_menu():
    print("""Manager: Account:
    Enter 1 to update manager details
    Enter 2 to change password
    Enter 3 to list account holders
    Enter 4 to search account holder
    Enter 5 to block an account
    Enter 6 to unblock an account
    Enter 0 to go back
    -->""")


def manager_loan_menu():
    print("""Manager: Loan:
    Enter 1 to search loans
    Enter 2 to list loans
    Enter 0 to go back
    -->""")


def manager_overdraft_menu():
    print("""Manager: Overdraft:
    Enter 1 to search overdraft
    Enter 2 to list overdraft
    Enter 0 to go back
    -->""")


def handle_holder_account_menu(action):
    if action == 1:
        email = str(input("Enter your email address: "))
        print("UPDATE ACCOUNT HOLDER DETAILS")
        first_name = str(input("Enter new first name: "))
        last_name = str(input("Enter new last_name: "))
        phone_number = str(input("Enter new phone number: "))
        new_holder = account_holder_manager.update_account_holder(email=email, first_name=first_name,
                                                                  last_name=last_name, phone_number=phone_number)
        if new_holder is True:
            print('Update valid')
        else:
            print('Update Invalid')

    elif action == 2:
        email = str(input("Enter your email address: "))
        print("CHANGE PASSWORD")
        new_password = str(input("Enter your new password: "))
        confirm_password = str(input("Confirm your new password: "))
        status = account_holder_manager.change_password(
            email=email, new_password=new_password, confirm_password=confirm_password)
        if status is True:
            print("Password Changed")
        else:
            print("Password not valid")

    elif action == 3:
        print("DEPOSIT")
        pin = int(input("Enter your pin: "))
        amount = float(input("Enter the amount: "))
        account_number = str(input("Enter the account number: "))
        deposit = account_manager.deposit(pin=pin, amount=amount, account_number=account_number)
        if deposit is True:
            print("transaction successful")
        else:
            print("Incorrect pin")

    elif action == 4:
        print("WITHDRAWAL")
        pin = int(input("Enter your pin: "))
        amount = float(input("Enter the amount: "))
        account_number = str(input("Enter the account number: "))
        withdrawal = account_manager.withdraw(pin=pin, account_number=account_number, amount=amount)
        if withdrawal is True:
            print("transaction successful")
        else:
            print("Incorrect pin")


def handle_holder_loan_menu(action):
    if action == 1:
        print("GET LOAN")
        account_number = str(input('Enter Your account Number: '))
        pin = int(input('Enter Your pin: '))
        print("""
        Enter 0 for Household Loan Amount: """f'{loan_manager.loan_types.get("household")}'"""
        Enter 1 for Car Loan: """f'{loan_manager.loan_types.get("car")}'"""
        Enter 2 for School fees Loan: """f'{loan_manager.loan_types.get("school fee")}'"""
        Enter 3 For Business Loan: """f'{loan_manager.loan_types.get("business")}'"""
        Enter 4 for Emergency loan: """f'{loan_manager.loan_types.get("emergency")}'"""
        """)
        val = int(input())
        loan_type = handle_loan_type(val)
        number_of_mounts = int(input('Enter numbers of months to pay back: '))
        account = account_manager.return_account(account_number=account_number, pin=pin)
        loan = loan_manager.create_loan(account=account, loan_type=loan_type, number_of_months=number_of_mounts)
        try:
            if loan['not_granted']:
                print(loan['not_granted'])
        except KeyError:
            print(loan['message'])

    elif action == 2:
        print("PAY LOAN")
        account_number = str(input('Enter Your account Number: '))
        amount = float(input("Enter the amount you want to pay: "))
        payment = loan_manager.pay_back(account_number=account_number, amount=amount)
        try:
            print(payment['pay'])
        except IndexError:
            print(payment['pay_success'])


def handle_loan_type(val: int):
    loan_names = ['household', 'car', 'school fee', 'business', 'emergency']
    for name in range(len(loan_names)):
        if val == name:
            return loan_names[name]


def handle_holder_overdraft_menu(action):
    if action == 1:
        print("GET OVERDRAFT")
        account_number = str(input('Enter Your account Number: '))
        pin = int(input('Enter Your pin: '))
        amount = float(input("Enter amount: "))
        account = account_manager.return_account(account_number=account_number, pin=pin)
        overdraft = overdraft_manager.get_overdraft(account=account, amount=amount)
        try:
            print(overdraft['see_manager'])
        except KeyError:
            print(overdraft['message'])

    elif action == 2:
        print("PAY OVERDRAFT")
        account_number = str(input('Enter Your account Number: '))
        amount = float(input("Enter the amount you want to pay: "))
        payment = overdraft_manager.pay_overdraft(account_number=account_number, amount=amount
                                                  )
        try:
            print(payment['pay'])
        except IndexError:
            print(payment['pay_success'])


def handle_manager_account_menu(action):
    if action == 1:
        print("UPDATE  MANAGER DETAILS")
        first_name = str(input("Enter your first name: "))
        last_name = str(input("Enter your last_name: "))
        phone_number = str(input("Enter your phone number: "))
        new_manager = manager_system.update_manager(first_name=first_name, last_name=last_name,
                                                    phone_number=phone_number)
        if new_manager is True:
            print('Update valid')
        else:
            print('Update Invalid')

    elif action == 2:
        print("CHANGE MANAGER PASSWORD")
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        login = manager_system.login(email=email, password=password)
        if login is True:
            new_password = str(input("Enter your new password: "))
            manager_system.change_password(new_password=new_password)
            print("Password Changed")
        else:
            print("Password not valid")

    elif action == 3:
        print("LIST OF ACCOUNT HOLDERS")
        account_holder_manager.list_account_holders()

    elif action == 4:
        print("SEARCH FOR A ACCOUNT HOLDERS")
        email = str(input("Enter the email of the account holder: "))
        account_holder_manager.search(email=email)

    elif action == 5:
        email = str(input("Enter the email address: "))
        status = account_holder_manager.delete_account_holder(email=email)
        if status is True:
            print("Account Deleted")
        else:
            print("Account not deleted")

    elif action == 6:
        email = str(input("Enter the email address: "))
        status = account_holder_manager.delete_account_holder(email=email)
        if status is True:
            print("Account Deleted")
        else:
            print("Account not deleted")

    elif action == 7:

        email = str(input("Enter the email address: "))
        status = account_holder_manager.delete_account_holder(email=email)
        if status is True:
            print("Account Deleted")
        else:
            print("Account not deleted")


def handle_manager_loan_menu(action):
    if action == 1:
        print("SEARCH FOR A LOAN")
        account_number = str(input("Enter the account number: "))
        loan = loan_manager.search_loan(account_number=account_number)
        if loan is False:
            print("Wrong account number")
        else:
            print(loan.id, '\t', loan.status, '\t', loan.loan_type)

    elif action == 2:
        print("LIST OF LOANS")
        loan_manager.list_loan()


def handle_manager_overdraft_menu(action):
    if action == 1:
        print("SEARCH FOR OVERDRAFT")
        account_number = str(input("Enter the account number: "))
        overdraft = overdraft_manager.search_overdraft(account_number=account_number)
        if overdraft is False:
            print("Wrong account number")
        else:
            print(overdraft.id, '\t', overdraft.status, '\t', overdraft.balance)

    elif action == 2:
        print("LIST OF LOANS")
        overdraft_manager.list_overdraft()


def main():
    flag = True
    while (flag):
        main_menu()
        option = int(input())
        if (option == 0):
            print("Thanks for banking with CodeBank!!")
            flag = False
        else:
            sub_menu(option)


main()