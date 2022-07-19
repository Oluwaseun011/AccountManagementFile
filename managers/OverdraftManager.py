from models.Overdraft import Overdraft
from models.Account import Account
from typing import List
import datetime


class OverdraftManager:
    overdrafts: List[Overdraft] = []

    file = open("Overdraft.txt", "a+")

    def create_overdraft(self, account: Account, amount: float):
        active_account = self.__is_account_active(account)
        if active_account is True:
            if amount <= 100000.00:
                overdraft_status = self.__is_overdraft_not_active(account_number=account.account_number)
                if overdraft_status is False:
                    overdraft = Overdraft(account=account, amount=amount)
                    overdraft.id = self.__get_id()
                    overdraft.balance = amount
                    overdraft.account.account_balance -= amount
                    overdraft.status = 'active'
                    overdraft.date = datetime.date.today()
                    self.overdrafts.append(overdraft)
                    if self.file.closed is True:
                        self.file = open("Overdraft.txt", "a+")
                    else:
                        self.file.write(f"{str(overdraft)}""\n")
                        self.file.flush()
                    answer = 'Overdraft collected'
                    return answer
                else:
                    answer = 'You have already collected an overdraft. Please pay up'
                    return answer
            else:
                answer = 'You cannot collect above 100 thousand'
                return answer
        else:
            answer = 'Account is not active'
            return answer

    def overdraft_balance(self, account_number: str, pin: int):
        overdraft = self.__get_overdraft(account_number=account_number, pin=pin)
        if overdraft:
            self.__show_overdraft_balance(overdraft)
        else:
            answer = 'You have no pending overdraft'
            return answer

    def list_overdraft(self):
        for overdraft in self.overdrafts:
            self.__show(overdraft)

    def search(self, account_number: str):
        overdraft = self.__find(account_number)
        if overdraft is None:
            return False
        else:
            self.__show(overdraft)

    def __check__amount__overdraft(self, account_number: str):
        for Overdraft in self.overdrafts:
            if Overdraft.amount <= 100000:
                return True
        return False

    def __find(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                return overdraft
            else:
                return None

    def __get_overdraft_initial_balance(self, amount: float):
        val = 100000
        amount = val
        return amount

    def __check_if_no_active_overdraft(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.overdraft_status == 'active':
                    return True
        return False

    def __get_id(self):
        length = len(self.overdrafts)
        if length == 0:
            length += 1
            return length
        else:
            for overdraft in self.overdrafts:
                if overdraft.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __get_overdraft(self, account_number: str, pin: int):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number and overdraft.account.pin == pin:
                if overdraft.overdraft_status == 'active':
                    return overdraft
        return False

    def __refresh_file(self):
        self.file = open("Overdraft.txt", "w")
        for overdraft in self.overdrafts:
            self.file.write(str(overdraft))
            self.file.write("\n")
        self.file.flush()

    def __is_overdraft_not_active(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.overdraft_status == 'active':
                    return overdraft
        return False

    def __show_overdraft_balance(self, overdraft: Overdraft):
        print('Your overdraft balance is: ', overdraft.balance)

    def __show(self, overdraft: Overdraft):
        print(
            overdraft.id, '.', ' ', overdraft.account.account_number, ' ', overdraft.account.account_holder.first_name,
            " ", overdraft.amount,
            ' ', '\t', overdraft.balance, )

    def __is_account_active(self, account: Account):
        if account.account_status == 'inactive':
            return False
        else:
            return True
