import socket

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
        sys.stdin.flush()
        sys.stdout.flush()
        sys.stderr.flush()

HOST = 'localhost'  
PORT = 11236
TERMINATE = '/q'
BUFFER = 2048  

def main():
    # Ref: https://realpython.com/python-sockets/
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

    sock.connect((HOST, PORT))

    while True:
        flush()
        msg = str(input("Msg: "))
        flush()
        sock.sendall(msg.encode())

        # Terminate if told to
        if msg == TERMINATE:
            break
        else:

            data = sock.recv(BUFFER)
            flush()
            if data.decode() == TERMINATE:
                print("Server terminated connection")
                break
            print(data.decode())
            

    sock.shutdown(0)
    sock.close()

if __name__ == '__main__':
    main()