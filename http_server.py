from Classes.SeverSocket import ServerSocket as sock

HOST = 'localhost'
PORT = 11234

# Initiates and starts an HTTP server from StreamSocket class
# Sends specified data when requested
def start_server():
    
    s = sock()
    s.http_server(HOST, PORT)
    print("Server is shutting down.")

start_server()