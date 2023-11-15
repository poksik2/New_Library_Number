from massage_contact import MassageContacts
from data_store import DataStoreContact
from verification_contact import VerificationNameSurname
from verification_contact import VerificationNumber

class AddContact:
    pass
    def __init__(self):
        self.base = DataStoreContact()
        self.vernamesurname = VerificationNameSurname()
        self.vernumber = VerificationNumber()
        self.name = ''
        self.surname = ''
        self.number = int

    def add_name_surname(self):

        while True:
            self.name = input(MassageContacts.enter_name)
            self.surname = input(MassageContacts.enter_surname)
            if self.vernamesurname.verify(self.name, self.surname):
                break


    def add_number(self):
        while True:
            self.number = input(MassageContacts.enter_number)
            if self.vernumber.verify_num(self.number):
                break


    def add_to_data(self):
        self.add_name_surname()
        self.add_number()
        self.base.add_to_base(self.name, self.surname, self.number)

start = AddContact()
start.add_to_data()