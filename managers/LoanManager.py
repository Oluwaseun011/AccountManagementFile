import datetime

from models.Loan import Loan
from models.Account import Account
from typing import List


class LoanManger:
    loans: List[Loan] = []

    file = open("Loan.txt", "a+")

    loan_types = {
        'household': 100000,
        'car': 500000,
        'school fee': 200000,
        'business': 1000000,
        'emergency': 50000
    }

    message = {}

    def create_loan(self, account: Account, loan_type: str, number_of_months: int):
        id = self.__get_id()
        loan = Loan(account=account, loan_type=loan_type)
        if_any_loan_active = self.__check_if_no_active_loan(account_number=loan.account.account_number)
        if if_any_loan_active is True:
            self.message["pay"] = 'You have a pending loan, Pay up first!'
            return self.message
        else:
            loan.amount = self.__get_loan_amount_by_loan_type(loan_type=loan_type)
            loan.status = 'active'
            loan.interest_rate = self.__get_loan_interest_rate(number_of_months == number_of_months)
            loan.balance = self.__get_loan_initial_balance(interest_rate=loan.interest_rate, amount=loan.amount)
            loan.loan_type = loan_type
            loan.id = self.__get_id()
            self.loans.append(loan)
            if self.file.closed is True:
                self.file = open("Loan.txt", "a+")
            else:
                self.file.write(f"{str(loan)}""\n")
                self.file.flush()
            answer = 'Loan granted, Your loan amount is: ', loan.amount, 'you are to pay back within, ', number_of_months
            return answer

    def list_loan(self):
        for loan in self.loans:
            self.__show(loan)

    def loan_balance(self, account_number: str):
        loan = self.__get_loan(account_number=account_number)
        if loan:
            self.__show_loan_balance(loan=loan)
        else:
            answer = 'You have no pending loan balance'
            return answer

    def pay_back(self, account_number: str, amount: float):
        loan = self.__get_loan(account_number=account_number)
        if loan is not False:
            loan.balance -= amount
            if loan.balance == 0:
                loan.status = 'inactive'
                answer = 'Loan Totally paid'
                self.__refresh_file()
                return answer
            else:
                answer = 'Payment successful, yu have ', loan.balance, 'left to pay'
                self.__refresh_file()
                return answer
        else:
            answer = 'No active loan found'
            return answer

    def search(self, account_number: str):
        loan = self.__find(account_number)
        if loan is None:
            return False
        else:
            self.__show(loan)

    def __check_if_no_active_loan(self, account_number: str):
        for loan in self.loans:
            if loan.account.account_number == account_number:
                if loan.status == 'active':
                    return True
        return False

    def __get_loan_amount_by_loan_type(self, loan_type: str):
        for loan in self.loan_types:
            if loan == loan_type:
                return self.loan_types[loan]

    def __find(self, account_number: str): 
        for loan in self.loans:
            if loan.account.account_number == account_number:
                return loan
            else:
                return None

    def __show_overdraft_balance(self, loan: Loan):
        print('Your loan balance is: ', loan.balance)

    def __get_loan_interest_rate(self, number_of_months: int):
        interest_rate = number_of_months / 100
        return interest_rate

    def __get_loan_initial_balance(self, interest_rate: int, amount: int):
        val = float(interest_rate * amount)
        amount += val
        return val

    def __get_id(self):
        length = len(self.loans)
        if length == 0:
            length += 1
            return length
        else:
            for loan in self.loans:
                if loan.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __get_loan(self, account_number: str):
        for loan in self.loans:
            if loan.account.account_number == account_number:
                if loan.status == 'active':
                    return loan
                else:
                    return False

    def __show(self, loan: Loan):
        print('LOAN ID: ', loan.id, '\n', 'DATE COLLECTED: ', loan.date, '\n', 'LOAN BALANCE: ', loan.balance, '\n', 'LOAN TYPE: ', loan.loan_type)

    def __show_loan_balance(self, loan: Loan):
        print('Your loan balance is: ',loan.balance)

    def __refresh_file(self):
        self.file = open("Loan.txt", "w")
        for loan in self.loans:
            self.file.write(str(loan))
            self.file.write("\n")
        self.file.flush()
