import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/angelgm/Angel/Servicios en Red/ADSR/6-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/angelgm/Angel/Servicios en Red/ADSR/6-AdministraciónDeRendimiento/IMG/'
fname = 'monitoreo.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "angel_cruzazul11@hotmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imgpath+'cpuload.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    fp = open(imgpath + 'ramusage.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()
