import sys
import sqlite3
import re
format_tel = "[0][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
format_email = "^[\w\.]+@([\w-]+\.)+[\w-]{2,4}$"
conn = sqlite3.connect('Contact.db')
cur = conn.cursor()

def Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse):
    try:
        Insert_clients ='''INSERT INTO Contact VALUES(?,?,?,?,?,?)'''
        inserer = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
        cur.execute(Insert_clients, inserer)
        conn.commit()
        print("Insertion réussie")
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def list(): #Changer le style
    try:
        sql = '''Select * from Contact'''
        result = cur.execute(sql)
        result = cur.fetchall()
        print(result)
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def man():
    print("hello noobie\nPour te servir de l'application en ligne de commande")
    print('Il y a plusieurs options tel que lister tout vos contacts, ajouter des contacts ou faire des recherches')
    print('\n')
    print('Il y a des exemples ci-dessous :' )   
    print("'python3 contact.py new' permet d'ajouter un nouveau contact en renseignant les informations le concernant")
    print("'python3 contact.py list' permet d'afficher toute la base de donnée")
    print("'python3 contact.py update' permet de mettre a jour les informations d'un contact")
    print("'python3 contact.py delete' permet de supprimer un contact")
    print("'python3 contact.py search --by-phone' permet de rechercher un contact en fonction de son numéro de téléphone")
    print("'python3 contact.py search --by-name' permet de rechercher un contact en fonction de son nom de famille")
    print("'python3 contact.py search --by-email' permet de rechercher un contact en fonction de son adresse email")
    print("'python3 contact.py search --by-address' permet de rechercher un contact en fonction de son adress")
    print("'python3 contact.py search --by-nickname' permet de rechercher un contact en fonction de son surnom")
    print("'python3 contact.py search --by-firstname' permet de rechercher un contact en fonction de son prénom")
    

def search(zone, rechercher):
    try:
        if zone == "Nom":
            select = "Select * from Contact WHERE Nom LIKE ?"
        if zone == "Prénom":
            select = "Select * from Contact WHERE Prénom LIKE ?"
        if zone == "Téléphone":
            select = "Select * from Contact WHERE Téléphone LIKE ?"
        if zone == "Surnom":
            select = "Select * from Contact WHERE Surnom LIKE ?"
        if zone == "Email":
            select = "Select * from Contact WHERE Email LIKE ?"
        if zone == "Adresse":
            select = "Select * from Contact WHERE Adresse LIKE ?"
        utile = ('%'+rechercher+'%', )
        result = cur.execute(select, utile)
        result = cur.fetchall()
        print(result)
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)


def intéract():
    choix = None
    print("Bienvenue dans le mode intéractif de Pytact")
    while choix != "bye":
        print("Tapez 1 pour ajouter un contact ")
        print("Tapez 2 pour lister vos contacts ")
        print("Tapez 3 pour rechercher un ou plusieurs contacts ")
        print("Tapez 4 pour voir l'aide ")
        print("Tapez 5 pour supprimer un contact ")
        print("Tapez 6 pour modifier un contact ")
        choix = input("Que voulez vous faire ? : ")
        if choix == "1":
            Nom= input('Quel est le nom de votre contact : ')
            Prenom= input('Quel est le prénom de votre contact : ')
            Surnom= input('Quel est le surnom de votre contact : ')
            Telephone= input('Quel est le numéro de téléphone de votre contact : ')
            Email = input('Quel est le mail de votre contact : ')
            Adresse= input("Quel est l'adresse de votre contact : ")
            try: 
                Telephone_test = re.match(format_tel, Telephone)
                while Telephone_test == None:
                    print("Respecter la norme d'input : 0x-xx-xx-xx-xx")
                    Telephone = input('Quel est le numéro de téléphone de votre contact : ')
                    Telephone_test = re.match(format_tel, Telephone)
            except:
                print("")
            try: 
                Email_test = re.match(format_email, Email)
                while Email_test == None:
                    print("Respecter la norme d'input : test@test.com")
                    Telephone = input('Quel est le mail de votre contact : ')
                    Telephone_test = re.match(format_email, Email)
            except:
                print("")
            Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Insertion réussie")
            print("\n")
            print("\n")      
        if choix == "2":    
            list()   
            print("\n")
            print("\n")
        if choix == "3":
            zone = input("Quel est la zone de recherche (Nom/Prénom/Surnom/Téléphone/Email/Adresse) : ")
            rechercher = input("Quel est le texte que vous recherchez ? ")
            search(zone, rechercher) 
            print("\n")
            print("\n")
        if choix =="4":
            man()
            print("\n")
            print("\n")
        if choix =="5":
            Nom= input('Quel est le nom de votre contact a supprimer: ')
            Prenom= input('Quel est le prénom de votre contact a supprimer: ')
            Surnom= input('Quel est le surnom de votre contact a supprimer: ')
            Telephone= input('Quel est le numéro de téléphone de votre contact a supprimer: ')
            Email= input('Quel est le mail de votre contact a supprimer: ')
            Adresse= input("Quel est l'adresse de votre contact a supprimer: ")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Suppression réussie")
            print("\n")
            print("\n")
        if choix =="6":
            Loca_update = input("Quel est la colonne a modifier (Nom/Prénom/Surnom/Téléphone/Email/Adresse): ")
            New_data = input("Quel est la nouvelle donnée : ")
            Nom= input('Quel est le nom de votre a mettre a jour : :')
            Prenom= input('Quel est le prénom de votre contact a mettre a jour :')
            Surnom= input('Quel est le surnom de votre contact a mettre a jour :')
            Telephone= input('Quel est le numéro de téléphone de votre contact a mettre a jour : ')
            Email= input('Quel est le mail de votre contact a mettre a jour : ')
            Adresse= input("Quel est l'adresse de votre contact a mettre a jour : ")
            try: 
                Telephone_test = re.match(format_tel, Telephone)
                while Telephone_test == None:
                    print("Respecter la norme d'input : 0x-xx-xx-xx-xx")
                    Telephone = input('Quel est le numéro de téléphone de votre contact : ')
                    Telephone_test = re.match(format_tel, Telephone)
            except:
                print("")
            try: 
                Email_test = re.match(format_email, Email)
                while Email_test == None:
                    print("Respecter la norme d'input : test@test.com")
                    Telephone = input('Quel est le mail de votre contact : ')
                    Telephone_test = re.match(format_email, Email)
            except:
                print("")
            maj(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse)
            print("\n")
            print("\n")

