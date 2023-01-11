import getpass
import telnetlib
HOST = "192.168.1.1"
user = "rcp"
password = "rcp"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"sudo nano archivo.txt")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
