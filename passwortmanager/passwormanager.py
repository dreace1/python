class Passwortmanager:

    def __init__(self) -> None:
        pass

    def zeige_menu(self):
        print("===================================================")
        print("                  Passwortmanager")
        print("===================================================")
        print("  1) Erstelle ein neues Passwort in der Datenbank")
        print("  2) Starte mit vorhandener Datenbank")
        print("  3) Abbrechen")
    
    def lese_eingabe(self):
        return input("Was möchtest du machen? ")

    
    
passwortmanager = Passwortmanager()
passwortmanager.zeige_menu()
passwortmanager.lese_eingabe()