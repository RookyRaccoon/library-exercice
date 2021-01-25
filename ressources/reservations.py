from flask_restful import Resource
from flask_jwt import jwt_required
from models.reservations import ReservationsModel


class Reservations(Resource):

    @jwt_required
    def get(self, name):
        reservation = ReservationsModel.find_by_name(name)
        if reservation:
            return reservation.json()
        return {'message': 'reservation not found'}, 404

    @jwt_required
    def post(self, name):
        if ReservationsModel.find_by_name(name):
            return {'message': "A reservation with name '{}' already exists.".format(name)}, 400

        reservation = ReservationsModel(name)
        try:
            reservation.save_to_db()
        except:
            return {"message": "An error occurred creating the reservation."}, 500

        return reservation.json(), 201

    @jwt_required
    def delete(self, name):
        reservation = ReservationsModel.find_by_name(name)
        if reservation:
            reservation.delete_from_db()

        return {'message': 'reservation deleted'}


class ReservationList(Resource):
    def get(self):
        return {'reservations': list(map(lambda x: x.json(), ReservationsModel.query.all()))}