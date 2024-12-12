#!/usr/bin/python3

"""

some messing around about sftp connection with password using python library paramiko

use exemple :

	python3 sftp.py [host] [username] [password] [folder path]

"""

import gnupg


gpg = gnupg.GPG()

file_to_encrypt = "sftp_file.txt"
encrypted_file = "sftp_file.txt.gpg"

public_key = ""

with open("public_key.txt", 'r') as f:
	for l in f:
		public_key += l

with open(file_to_encrypt, "rb") as f:
    status = gpg.encrypt_file(f, recipients=["hocine.meraouna@gmail.com"], output=encrypted_file)
