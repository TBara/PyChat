from Classes.SeverSocket import ServerSocket as sock

HOST = 'localhost'
PORT = 11234

# Initiates and starts an HTTP server from StreamSocket class
# Sends specified data when requested
def start_server():
    data = b"Server replies Hello World!"

    s = sock()
    s.http_server(data, HOST, PORT)

start_server()