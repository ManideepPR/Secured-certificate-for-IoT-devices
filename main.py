
from flask import Flask, jsonify,render_template
app= Flask(__name__)

devices_db=[
    {
    'id':"001",
    'type':"Temperature Sensor",
    'organization':'abc',
    'created date':'07/12/2021',
    'trusted key':'h3hevdtrds5wevdts5'
    },
    {
    'id':"002",
    'type':"Humidity Sensor",
    'organization':'xyz',
    'created date':'12/12/2008',
    'trusted key':'bjguw62202gdsvcrxx529'
    },
    {
    'id':"003",
    'type':"Soil Moisuture Sensor",
    'organization':'rgs',
    'created date':'29/09/2017',
    'trusted key':'nshyw628762f52gf27gb'
    },
    {
    'id':"004",
    'type':"Pressure sensor",
    'organization':'hal',
    'created date':'7/8/2016',
    'trusted key':'hahebe73edeu3efe639'
    },
    {
    'id':"005",
    'type':"Infrared sensor",
    'organization':'DEF',
    'created date':'15/7/2009',
    'trusted key':'bckur7409373bhvd649493b'
    },
    {
    'id':"006",
    'type':"Optical sensor",
    'organization':'abc',
    'created date':'7/9/2004',
    'trusted key':'bchhdyc76267879-2wedchvu'
    },
    {
    'id':"007",
    'type':"Proximity sensor",
    'organization':'htahsp',
    'created date':'4/5/2007',
    'trusted key':'vdy353vgst628bxfses3'
    },
    {
    'id':"008",
    'type':"Level sensor",
    'organization':'yvsg',
    'created date':'6/4/2022',
    'trusted key':'bcgdyrbjf7743389bffg'
    },
    {
    'id':"009",
    'type':"Accelerometer",
    'organization':'hiuudge',
    'created date':'4/09/2109',
    'trusted key':'bjs6272vcvsxts4628tv'
    },
    {
    'id':"010",
    'type':"Gyroscope",
    'organization':'bshsy',
    'created date':'6/11/2007',
    'trusted key':'cxdhvv7268729vdcu82'
    },
]
@app.route("/abcd",methods=['GET'])
def welcome():
    f=open("cert.txt","r")
    return f.read()

@app.route("/getDevices",methods=['GET'])
def getDevices():
    return jsonify({"Iot Devices":devices_db})

@app.route("/getDevices/<id>",methods=['GET'])
def get_srn(id):
    device=[dev for dev in devices_db if(dev['id'])==id]
    return jsonify(device)

@app.route("/updateDevices/<id>",methods=['PUT'])
def update(id):
    device=[dev for dev in devices_db if(dev['id'])==id]
    device[0]['type']= 'Humidity Sensor'
    return jsonify({"Device":device[0]})

@app.route("/addDevices/",methods=['POST'])
def addDevice():
    device={
    'id':"011",
    'type':"Pressure sensor",
    'organization':'sbsg',
    'created date':'09/08/2008',
    'trusted key':'xbiysi36363hvdvyd6'
    },
    devices_db.append(device)
    return jsonify({"Devices":devices_db})

@app.route("/deleteDevices/<id>",methods=['DELETE'])
def deleteDevice(id):
    device=[dev for dev in devices_db if(dev['id']==id)]
    if(len(device)>0):
        devices_db.remove(device[0])
    return jsonify({"Device":device})

if __name__=="__main__":
    app.run(host='0.0.0.0')