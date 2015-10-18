__author__ = 'dengcanrong'

from flask import request

from flask_restful import Resource

from flask import json
import requests

from app.database import db_session
from app.model import User
from app import app, api, lm

API_KEY = "AIzaSyBngz6phmJufLy-HTLH09irXLre2j7TZOo"  # Google Cloud Message
url = "https://android.googleapis.com/gcm/send"  # Google Cloud Message


# config setting

# UDP settings
UDP_IP = "0.0.0.0"
UDP_PORT = 8080


@app.before_request
def before_request():
    # init_db();
    pass


@app.teardown_request
def teardown_request(exception):
    db_session.close()
    db_session.remove()


    # User loader for log-in purposes.


@lm.user_loader
def user_loader(id):
    return User.query.get(int(id))


# parser for json.
# def parse_json():
#   return request.get_json()


# Class for getting the users from the database.[not used]
# need return   username, latitude,longitude,heading, sip_address
class Users(Resource):
    def get(self):
        # User.query.all()
        #users = db_session.query(User).all()
        users=User.query.all()
        if users is None:
            return 'database is Null'
        return u'\r '.join([u"{0}: {1}:{2}:{3}:{4}:{5}".format(user.id, user.name, user.gps_longitude, user.gps_latitude,
                                                user.gps_heading, user.registration_token) for user in users])

        pass


class Login(Resource):
    def post(self):
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        app.logger.info("user:%s passwd:%s", name, passwd)
        registered_user = User.query.filter(User.name == name,
                                            User.passwd == passwd).first()  # this sentence is correct
        if registered_user is None:
            return "error"

        return "success"
        pass


# register a new user
class Register(Resource):  # need to return something if the username exist
    def post(self):  # TCP post method
        name = request.form.get('name', 'aa', type=str)
        passwd = request.form.get('passwd', type=str)
        sip_address = request.form.get('sip', type=str)
        registration_token = request.form.get('token', type=str)
        # name, passwd, caregiver_id,registration_token,Instance_ID, sip_address
      #  app.logger.info("user:%s passwd:%s,token,%S,Instance_ID,%S,ipaddress,%s", name, passwd, registration_token,Instance_ID, sip_address)
        user = User(name, passwd, 1, 'token' , sip_address);
        db_session.add(user)
        db_session.commit()

        return 'User successfully registered'


# Get user location from the database.
class User_location(Resource):  # location need post part and get part.
    def get(self):  # TCP post method
        userid = request.args.get('userid')
        user = User.query.get(int(userid))
        location_data = {}
        location_data['latitude'] = user.gps_latitude
        location_data['longitude'] = user.gps_longitude
        location_data['heading'] = user.gps_heading
        print location_data['latitude']
        print location_data['longitude']
        envelope = {}
        envelope['location'] = location_data
        return envelope




# Includes functions to send controls to the smartglasses via udp.
# control is from the unity 3d part to android part
class Control(Resource):  # '''this part need to change to tcp connection'''
    def get(self):
        userid = request.args.get('userid')
        control = request.args.get('control', type=str)  # left,right,forward,stop
        app.logger.info("userid:%s control:%s", userid, control)
        user=User.query.get(int(userid))
        print user.registration_token
        body = {}
        body["to"] = user.registration_token  # need to edit
      #  body["notification"] = {"title": "Portugal vs. Denmark", "body": "5 to 1", "icon": "myicon"}
        body['data'] = {'message': control}

        headers = {'Content-Type': 'application/json', 'Authorization': 'key=' + API_KEY}
        print "Send data \n" + str(body)
        #r = requests.post(url, data=json.dumps(body), headers=headers)
        r = requests.post(url, data=json.dumps(body), headers=headers)
        print r.status_code
        print r.text





pass  # Add the resources.''''

api.add_resource(Register, '/oldbirds/api/register', endpoint='register')  # is ok
api.add_resource(Users, '/oldbirds/api/users/', endpoint='users')  # is ok
api.add_resource(User_location, '/oldbirds/api/user_location/', endpoint='user_location')  # get is ok need post part.
api.add_resource(Control, '/oldbirds/api/control/', endpoint='control')  # need hannu reply

