
import manager_controller as controller
import manager_ui as ui
from db_mock import db_mock


class Passwordmanager:

    def __init__(self) -> None:
        self.input = 0
        self.db_mock = db_mock()

    def read_input(self):
        return int(input("Was möchtest du machen? "))

    def read_db_name(self):
        return str(input("Bitte einen Namen für die Datenbank ein ")) + ".json"
     
    def use_existing_db(self):        
        pass

    def get_action(self):
        return self.action   

    def set_action(self, action):
        self.action = action

    def start(self):
        while True:
            ui.show_menu()
            self.action = self.read_input()
            controller.choose_operation(self)

passwordmanager = Passwordmanager()
passwordmanager.start()
