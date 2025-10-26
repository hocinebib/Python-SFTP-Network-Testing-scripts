#!/usr/bin/python3

"""

some messing around about getting IP address/DNS

use exemple :

	python3 DnsLookup.py [DNS or IP address]

"""

import argparse
import socket
import ipaddress

def dns_lookup(dns):
	"""
	function to get the IP address
	"""
	return socket.gethostbyname(dns)

def reverse_dns_lookup(ip):
	"""
	function to get the DNS
	"""
	return socket.gethostbyaddr(ip)[0]

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("host", help="the DNS/IP address for the lookup/reverse lookup", type=str)

    ARGS = PARSER.parse_args()

    HOST = ARGS.host

    try:
        ipaddress.ip_address(HOST)
        print(reverse_dns_lookup(HOST))
    except Exception as e:
    	print(dns_lookup(HOST))
