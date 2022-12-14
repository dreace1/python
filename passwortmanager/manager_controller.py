import json
import manager_ui as ui



def choose_operation(passwordmanager):
    match passwordmanager.get_action():
        case 1:
            db_mock = passwordmanager.db_mock
            db_mock.set_db_name(passwordmanager.read_db_name())
            ui.show_new_db_menu(db_mock.get_db_name())
            create_new_db(db_mock)
            passwordmanager.read_input()
            choose_db_option(passwordmanager)
        case 2:
            pass
            #use_existing_db(Passwordmanager)
        case 3:
            exit()

def choose_db_option(passwordmanager):
    match passwordmanager.get_action():
        case 1:
            print(passwordmanager.db_mock)
        case 2:
            n = 2
            d = dict(input("Gebe den Account Namen ein: ").split() for _ in range(n))
            add_pw_to_db(passwordmanager.db_mock, d)
        case 3:
            pass
        case 4:
            pass
        case 5:
            exit()


def create_new_db(db_mock):
    pw_db = json.dumps(db_mock.get_db(), indent=4)
        
    with open("json/" + db_mock.get_db_name(), "w") as outfile:
        outfile.write(pw_db)

def add_pw_to_db(db_mock, password):
    dict = json.dumps(password, indent=4)

    with open("json/" + db_mock.get_db_name(), "w") as outfile:
            outfile.write(dict)


