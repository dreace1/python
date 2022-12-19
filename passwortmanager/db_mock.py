class db_mock:
    def __init__(self) -> None:
        self.db = []
        self.db_name = ""

    #Testfunktion für das erstellen einer gemockten json datei
    def create_db_mock(self):
        self.db =  [
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

    def add_pw_to_db(self, password):
        self.db.append(password)

    def get_db(self):
        return self.db
    
    def set_db(self, db):
        self.db = db

    def get_db_name(self) -> str:
        return str(self.db_name)
    
    def set_db_name(self, db_name):
        self.db_name = str(db_name)

    

