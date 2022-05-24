from flask import Flask
from flask import Response
from flask import request
import subprocess
import sys
app = Flask(__name__)
max_user=1500
@app.route('/gtc/<user>/status')
def best_server_select(user):
    data=subprocess.check_output(['bash','-c', 'bash ./status.sh ']).decode(sys.stdout.encoding)
    count=data.count(user)
    return str(max_user-int(count))
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
        print("#### BAD ACCESS IP:"+request.remote_addr)
        print(request.headers.get('User-Agent'))
        print("#### -----------\n")
        return "FULL"
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
        return "error"
app.run(host='0.0.0.0',port=80)
