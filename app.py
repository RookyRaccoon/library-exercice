from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt import JWT
from ressources.user import UserRegister
from ressources.books import Book,BookList
from ressources.reservations import Reservations,ReservationList
from db import db
from authentication import identity, authenticate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key('elodieexcercice')
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

 # /auth
jwt = JWT(app, authenticate, identity) 


api.add_resource(Reservations, '/reservation/<string:name>')
api.add_resource(ReservationList, '/reservations')
api.add_resource(Book, '/book/<string:title>')
api.add_resource(BookList, '/books')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)