from Classes.ClientSocket import ClientSocket as sock

HOST = 'localhost'
PORT = 11234
MESSAGE = b"Client says Hello!"

# Starts a connection and makes an HTTP requests
# Receives and prints the responsse data.
def send_client_request(host, port, msg):
    s = sock()
    if s.start_connection(HOST, PORT):
        data = s.http_client(msg)
        print(data.decode())
        s.close_connection()
    else:
        print("No connection created.")

send_client_request(HOST, PORT, MESSAGE)

