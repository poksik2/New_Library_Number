# New Project
from massage_contact import MassageContacts
from add_contact import AddContact

class MainContacts:

    def __init__(self):
        print(MassageContacts.hellomassage)
        self.add_contact = AddContact()


    def initial_steps(self):
        pass


start = MainContacts()
