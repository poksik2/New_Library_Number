# New Project
import sqlite3 as sql
from massage_contact import MassageContacts
from add_contact import AddContact
from delete_contact import DeleteContact
from data_store import DataStoreContact


class MainContacts:

    def __init__(self):
        print(MassageContacts.hellomassage)
        self.add_contact = AddContact()
        self.delete_contact = DeleteContact()
        self.read_contact = DataStoreContact()


    def initial_steps(self):

        while True:
            choice = input('1- Посмотреть, 2- Добавить, 3- Удалить: ')
            if choice == '1':
                self.read_contact.read_from_base()
            elif choice == '2':
                self.add_contact.add_to_data()
            elif choice == '3':
                self.delete_contact.delete_contact()
            else:
                print('Стоп!')
                exit()


start = MainContacts()
start = start.initial_steps()
