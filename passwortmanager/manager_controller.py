import json
import manager_ui as ui



def choose_operation(passwordmanager):
        match passwordmanager.get_action():
            case 1:
                passwordmanager.set_action(passwordmanager.read_db_name())
                ui.show_new_db_menu(passwordmanager.get_action())
                create_new_db(passwordmanager)
                passwordmanager.read_input()
            case 2:
                pass
                #use_existing_db(Passwordmanager)
            case 3:
                exit()

def create_new_db(passwordmanager):
        pw_db = json.dumps(passwordmanager.db_mock.get_db(), indent=4)

        with open("passwortmanager/json/" + passwordmanager.get_action(), "w") as outfile:
            outfile.write(pw_db)
