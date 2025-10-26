#!/usr/bin/python3

"""

a script for counting the number of IP addresses on a subnet

use exemple :

	python3 CountSubnet.py [DNS or IP address]

"""

import argparse
import ipaddress

def count_ip(subnet):
	"""
	function to return the number of IP addresses
	"""
	return ipaddress.ip_network(subnet, strict=False).num_addresses

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("subnet", help="the subnet for which you want the number of IP addresses", type=str)

    ARGS = PARSER.parse_args()

    SUBNET = ARGS.subnet

    print(count_ip(SUBNET))
