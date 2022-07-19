from typing import List

from models.AccountHolder import AccountHolder


class AccountHolderManager:
    accountHolders: List[AccountHolder] = []

    file = open("AccountHolder.txt", "a+")

    def __init__(self):
        self.file.seek(0)
        for account_line in self.file:
            self.accountHolders.append(AccountHolder.parse(account_line))

    def create_account_holder(self, email: str, password: str, confirm_password: str, first_name: str, last_name: str,
                              phone_number: str):
        id = self.__get_id()
        if password == confirm_password:
            account_holder = AccountHolder(email=email, password=password, id=id, first_name=first_name,
                                           last_name=last_name, phone_number=phone_number)
            self.accountHolders.append(account_holder)
            if self.file.closed is True:
                self.file = open("AccountHolder.txt", "a+")
            else:
                self.file.write(f"{str(account_holder)}\n")
                self.file.flush()
            return account_holder
        else:
            return False

    def login_account_holder(self, email: str, password: str):
        for account_holder in self.accountHolders:
            if account_holder.email == email and account_holder.password == password:
                return account_holder
        else:
            return False

    def update_account_holder(self, email: str, first_name: str, last_name: str, phone_number: str):
        account_holder = self.__find(email=email)
        if account_holder:
            account_holder.first_name = first_name
            account_holder.last_name = last_name
            account_holder.phone_number = phone_number
            self.__refresh_file()
            return True
        else:
            return False

    def change_password(self, email: str, pin: int, new_password: str, confirm_password: str):
        account_holder = self.__find(email=email)
        if account_holder:
            account_holder.password = new_password
            if new_password == confirm_password:
                return True
        else:
            return False

    def list_account_holder(self):
        for account_holder in self.accountHolders:
            self.__show(account_holder=account_holder)

    def __show(self, account_holder: AccountHolder):
        print(
            f"{account_holder.id}\t{account_holder.first_name}\t{account_holder.last_name}\t{account_holder.email}\t{account_holder.phone_number}")

    def __refresh_file(self):
        self.file = open("AccountHolder.txt", "w")
        for account_holder in self.accountHolders:
            self.file.write(str(account_holder))

            self.file.write("\n")
        self.file.flush()

    def __find(self, email: str):
        for account_holder in self.accountHolders:
            if account_holder.email == email:
                return account_holder
        return False

    def __get_id(self):
        length = len(self.accountHolders)
        if length == 0:
            length += 1
            return length
        else:
            for account_holder in self.accountHolders:
                if account_holder.id == length or account_holder.id >= length:
                    length += 1
                    return length
                else:
                    continue
