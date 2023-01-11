from ftplib import FTP

ftp = FTP('files.000webhost.com')  # connect to host, default port
ftp.login(user='simaar', passwd='Angel_GM11')                     # user anonymous, passwd anonymous@
ftp.cwd('public_html/public/build/images')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents

with open('archivorecibido.txt', 'wb') as fp:
    ftp.retrbinary('RETR archivo.txt', fp.write)

file = open('archivorecibido.txt', 'w+')
contenido = file.read()
contenido += "cualquier cosa\nOtra linea\notra\nfrdthftgh"
file.write(contenido)
file.close()

ftp.storbinary('STOR archivo.txt', open('archivorecibido.txt', 'rb'))
print("Uploaded!")
ftp.quit()
