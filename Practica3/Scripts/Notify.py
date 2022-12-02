import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '
# Define params
rrdpath = '/home/angelgm/Angel/Servicios en Red/ADSR/Practica3/RRD/'
imgpath = '/home/angelgm/Angel/Servicios en Red/ADSR/Practica3/IMG/'
fname = 'monitoreo.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "agm110706@gmail.com"
mailcc = "agm110706@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject, img, info):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    # msg['Cc'] = mailcc
    fp = open(imgpath+img+'.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    text = MIMEText(info)
    msg.attach(text)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()
