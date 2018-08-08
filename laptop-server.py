import socket
import threading
host = ''
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Waiting for Connection")
s.listen(1)
def waitconn():
        conn,addr = s.accept()
        print("Connected by", addr)
        name = str(threading.current_thread().name)+".txt"
        f = open(name,"w")
         while 1:
                data = conn.recv(1024)
                print(data.decode('utf-8'))
                f.write(data.decode('utf'))
 
t1 = threading.Thread(target = waitconn,name="thread1")
t1.start()
t2 = threading.Thread(target = waitconn,name="thread2")
t2.start()
t3 = threading.Thread(target = waitconn,name="thread3")
t3.start()
t1.join()
t2.join()
t3.join()