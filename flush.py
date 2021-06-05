
# Ref: https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer#Python
def flush_input():
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