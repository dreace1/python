

def show_menu():
    print("===================================================")
    print("                  Passwortmanager")
    print("===================================================")
    print("  1) Erstelle eine Passwort Datenbank")
    print("  2) Starte mit vorhandener Datenbank")
    print("  3) Abbrechen")

def show_db_menu(db_name: str):

    print("===================================================")
    print("                  Passwortmanager (" + db_name + ")")
    print("===================================================")
    print(" 1) Zeige vorhandene Passwörter")
    print(" 2) Neues Passwort hinzufügen")
    print(" 3) Lösche vorhandenes Passwort")
    print(" 4) Passwort aktualisieren")
    print(" 5) Abbrechen")

def show_existing_passwords(db_mock):
    print("===================================================")
    print("Name           Passwort           URL           Notiz")
    print("===================================================")
    for line in db_mock.get_db():
        print("     ".join(list(line.values())))
    #TODO Formatierung des Ausgabe