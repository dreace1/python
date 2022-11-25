class db_mock:
    def __init__(self) -> None:
        self.create_db_mock()
        self.db_name = ""

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

    def get_db(self):
        return self.db

    def get_db_name(self) -> str:
        return self.db_name