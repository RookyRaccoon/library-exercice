from db import db

ACCESS = {
    'user' : 0,
    'employee' : 1
}

class UserModel(db.Model):
    """
    Simple class modeling a user of the library website

    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    access = db.Column(db.Iteger)


    def __init__(self, username:str, password:str,access:int):
        self.username = username
        self.password = password
        self.access = access

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def is_employee(self)-> bool:
        return self.access == ACCESS['employee']

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    