from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Patients(Resource):
    def get(self):
        data = pd.read_csv('patient.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('patientid', required=True)
        parser.add_argument('firstname', required=True)
        parser.add_argument('lastname', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('phoneno', required=True)
        parser.add_argument('vaccinename', required=True)
        parser.add_argument('dosagegiven', required=True)
        parser.add_argument('amountpaid', required=True)
        args = parser.parse_args()

        data = pd.read_csv('patient.csv')

        new_data = pd.DataFrame({
            'patientid': [args['patientid']],
            'firstname': [args['firstname']],
            'lastname': [args['lastname']],
            'age': [args['age']],
            'phoneno': [args['phoneno']],
            'vaccinename': [args['vaccinename']],
            'dosagegiven': [args['dosagegiven']],
            'amountpaid': [args['amountpaid']]

        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('patient.csv', index=False)
        return {'data': new_data.to_dict('records')}, 201


class Vaccines(Resource):
    def get(self):
        data = pd.read_csv('vaccine.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('vaccinename', required=True)
        parser.add_argument('vaccinecompany', required=True)
        parser.add_argument('expirationdate', required=True)
        parser.add_argument('quantity', required=True)
        parser.add_argument('usage', required=True)
        parser.add_argument('cost', required=True)
        args = parser.parse_args()

        data = pd.read_csv('vaccine.csv')

        new_data = pd.DataFrame({
            'vaccinename': [args['vaccinename']],
            'vaccinecompany': [args['vaccinecompany']],
            'expirationdate': [args['expirationdate']],
            'quantity': [args['quantity']],
            'usage': [args['usage']],
            'cost': [args['cost']],

        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('vaccine.csv', index=False)
        return {'data': new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('vaccinename', required=True)
        args = parser.parse_args()

        data = pd.read_csv('vaccine.csv')

        data = data[data['vaccinename'] != args['vaccinename']]

        data.to_csv('vaccine.csv', index=False)
        return {'message': 'Record deleted successfully.'}, 200


class Users(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', required=True)
        parser.add_argument('lastname', required=True)
        parser.add_argument('username', required=True)
        parser.add_argument('emailid', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        data = pd.read_csv('user.csv')

        new_data = pd.DataFrame({
            'firstname': [args['firstname']],
            'lastname': [args['lastname']],
            'username': [args['username']],
            'emailid': [args['emailid']],
            'password': [args['password']],
        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('user.csv', index=False)
        return {'data': new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        args = parser.parse_args()

        data = pd.read_csv('user.csv')

        data = data[data['username'] != args['username']]

        data.to_csv('user.csv', index=False)
        return {'message': 'Record deleted successfully.'}, 200


# Add URL endpoints
api.add_resource(Patients, '/patient')
api.add_resource(Vaccines, '/user/vaccine')
api.add_resource(Users, '/user')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
