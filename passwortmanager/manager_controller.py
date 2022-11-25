import json
import manager_ui as ui



def choose_operation(passwordmanager):
        match passwordmanager.get_action():
            case 1:
                create_new_db(passwordmanager)
                ui.show_new_db_menu()
            case 2:
                pass
                #use_existing_db(Passwordmanager)
            case 3:
                exit()

def create_new_db(Passwordmanager):
        pw_db = json.dumps(Passwordmanager.db_mock.get_db(), indent=4)
    
        with open("pw_mock.json", "w") as outfile:
            outfile.write(pw_db)