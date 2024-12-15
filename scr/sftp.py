#!/usr/bin/python3

"""

some messing around about sftp connection with password using python library paramiko

use exemple :

	python3 sftp.py [host] [port] [username] [password] [folder path]

"""

import paramiko
import argparse
import telnetlib


def telnet_test(host, port):
	"""
	function for a telnet test
	"""

	try:
		test = telnetlib.Telnet(host,port)
		return True
	except:
		return False


def sftp_connection(host, username, password, folder):
	"""
	function used for the connection to the SFTP account and to list the files
	using paramiko library to do so
	"""

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	ssh.connect(host, username=username, password=password,allow_agent=False,look_for_keys=False)

	return ssh


def sftp_previous_files(ssh, folder):
	"""
	function used to check for new files
	"""

	sftp = ssh.open_sftp()

	t = sftp.listdir_attr(folder)

	for i in t:
		print(str(i))

	ssh.close()


def pull_file(ssh, folder):
	"""
	"""

	sftp = ssh.open_sftp()

	files_to_pull = []

	for f in sftp.listdir(folder):
		if '.' in f:
			files_to_pull.append(f)

	for f in files_to_pull:
		sftp.get(folder+"/"+f,"../"+f)

	ssh.close()


def push_file(ssh, folder, file_to_push):
	"""
	"""

	sftp = ssh.open_sftp()

	sftp.put(file_to_push,"test/incoming/"+file_to_push.split('.')[-2]+"v5.txt")

	ssh.close()


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("host", help="the SFTP server hostname of IP address", type=str)

    PARSER.add_argument("port", help="port number of the server", type=str)

    PARSER.add_argument("username", help="the username/login",  type=str)

    PARSER.add_argument("password", help="the password for the authentication", type=str)

    PARSER.add_argument("folder_path", help="the folder in the SFTP server that will be used for the listdir in this test", type=str)

    ARGS = PARSER.parse_args()

    HOST = ARGS.host

    PORT = ARGS.port

    USERNAME = ARGS.username

    PASSWORD = ARGS.password

    FOLDER = ARGS.folder_path

    if telnet_test(HOST, PORT):

    	print("Telnet test successful")

    	pull_file(sftp_connection(HOST, USERNAME, PASSWORD, FOLDER), FOLDER)

    	push_file(sftp_connection(HOST, USERNAME, PASSWORD, FOLDER), FOLDER, "../topush.txt")

    	sftp_previous_files(sftp_connection(HOST, USERNAME, PASSWORD, FOLDER), "test/incoming/")

    else:
    	print("failed telnet test")
