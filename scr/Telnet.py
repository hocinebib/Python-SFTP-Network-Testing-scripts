#!/usr/bin/python3

"""

a script for doing telnet tests

use exemple :

    python3 Telnet.py address port

"""

import argparse
import socket, errno

def telnet_test(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except Exception as e:
        s.close()
        return("Error :", str(e))
    s.sendall(b'Test')
    r = s.recv(8192)
    s.close()
    return(r)

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("address", help="the server IP addresses", type=str)
    PARSER.add_argument("port", help="the port", type=int)

    ARGS = PARSER.parse_args()

    ADDRESS = ARGS.address
    PORT = ARGS.port

    print(telnet_test(ADDRESS, PORT))
