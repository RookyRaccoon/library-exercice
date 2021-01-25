from db import db


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    location = db.Column(db.String(80))
    available = db.Column(db.Boolean,default = True)
 
    reservations_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))
    reservations = db.relationship('ReservationsModel')

    def __init__(self, title: str, author:str, location:str, available: bool):
        self.name = name
        self.author = author
        self.location = location
        self.available = available

    def json(self):
        return {'tile': self.title, 'author': self.author, 'location': self.location, 'available': self.available}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    @classmethod
    def find_by_author(cls, author):
        return cls.query.filter_by(author=author).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()