import socket
class PCconnection:
        def __init__(self): 
                self.host = '192.168.0.101' 
                self.port = 12345 
                self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                self.s.connect((self.host,self.port)) 
                print("Connected") 
        def send_Data(self): 
                msg = "HELLO\n"
                self.s.send(msg.encode())
myCon = PCconnection()
while 1: 
        myCon.send_Data()