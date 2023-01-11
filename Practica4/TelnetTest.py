import telnetlib
import getpass


HOST = "localhost"
user = input("USERNAME: ")
password = getpass.getpass()

tn = telnetlib.Telnet()
tn.open(HOST)

tn.read_until(b"login: ")
tn.write(user.encode("ascii")+b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode("ascii")+b"\n")
tn.write(b"exit\n")
print(tn.read_all())
tn.close()
