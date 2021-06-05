# References:
# https://realpython.com/python-sockets/#echo-client
# https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
# https://realpython.com/python-sockets/#echo-server

import sys
import socket
from time import sleep
from .common import flush_input as flush

BUFFER = 2048
TERMINATE = "/q"


# Simple HTTP client and server class
class ServerSocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )
            # Prevent [Errno 98] Address already in use
            self.sock.setsockopt(socket.SOL_SOCKET, \
                socket.SO_REUSEADDR, 1)
        else:
            self.sock = sock


    # Start a simple server by binding and listening
    # to provided host and port. 
    def http_server(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)

        while True:       
            conn, _ = self.sock.accept()
            try:
                msg = conn.recv(BUFFER)   
                print(str(msg.decode()))
                flush()
                
                if msg.decode() == TERMINATE:
                    conn.sendall(b'')
                    flush()
                    conn.close()
                else:
                    resp = input("Reply:")
                    conn.sendall(resp.encode())
                    flush()
                    conn.close()
                    if resp == TERMINATE:
                        break
            except socket.error as e:
                print("Socket error: %s", e)
                conn.close()
                break


        self.sock.close()
        return