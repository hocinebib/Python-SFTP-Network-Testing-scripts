#!/usr/bin/python3

"""

some messing around about pgp encryption using python library gnupg

use exemple :

	python3 pgp.py [public_key] [email] [file_to_encrypt] [passphrase]

"""

import gnupg
import argparse

def pgp_encryption(gpg, pub_key, email, filename):
	"""
	function used for the encryption of the files
	using gnupg library to do so
	"""

	with open(filename, "rb") as f:
		status = gpg.encrypt_file(f, recipients=[email], output=filename+".gpg")

def pgp_decryption(gpg, password, filename):
	"""
	function used to decrypt the files
	using gnupg library to do so
	"""

	with open(filename, "rb") as f:
		decrypted_data = gpg.decrypt_file(f, passphrase=password)
		if decrypted_data.ok:
			print("The file " + filename + " has been correctly decrypted")


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("public_key", help="the public PGP key that will have to be used to encrypt the files", type=str)

    PARSER.add_argument("email", help="the eamil address corresponding to the PGP keys that will be used",  type=str)

    PARSER.add_argument("file_to_encrypt", help="the file that entends to be PGP encrypted", type=str)

    PARSER.add_argument("passphrase", help="the passphrase of the private key used to decrypt the files", type=str)

    ARGS = PARSER.parse_args()

    PUBLIC_KEY = ARGS.public_key

    EMAIL = ARGS.email

    FILE_TO_ENCRYPT = ARGS.file_to_encrypt

    PASSPHRASE = ARGS.passphrase

    pk = ""

    with open(PUBLIC_KEY, 'r') as f:
    	for l in f:
    		pk += l

    gpg = gnupg.GPG()

    pgp_encryption(gpg, pk, EMAIL, FILE_TO_ENCRYPT)

    pgp_decryption(gpg, PASSPHRASE, FILE_TO_ENCRYPT+".gpg")

