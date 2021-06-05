from Classes.ClientSocket import ClientSocket as sock
from time import sleep


HOST = 'localhost'
PORT = 11234

# Starts a connection and makes an HTTP requests
# Receives and prints the responsse data.
def send_client_request(host, port):
    while True:
        s = sock()
        if s.start_connection(HOST, PORT):
            data = s.http_client()
            print(data.decode())
            s.close_connection()

            if str(data.decode()) == "/q":
                break
        else:
            print("No connection created.")

send_client_request(HOST, PORT)

