class User:
    def __init__(self, _id, username, password): #id is a reserved keyword so we use _id
        self.id=_id
        self.username=username
        self.password=password