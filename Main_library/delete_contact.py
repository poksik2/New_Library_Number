from massage_contact import MassageContacts
import sqlite3 as sql
from data_store import DataStoreContact
class DeleteContact:

    def __init__(self):
        self.choice = ''
        self.data = DataStoreContact()

    def delete_contact(self):
        self.data.read_from_base()
        self.choice = input('Введите ID: ')
        can = sql.connect('database.db')
        with can:
            cur = can.cursor()
            cur.execute(f"DELETE FROM `base_for_phonebook` WHERE (id = ('{self.choice}'))")
        can.commit()



#start = DeleteContact()
#start = start.delete_contact()


