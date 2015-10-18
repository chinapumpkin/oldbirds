from app.database import init_db
from app import app
__author__ = 'dengcanrong'
# this correct don't need change
# if you need to change the databases, delete the comment before init_db()
#init_db();# drop all the exist table and create new table

import socket, select, Queue

from flask import Flask







###############################
app.debug = True
app.run('0.0.0.0', 8080)