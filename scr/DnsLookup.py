#!/usr/bin/python3

"""

some messing around about getting IP address/DNS

use exemple :

	python3 DnsLookup.py [DNS]

"""

import argparse
import socket

def dns_lookup(dns):
	"""
	function to get the IP address
	"""
	return socket.gethostbyname(dns)

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("dns", help="the DNS for which you are looking for the IP address", type=str)

    ARGS = PARSER.parse_args()

    DNS = ARGS.dns

    print(dns_lookup(DNS))
