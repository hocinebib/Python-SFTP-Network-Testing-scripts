import paramiko

host = 'eu-central-1.sftpcloud.io'
user = '872d6c1f283f4eafb0693df8bbc2981e'
pswd = '1U3XzBAai36zR2up6YZX2NGzpdxHFHe8'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, username=user, password=pswd,allow_agent=False,look_for_keys=False)


sftp = ssh.open_sftp()
print(sftp.listdir('test/outgoing'))
