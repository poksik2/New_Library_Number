import sqlite3 as sql

class Contacts:

    def __init__(self):
        self.name = input('Name: ')
        self.surname = input('Surname: ')
        self.number = input('Number: ')
        #self.contacts = (f"Name : {self.name} \nSurname : {self.surname} \nNumbers : {self.number}")


contact = Contacts()



print(contact.name)

con = sql.connect('test.db')
with con:
    cur = con.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS `test` (id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, surname STRING, phone_number INTEGER)")
    #cur.execute(f"INSERT INTO `test` (name, surname, phone_number) VALUES ('{contact.name}', '{contact.surname}','{contact.number}')")
    #con.execute("DELETE FROM 'test' WHERE id = 1")
    con.commit()

    cur.execute("SELECT * FROM 'test'")
    data = cur.fetchall()
    #print (str(data))
    cur.execute(f"SELECT * FROM 'test' WHERE ((name = 'Bob') AND (surname = 'Valter'))")
    ns = cur.fetchall()
    #print(ns)

base = []
basefull = [(2, "asd",111)]

if basefull != []:
    print("ok")
else:
    print("not")


