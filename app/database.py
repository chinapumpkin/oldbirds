__author__ = 'dengcanrong'
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# if you don't understand this file . You can read http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
# the offical document about the  sqlalchemy part
engine = create_engine('sqlite://///Users/dengcanrong/PycharmProjects/oldbirds/oldbirds.db', convert_unicode=True, echo=True)
#if it is in the windows environment 'sqlite:///C:\\path\\to\\oldbirds.db'
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.drop_all(bind=engine)
    import app.model
    Base.metadata.create_all(bind=engine)
    pass
