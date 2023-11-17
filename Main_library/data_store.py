import sqlite3 as sql
#from add_contact import AddContact


class DataStoreContact:

    def __init__(self):
        #self.add_contact = AddContact()
        con = sql.connect('database.db')
        with con:
            cur = con.cursor()
            cur.execute(
            "CREATE TABLE IF NOT EXISTS `base_for_phonebook` "
            "(id INTEGER PRIMARY KEY, "
            "name STRING, "
            "surname STRING, "
            "phone_number INTEGER)")
            con.commit()


    def add_to_base(self,name,surname,number):
        con = sql.connect('database.db')
        with con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO `base_for_phonebook` (name, surname, phone_number) VALUES "
                        f"('{name}', '{surname}','{number}')")
            con.commit()

    def read_from_base(self):
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM `base_for_phonebook`")
        all_contact = (cur.fetchall())
        i = 0
        while i != len(all_contact):
            all_liner = (all_contact[i])
            i +=1
            print('-------------------------------')
            print(*all_liner)


#data_store = DataStoreContact()
#data_store.add_to_base()
#data_store.read_from_base()