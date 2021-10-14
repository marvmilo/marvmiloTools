import marvmiloTools as mmt

#init cloudMQTT client
cloudmqtt = mmt.CloudMQTT(
    client_name = "clientname", 
    channel = "demo", 
    qos = 0
)

#connect to server
cloudmqtt.connect(
    user = "fojodopd", 
    pw = "pUZEtTZi32BU", 
    addr = "hairdresser.cloudmqtt.com", 
    port = 15604
)

cloudmqtt.reconnect()