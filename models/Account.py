from models.AccountHolder import AccountHolder


class Account:

    def __init__(self, account_holder: AccountHolder, pin: int, id=0, account_name="", account_number="",
                 account_balance=0.0,
                 account_status="active"):
        self.id = id
        self.account_holder = account_holder
        self.account_name = account_name
        self.account_number = account_number
        self.pin = pin
        self.account_balance = account_balance
        self.account_status = account_status

    def __str__(self):
        return f"{self.id}\t{self.account_name}\t{self.account_number}\t{self.pin}\t{self.account_balance}\t{self.account_status}"

    def parse(line: str):
        id, account_name, account_number, pin, account_balance, account_status = line.split('\t')
        id = int(id)
        pin = int(pin)
        account_balance = float(account_balance)
        return Account(id=id, account_holder=account_name,  account_number=account_number,
                       pin=pin, account_balance=account_balance, account_status=account_status)
