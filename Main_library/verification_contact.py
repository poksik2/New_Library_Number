import sqlite3 as sql
from massage_contact import MassageContacts


class VerificationNumber:
    def __init__(self):
        self.base =[]

    def verify_num(self,number):
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM 'base_for_phonebook' WHERE (phone_number = ('{number}'))")
        self.base = cur.fetchall()
        return self.result_verify_num()

    def result_verify_num(self):
        if len(self.base) > 0:
            print(MassageContacts.number_matches)
            print(str(self.base))
            return False
        else:
            return True

class VerificationNameSurname:

        def __init__(self):
            self.base = []

        def verify(self,name,surname):

            con = sql.connect('database.db')
            cur = con.cursor()
            cur.execute(f"SELECT * FROM 'base_for_phonebook' WHERE ((name = '{name}') AND (surname = '{surname}'))")
            self.base = cur.fetchall()
            return self.result_verify()

        def result_verify(self):
            if len(self.base) > 0:
                print(MassageContacts.name_matches)
                print(str(self.base))
                return False
            else:
                return True


