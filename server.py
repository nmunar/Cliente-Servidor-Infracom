# import socket programming library
import socket
import hashlib


# import thread module
from _thread import *
import threading

print_lock = threading.Lock()


# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)

        data = open("./video.mp4", "rb")#, encoding="dbcs")
        arch = data.read()
        if not data:
            print('File not found')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        #data = data[::-1]
        print("Envio de informacion")
        m = hashlib.sha256()
        m.update(arch)#.encode('dbcs'))
        h = str(m.hexdigest())
        print("Digest enviado: ", m.hexdigest())
        # send back reversed string to client
        c.send(arch)#.encode('dbcs'))
        c.send(m.hexdigest().encode("utf-8"))

        # lock released on exit
        print_lock.release()
        break

    # connection closed
    c.close()


def Main():
    host = socket.gethostname()

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
