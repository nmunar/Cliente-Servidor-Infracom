# Import socket module 
import socket 

import hashlib
from time import time
from pathlib import Path

 
import os, platform, logging

if platform.platform().startswith('Cliente-Servidor-Infracom'):
    fichero_log = os.path.join('archivoCliente.log')
else:
    fichero_log = os.path.join('archivoCliente.log')

print('Archivo Log en ', fichero_log)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename=fichero_log,
                    filemode='a', ) 


size = int(float(3.1*(10**8))) 

def Main():

    # local host IP '127.0.0.1', cloud: '3.88.163.203'
    host = '127.0.0.1'
    # Define the port on which you want to connect 
    port = 55000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server 
    message = "Preparado"
    while True: 
  
        # message sent to server 
        tiempo_inicial = time()
        s.send(message.encode('utf-8')) 
        print("Cliente "+ message)


        resp = s.recv(1024).decode("utf-8")
        print("video: " + resp)
        video = resp
  
        # message received from server 
        data = s.recv(size) 
        hashh = s.recv(size)
        logging.info("Recibio datos: video "+resp+ " de tamano " + str(round(Path(video).stat().st_size/(1024*1024), 2))+" MB")
        logging.info("Recibio su hash: "+ str(hashh.decode('utf-8')) )
        print("Hash recibido: " + str(hashh.decode('utf-8')))
        arch = data

        # print the received message 
        # here it would be a reverse of sent message 
        print('Received file from the server :'+ resp + "de tamaño" + str(round(Path(video).stat().st_size/(1024*1024), 2))+" MB")#,str(data.decode('ANSI'))) 
        m = hashlib.sha256()
        m.update(arch)
        h = str(m.hexdigest())
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        logging.info("Tiempo que se tardo en enviar los archivos: "+ str(round(tiempo_ejecucion, 2))+ " ms")
        
        print("tiempo de operación: "+ str(tiempo_ejecucion))
        print("Digest calculado: ", m.hexdigest())
        # ask the client whether he wants to continue 

        break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 