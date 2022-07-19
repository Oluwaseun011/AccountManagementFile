class Manager:
    def __init__(self, email: str, password: str, id=1, first_name="", last_name="", phone_number=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.id}\t{self.first_name}\t{self.last_name}\t{self.email}\t{self.password}\t{self.phone_number}"

    def parse(line: str):
        id, first_name, last_name, email, phone_number, password = line.split('\t')
        id = int(id)
        return Manager(id=id, email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)

