#!/usr/bin/python
import paramiko
import shutil
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='35.86.109.36',username='ec2-user',password='admin',port=22)
sftp_client=ssh.open_sftp()

sftp_client.put("test.txt",'/home/ec2-user/test.yaml')
sftp_client.close()
ssh.close()

source_dir = r"E:\demos\files\reports"
destination_dir = r"E:\demos\files\account"
shutil.copytree(source_dir, destination_dir)
