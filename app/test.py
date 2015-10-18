from urllib2 import urlopen
from flask import Request
import urlfetch

__author__ = 'dengcanrong'
# this file is setting for test whether the run.py is working
import requests
import json
# payload = {'key1': 'value1', 'key2': 'value2','sip': '@linphone.com'}
user_info = {'name': 'apple', 'passwd': '321'}
#r = requests.post("http://0.0.0.0:8080/oldbirds/api/register", data=user_info)#, json=payload)
# r = requests.post("http://0.0.0.0:8080/register")
# r1=requests.post("http://0.0.0.0:8080")
r=requests.get('http://0.0.0.0:8080/oldbirds/api/users/')
control_info = {'userid': '5', 'control': 'left'}
#r1 = requests.post('http://0.0.0.0:8080/oldbirds/api/login/', data=user_info)
r1 = requests.get('http://0.0.0.0:8080/oldbirds/api/control/', params=control_info)
#r=requests.get('http://0.0.0.0:8080/oldbirds/api/user_location/?userid=1')
print r1.text
print r.text
'''
import socket

UDP_IP = '0.0.0.0'
UDP_PORT = 8080
ADDRESS = (UDP_IP, UDP_PORT)
S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
S.connect(ADDRESS)

while 1:

    data={'type':'register','name':'pumpkin','passwd':'321','token':'123','longitude':'','latitude':'','heading':'','sip_address':'qqq6'}
    json_str = json.dumps(data)
    S.sendall(json_str)
    msg = S.recv(2048)
    print '%s says: %s' % (UDP_IP, msg)

    break

S.close()'''
API_KEY = "AIzaSyCMsdeyCT4CuBfLdbwdwefdHSwg3p1zUjk"  # Google Cloud Message
url = "https://android.googleapis.com/gcm/send"  # Google Cloud Message

