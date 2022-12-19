import json
import manager_ui as ui



def choose_operation(passwordmanager):
    match passwordmanager.get_action():
        case 1:
            db_mock = passwordmanager.db_mock
            db_mock.set_db_name(passwordmanager.read_db_name())
            ui.show_db_menu(db_mock.get_db_name())
            create_new_db(db_mock)

            read_db_menu_action(passwordmanager)
        case 2:
            passwordmanager.use_existing_db()
            ui.show_db_menu(passwordmanager.db_mock.get_db_name())

            read_db_menu_action(passwordmanager)
        case 3:
            exit()



def choose_db_option(passwordmanager):
    match passwordmanager.get_action():
        case 1:
            ui.show_existing_passwords(passwordmanager.db_mock)

            read_db_menu_action(passwordmanager)
        case 2:
            add_new_password(passwordmanager)
            add_pw_to_db(passwordmanager.db_mock, passwordmanager.db_mock.get_db())

            read_db_menu_action(passwordmanager)
        case 3:
            pass
        case 4:
            pass
        case 5:
            exit()

def add_new_password(passwordmanager):
    name = str(input("Bitte gebe einen Accountnamen an: "))
    password = str(input("Bitte gebe ein Passwort ein: "))
    url = str(input("Bitte gebe eine URL an: "))
    note = str(input("Bitte gebe eine Notiz an: "))

    password_entry ={
        "name": name,
        "passwort": password,
        "url": url,
        "note": note   
    }

    passwordmanager.db_mock.add_pw_to_db(password_entry)

def create_new_db(db_mock):
    pw_db = json.dumps(db_mock.get_db(), indent=4)
        
    with open("json/" + db_mock.get_db_name(), "x") as outfile:
        outfile.write(pw_db)

def add_pw_to_db(db_mock, password):
    dict = json.dumps(password, indent=4)

    with open("json/" + db_mock.get_db_name(), "w") as outfile:
            outfile.write(dict)

def read_db_menu_action(passwordmanager):
    ui.show_db_menu(passwordmanager.db_mock.get_db_name())
    passwordmanager.set_action(passwordmanager.read_input())
    choose_db_option(passwordmanager)



