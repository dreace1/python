import json

class Passwordmanager:

    def __init__(self) -> None:
        self.input = 0

    def show_menu(self):
        print("===================================================")
        print("                  Passwortmanager")
        print("===================================================")
        print("  1) Erstelle ein neues Passwort in der Datenbank")
        print("  2) Starte mit vorhandener Datenbank")
        print("  3) Abbrechen")
    
    def read_input(self):
        return int(input("Was möchtest du machen? "))

    def choose_operation(self):
        match self.action:
            case 1:
                self.create_new_db()
            case 2:
                self.use_existing_db()
            case 3:
                exit()
    
    def db_mock(self):
        return [
            {
            "name": "leon",
            "passwort": "leon123!",
            "url": "leon@leon.de",
            "note": "leon123"
            },
            {
            "name": "hannes",
            "passwort": "hannes123!",
            "url": "hannes@hannes.de",
            "note": "hannes"  
            }
        ]

    def create_new_db(self):
        pw_db = json.dumps(self.db_mock(), indent=4)
    
        with open("pw_mock.json", "w") as outfile:
            outfile.write(pw_db)
            
    def use_existing_db(self):        
        pass        

    def start(self):
        while True:
            self.show_menu()
            self.action = self.read_input()
            self.choose_operation()

passwordmanager = Passwordmanager()
passwordmanager.start()
