from flask import Flask
from flask import Response
from flask import request
import subprocess
import sys
app = Flask(__name__)
max_user=150
@app.route('/get/count')
def getStats():
    data=subprocess.check_output(['bash','-c', 'bash ./status.sh ']).decode(sys.stdout.encoding)
    count=data.count("cdsclient")
    return count
@app.route('/status/<user>')
def getServerStatus(user):
    data=subprocess.check_output(['bash','-c', 'bash ./status.sh ']).decode(sys.stdout.encoding)
    count=data.count(user)
    if count>max_user:
        return "FULL"
    return str(count)
@app.route('/gtc/<user>/get_connection')
def get_connection(user):
    print("Client connected!")
    if request.headers.get('User-Agent')!="cyberster":
        return
    data=subprocess.check_output(['bash','-c', 'bash ./status.sh ']).decode(sys.stdout.encoding)
    count=data.count(user)
    if count>max_user:
        return "FULL"
    try:
        config_file = open("/root/"+user+".ovpn","r")
        config=config_file.read()
        x =  '{ "username":"'+user+'", "password":"", "connection":"'+config+'"}'
        return Response(x)
    except:
        print("ERROR FILE NOT FOUND")
        return 0
app.run(host='0.0.0.0')