# import socket programming library
import socket
import hashlib


# import thread module
from time import time
from _thread import *
import threading

print_lock = threading.Lock()


# thread function
def threaded(c):
    while True:

        # data received from client
        tiempo_inicial = time()
        data = c.recv(1024)
        data = open("./video.mp4", encoding="ANSI")
        arch = data.read()
        if not data:
            print('File not found')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        #data = data[::-1]
        print("Envio de información")
        m = hashlib.sha256()
        m.update(arch.encode('ANSI'))
        h = str(m.hexdigest())
        print("Digest enviado: ", m.hexdigest())
        # send back reversed string to client
        c.sendall(arch.encode('ANSI'))
        c.sendall(m.hexdigest().encode("utf-8"))
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print("tiempo de operación: "+ tiempo_ejecucion)
        # connection closed
        c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 55000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(1)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()