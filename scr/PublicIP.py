#!/usr/bin/python3

"""

a script to get your public IP addresses (IPv4)

use exemple :

	python3 PublicIP.py

"""

import requests

def get_ip():
	"""
	function to return the public IP addresses
	"""
	return requests.get('https://api.ipify.org').content.decode('utf8')

if __name__ == '__main__':

    print(get_ip())
