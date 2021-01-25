from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.books import BookModel


class Book(Resource):

    #for POST
    parser = reqparse.RequestParser()
    parser.add_argument('location',
                        type=float,
                        required=True,
                        help="Location that can be set up by employee"
                        )
    parser.add_argument('reservation_id',
                        type=int,
                        required=False,
                        help="Reservation id for a book."
                        )

    @jwt_required()
    def get(self, title: str):
        book = BookModel.find_by_title(title)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    @jwt_required()
    def post(self, title: str):
        if BookModel.find_by_title(title):
            return {'message': "An book with name '{}' already exists.".format(title)}, 400

        data = Book.parser.parse_args()

        book = BookModel(title, **data)

        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred inserting the book."}, 500

        return book.json(), 201

    @jwt_required()
    def delete(self, title: str):
        book = BookModel.find_by_title(title)
        if book:
            book.delete_from_db()
            return {'message': 'book deleted.'}
        return {'message': 'book not found.'}, 404

    @jwt_required()
    def put(self, title: str):
        data = Book.parser.parse_args()

        book = BookModel.find_by_title(title)

        if book:
            book.price = data['price']
        else:
            book = BookModel(title, **data)

        book.save_to_db()

        return book.json()


class BookList(Resource):
    def get(self):
        return {'books': list(map(lambda x: x.json(), BookModel.query.all()))}