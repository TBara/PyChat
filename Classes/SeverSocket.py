# References:
# https://realpython.com/python-sockets/#echo-client
# https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
# https://realpython.com/python-sockets/#echo-server

import socket
BUFFER = 2048

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
    def http_server(self, data, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)

        cnt = 1
        while True:
            
            conn, _ = self.sock.accept()
            try:
                
                req = conn.recv(BUFFER)   
                print('Received: ', req)
                
                print("\nSending>>>>>>>>>>>>>>")
                data = b"Server replies Hello World!"
                conn.sendall(data + "_" + str(cnt))
                print(data.decode())
                print("<<<<<<<<<<<<<<<<")
                
                conn.close()
                cnt += 1
            except socket.error as e:
                print("Socket error: %s", e)
                break
        return