
import json
import manager_ui as ui
from db_mock import db_mock

class Passwordmanager:

    def __init__(self) -> None:
        self.input = 0
        self.db_mock = db_mock()

    def read_input(self):
        return int(input("Was möchtest du machen? "))
    
    
            
    def use_existing_db(self):        
        pass        

    def start(self):
        while True:
            ui.show_menu()
            self.action = self.read_input()
            self.choose_operation()

passwordmanager = Passwordmanager()
passwordmanager.start()
