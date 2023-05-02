import sys
import sqlite3

conn = sqlite3.connect('Contact.db')
cur = conn.cursor()

def Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse):     
    Insert_clients ='''INSERT INTO Contact VALUES(?,?,?,?,?,?)'''
    inserer = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
    cur.execute(Insert_clients, inserer)
    conn.commit()
    cur.close()
    conn.close()

def list():
    cur.execute('''Select * from Contact''')
    result = cur.fetchall()
    print(result)
    conn.commit()
    cur.close()
    conn.close()

#def select_number():

#def select_name():


for arg in sys.argv:
    print(arg)
    if arg == "new":
        Nom= input('Quel est le nom de votre contact :')
        Prenom= input('Quel est le prénom de votre contact :')
        Surnom= input('Quel est le surnom de votre contact :')
        Telephone= input('Quel est le numéro de téléphone de votre contact :')
        Email= input('Quel est le mail de votre contact :')
        Adresse= input("Quel est l'adresse de votre contact :")
        Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)    
    
    if arg == "list":
        list()
        
    if arg == "search":
        print("par tel")
        exit()


#https://pythonforge.com/sqlite/
#https://waytolearnx.com/2020/06/inserer-des-donnees-dans-une-table-sqlite-avec-python.html

#if len(sys.argv) == "Test":
#    print ("Test fonctionne")
#    exit()