def supprimer(Nom, Prenom, Surnom, Telephone, Email, Adresse):
    try:
        Delete ='''Delete from Contact where Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
        Suppr = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
        cur.execute(Delete, Suppr)
        conn.commit()  
        print("Suppression réussie")
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def maj(Loca_update,New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse):
    if Loca_update == "Nom":
        Cmd ='''UPDATE Contact SET Nom = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Prénom":
        Cmd ='''UPDATE Contact SET Prénom = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Surnom":
        Cmd ='''UPDATE Contact SET Surnom = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Téléphone":
        Cmd ='''UPDATE Contact SET Téléphone = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Email":
        Cmd ='''UPDATE Contact SET Email = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Adresse":
        Cmd ='''UPDATE Contact SET Adresse = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    try:
        Update = (New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse)
        cur.execute(Cmd, Update)
        conn.commit()  
    except sqlite3.Error as error:
        print("Petit soucis ! ", error)

for arg in sys.argv:
    try:
        if sys.argv[1] == "new" :
            Nom= input('Quel est le nom de votre contact : ')
            Prenom= input('Quel est le prénom de votre contact : ')
            Surnom= input('Quel est le surnom de votre contact :')
            Telephone= input('Quel est le numéro de téléphone de votre contact : ')
            Email= input('Quel est le mail de votre contact ')
            Adresse= input("Quel est l'adresse de votre contact ")
            try: 
                Telephone_test = re.match(format_tel, Telephone)
                while Telephone_test == None:
                    print("Respecter la norme d'input : 0x-xx-xx-xx-xx")
                    Telephone = input('Quel est le numéro de téléphone de votre contact : ')
                    Telephone_test = re.match(format_tel, Telephone)
            except:
                print("")
            try: 
                Email_test = re.match(format_email, Email)
                while Email_test == None:
                    print("Respecter la norme d'input : test@test.com")
                    Telephone = input('Quel est le mail de votre contact : ')
                    Telephone_test = re.match(format_email, Email)
            except:
                print("")
            Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            break
              

        if sys.argv[1] == "list" :
            list()
            break

        if sys.argv[1] == "?":
            man()
            break
        if sys.argv[1] == "delete":
            Nom= input('Quel est le nom de votre contact :')
            Prenom= input('Quel est le prénom de votre contact :')
            Surnom= input('Quel est le surnom de votre contact :')
            Telephone= input('Quel est le numéro de téléphone de votre contact :')
            Email= input('Quel est le mail de votre contact :')
            Adresse= input("Quel est l'adresse de votre contact :")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            break
            
        if sys.argv[1] == "update":
            Loca_update = input("Quel est la colonne a modifier (Nom/Prénom/Surnom/Téléphone/Email/Adresse): ")
            New_data = input("Quel est la nouvelle donnée : ")
            Nom= input('Quel est le nom de votre a mettre a jour : :')
            Prenom= input('Quel est le prénom de votre contact a mettre a jour :')
            Surnom= input('Quel est le surnom de votre contact a mettre a jour :')
            Telephone= input('Quel est le numéro de téléphone de votre contact a mettre a jour : ')
            Email= input('Quel est le mail de votre contact a mettre a jour : ')
            Adresse= input("Quel est l'adresse de votre contact a mettre a jour : ")
            try: 
                Telephone_test = re.match(format_tel, Telephone)
                while Telephone_test == None:
                    print("Respecter la norme d'input : 0x-xx-xx-xx-xx")
                    Telephone = input('Quel est le numéro de téléphone de votre contact : ')
                    Telephone_test = re.match(format_tel, Telephone)
            except:
                print("")
            try: 
                Email_test = re.match(format_email, Email)
                while Email_test == None:
                    print("Respecter la norme d'input : test@test.com")
                    Telephone = input('Quel est le mail de votre contact : ')
                    Telephone_test = re.match(format_email, Email)
            except:
                print("")
            maj(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse)
            break
        
        if sys.argv[1] == "search":
            rechercher = sys.argv[3]
            try:
                if sys.argv[2] == "--by-name" :
                    zone = "Nom"
                if sys.argv[2] == "--by-tel" :
                    zone = "Téléphone"
                if sys.argv[2] == "--by-email" :
                    zone = "Email"
                if sys.argv[2] == "--by-nickname" :
                    zone = "Surnom"
                if sys.argv[2] == "--by-firstname" :
                    zone = "Prénom"
                if sys.argv[2] == "--by-address" :
                    zone = "Adresse"
                search(zone, rechercher)
            except:
                    print ("Veuillez utiliser la commande 'python3 contact.py ?' ou veuillez entrer dans le mode intéractif ")
            break
    except:
            intéract()
        
   



