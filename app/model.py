from sqlalchemy import Column, Integer, String
from database import Base


# SQLAlchemy is sensitive to Capital character ,so everything variable is lower case
# SQLAlchemy created database
class User(Base):
    __tablename__ = "user"
    id = Column('id', Integer, primary_key=True)
    # SQLAlchemy will automatic set which is PK but not FK as autoincrement
    name = Column('name', String, unique=True)#may be name don't need to be unique
    passwd = Column('passwd', String)
    gps_latitude = Column('latitude', String)
    gps_longitude = Column('longitude', String)
    gps_heading = Column('heading', String)
    caregiver_id = Column('caregiverid', Integer)
    registration_token=Column('token',String) # from Google Cloud Message
    sip_address = Column('sip_address', String)  # User Linephone account

    def __init__(self, name, passwd, caregiver_id,registration_token, sip_address):
        self.name = name
        self.passwd = passwd
        self.caregiver_id = caregiver_id
        self.registration_token=registration_token
        self.sip_address = sip_address
        self.gps_heading='0'
        self.gps_longitude='0'
        self.gps_latitude='0'

    def __repr__(self):
        return 'name: %s  pwd: %s' % (self.name, self.passwd)

    ##The Flask-Login extension expects certain methods to be implemented in our User class.
    #  Outside of these methods there are no requirements for how the class has to be implemented.

    def get_id(self):
        print "Get ID"
        return unicode(self.id)

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


# Flask-Login extension
pass


class Caregiver(Base):
    __tablename__ = "caregiver"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
    pwd = Column('passwd', String)
    sip_address = Column('SIP', String)

    def __init__(self, name, pwd, sip_address):
        self.name = name
        self.pwd = pwd
        self.sip_address = sip_address

    ##The Flask-Login extension expects certain methods to be implemented in our User class.
    #  Outside of these methods there are no requirements for how the class has to be implemented.
    def get_id(self):
        print "Get ID"
        return unicode(self.id)

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

##Flask-Login extension
pass
