
import paramiko
import os

host = 'eu-central-1.sftpcloud.io'
user = '4da0c1944ee0490f88543ccb3ade88e3'
pswd = 'DCm5xIRVuxFL6us2XeXf6lLBT54Bcu7N'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, username=user, password=pswd,allow_agent=False,look_for_keys=False)


sftp = ssh.open_sftp()
print(sftp.listdir('outgoing'))


t = sftp.listdir_attr('outgoing')

a = str(t[0])

print(' '.join(a.split()[-4:]))

ssh.close()
