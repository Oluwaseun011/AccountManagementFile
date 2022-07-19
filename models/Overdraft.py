import datetime

from models.Account import Account


class Overdraft:

    def __init__(self, account: Account, id=0, amount="", balance="", overdraft_status="inactive", date=datetime.date.today()):
        self.id = id
        self.account = account
        self.amount = amount
        self.balance = balance
        self.overdraft_status = overdraft_status
        self.date = date

    def __str__(self):
        return f"{self.id}\t{self.account.account_number}\t{self.amount}\t{self.balance}\t{self.overdraft_status}\t{self.date}"

    def parse(line: str):
        id, account, amount, balance, overdraft_status, date = line.split('\t')
        id = int(id)
        return Overdraft(id=id, account=account.account_number, amount=amount,
                       balance=balance, overdraft_status=overdraft_status, date=date)