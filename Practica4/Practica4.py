from ftplib import FTP
import telnetlib

HOST = "192.168.1.1" # Router 1
HOST2 = "192.168.1.2"# Router 2
user = "rcp"
password = "rcp"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"User: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
print("Conexion correcta!")
tn.write(b"en\n")
print("Habilitado")
tn.write(b"conf\n")
print("Listo para configurar")
tn.write(b"hostname R1\n")
print("Nombre cambiado")
tn.write(b"copy run start\n")
print("Persistencia iniciada")
tn.write(b"exit\n")
print("Conexion cerrada")
tn.close()

ftp = FTP(HOST)
ftp.login(user=user, passwd=password)
print("Conexion FTP correcta")
with open('startup-config', 'wb') as fp:
    ftp.retrbinary('RETR startup-config', fp.write)
    print("Archivo recibido")
ftp.quit()
print("Conexion FTP cerrada")
ftp = FTP(HOST2)
ftp.login(user=user, passwd=password)
print("Segunda conexion FTP correcta")
ftp.storbinary('STOR startup-config2', open('startup-config', 'rb'))
print("Archivo subido!")
ftp.quit()
print("Segunda conexion FTP cerrada")
