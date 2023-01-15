from ftplib import FTP
import telnetlib

HOST = "192.168.1.1"
HOST2 = "192.168.1.2"
user = "rcp"
password = "rcp"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"enable")
tn.write(b"configure")
tn.write(b"hostname Router1ADSR")
tn.write(b"copy run start")
# tn.write(b"exit\n")
tn.close()

ftp = FTP(HOST)
ftp.login(user=user, passwd=password)
with open('startup-config', 'wb') as fp:
    ftp.retrbinary('RETR startup-config', fp.write)
ftp.quit()

ftp = FTP(HOST2)
ftp.login(user=user, passwd=password)
ftp.storbinary('STOR startup-config', open('startup-config', 'rb'))
print("Uploaded!")
ftp.quit()
