
import json
import manager_ui as ui
from db_mock import db_mock

class Passwordmanager:

    def __init__(self) -> None:
        self.input = 0
        self.db_mock = db_mock()

    def read_input(self):
        return int(input("Was möchtest du machen? "))

    def choose_operation(self):
        match self.action:
            case 1:
                self.create_new_db()
                ui.show_new_db_menu()
            case 2:
                self.use_existing_db()
            case 3:
                exit()
    
    def create_new_db(self):
        pw_db = json.dumps(self.db_mock.get_db(), indent=4)
    
        with open("pw_mock.json", "w") as outfile:
            outfile.write(pw_db)
            
    def use_existing_db(self):        
        pass        

    def start(self):
        while True:
            ui.show_menu()
            self.action = self.read_input()
            self.choose_operation()

passwordmanager = Passwordmanager()
passwordmanager.start()
