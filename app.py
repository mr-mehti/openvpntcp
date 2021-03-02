from flask import Flask
from flask import Response
import subprocess
import sys
app = Flask(__name__)
@app.route('/bye/<request>')
def handle(request):
    name = request
    print("Disconnect:"+name)
    if name!="0":
        subprocess.Popen(['bash','/root/wire/scripts/delete_peer.sh',name])
    return "Good bye."
@app.route('/get/stats')
def getStats():
    data=subprocess.check_output(['bash','-c', 'bash ./scripts/peers_count.sh ']).decode(sys.stdout.encoding)
    return data
@app.route('/status/<request>')
def getServerStatus(request):
    data=subprocess.check_output(['bash','-c', 'bash ./status.sh ']).decode(sys.stdout.encoding)
    count=250-data.count("cdsclient")
    return str(count)
@app.route('/add/<request>')
def add(request):
    text=subprocess.check_output(['bash','-c', 'cat /root/cdsclient.ovpn']).decode(sys.stdout.encoding)
    print("Client connected!")
    config_file = open("/root/cdsclient.ovpn","r")
    config=config_file.read()
    return Response(config)
app.run(host='0.0.0.0')