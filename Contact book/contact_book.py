import os
from os import system
import sqlite3
from sqlite3 import Error

def main():
    # connection
    conn = sqlite3.connect(os.getcwd()+'\\db.sqlite3')
    curs = conn.cursor()
    # create_table
    # data types : INTEGER, REAL, TEXT, BLOB & NULL
    curs.execute("""CREATE TABLE IF NOT EXISTS contact(
        contact_id INTEGER PRIMARY KEY,
        name TEXT,
        number TEXT
        )"""
    )
    while True:
        system('cls')
        print("Vos contacts :\n", *curs.execute("SELECT * FROM contact").fetchall(), sep='\n')
        answer = input("""
-------------------------------------------------
|              GESTIONNAIRE DE CONTACT          |
-------------------------------------------------
|       Pour ajouter un contact tapper 1,       | 
|       Pour supprimer un contact tapper 2,     |
|       Pour modifier un contact tapper 3,      |
|       Pour quitter tapper entrer,             |
-------------------------------------------------
: """)
        if answer == "1":
            name = input("nom : ")
            numero = input("numero : ")
            # insert data
            curs.execute("INSERT INTO contact(name, number) VALUES('"+name+"', '"+numero+"')")
            conn.commit()
        
        elif answer == "2":
            contact_id = input("contact_id : ")
            # delete data
            curs.execute("DELETE FROM contact WHERE contact_id='"+contact_id+"'")
            conn.commit()
        
        elif answer == "3":
            contact_id = input("contact_id : ")
            name = input("nouveau nom : ")
            numero = input("nouveau numero : ")
            # update data
            curs.execute("UPDATE contact SET name='"+name+"', number='"+numero+"' WHERE contact_id='"+contact_id+"'")
            conn.commit()

        elif answer == "":
            print("Bye bye !")
            break
    
    curs.close()
    conn.close()

if __name__ == '__main__':
    main()