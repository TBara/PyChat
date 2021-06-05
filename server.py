import socket

HOST = 'localhost'  
PORT = 11236
TERMINATE = '/q'
BUFFER = 2048      

# Ref: https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer#Python
def flush():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        termios.tcflush(sys.stdout, termios.TCIOFLUSH)

def main():
    shutdown = False

    # Ref: https://realpython.com/python-sockets/
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        while not shutdown:
            conn, _ = s.accept()
            with conn:
                while True:
                    try: 
                        flush()
                        # Receive client'smessage
                        data = conn.recv(BUFFER)

                        # Respond to term message
                        if data.decode() == TERMINATE:
                            conn.sendall(b'')
                            flush()
                            break

                        print(data.decode())
                        flush()

                    except socket.error as e:
                        print("Socket error: %s", e)
                    
                    # Send reply to client
                    flush()
                    resp = input("Reply:")
                    flush()
                    try:
                        conn.sendall(resp.encode())
                    
                        if resp == TERMINATE:
                            shutdown = True
                            break
                    except socket.error as e:
                        print("Socket error: %s", e)

                print("Connection closed.")   
                conn.close()
                flush()

        print("Server shutdown")


if __name__ == '__main__':
    main()