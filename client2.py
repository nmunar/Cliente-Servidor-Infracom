# Import socket module 
import socket 

import hashlib

 
size = int(float(3.1*(10**8))) 

def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
    # Define the port on which you want to connect 
    port = 55000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server 
    message = "prueba"
    while True: 
  
        # message sent to server 
        s.send(message.encode('utf-8')) 
  
        # message received from server 
        data = s.recv(size) 
        hashh = s.recv(size)
        print("Hash recibido: " + hashh.decode("utf-8"))
        arch = data.decode('ANSI')
        # print the received message 
        # here it would be a reverse of sent message 
        print('Received file from the server :')#,str(data.decode('ANSI'))) 
        m = hashlib.sha256()
        m.update(arch.encode('ANSI'))
        h = str(m.hexdigest())
        print("Digest calculado: ", m.hexdigest())
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 