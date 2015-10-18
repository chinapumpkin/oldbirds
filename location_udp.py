from _ctypes import sizeof
from _socket import SO_REUSEADDR, SOL_SOCKET
import socket
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import yaml
from app import  User, db_session

app = Flask(__name__)

# Path for the database.
'''
engine = create_engine('sqlite:////tmp/oldbirds.db', convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))'''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Enable address reuse */
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('0.0.0.0', 8080))
while True:
    data, addr = sock.recvfrom(1024)
    print "received message: ", addr, data
    # Get json.
    try:
        # _private_value
        _values = yaml.safe_load(data)
        # _values = loads(data)
        print "it is JSON"
    except Exception, e:
        print "Cannot parse data. Maybe not JSON?"
        # Get gps_data
    try:
        type=_values['type']
        print type
        if type=='register':
            name = _values['name']
            print name
            passwd = _values['passwd']
            print passwd
            sip_address=_values['sip_address']
            print sip_address
            token=_values['token']
            print token
            print 'a new people want to register '
            user = User(name, passwd, 1, token , sip_address);
            db_session.add(user)
            db_session.commit()


        elif type=='location':
            latitude = _values['latitude']
            longitude = _values["longitude"]
            heading = _values["heading"]
            name = _values['name']
            passwd = _values['passwd']
            registered_user = User.query.filter(User.name == name,
                                            User.passwd == passwd).first()  # this sentence is correct
            if registered_user is None:
                print "error"
            else:
            ####################
            # Update database
                registered_user.gps_latitude = latitude
                registered_user.gps_longitude = longitude
                registered_user.gps_heading = heading
            # db_session.merge(registered_user)
                db_session.commit()
            #db_session.close()
                print "success"
        else:
            print type

            

    except Exception, e:
        print "Maybe handshake? No-action"
