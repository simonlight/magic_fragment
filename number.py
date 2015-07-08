import requests
import urllib
import smtplib
import time
def send_email(msg):
    try:
        sender = 'simonlight9000@gmail.com'
        receivers  = 'simonlight90@gmail.com'
        message = msg
        # Credentials (if needed)
        username = 'simonlight9000'
        password = '19900401wc'
        # The actual mail send
        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        smtpObj.starttls()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"

headers = {
'Demande':'POST /coupfil/booking/create/427/0 HTTP/1.1',
'Host': 'www.rdvusagers.essonne.gouv.fr',
'Connection': 'keep-alive',
'Content-Length': '65',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Origin': 'http://www.rdvusagers.essonne.gouv.fr',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'http://www.rdvusagers.essonne.gouv.fr/coupfil/booking/create/427/0',
'Accept-Encoding': 'gzip,deflate',
'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4,zh;q=0.2',
}

cookies = dict(xtvrn='$481982$',xtan481982='-',xtant481982='1',eZSESSID='7hg39q6809lm4dd9crnspt9qf5')

data ={
'condition':'on',
'nextButton':'Effectuer+une+demande+de+r%C3%A9servation'}

data = urllib.urlencode(data)
url = 'http://www.rdvusagers.essonne.gouv.fr/coupfil/booking/create/427/0'
obj_url = 'http://www.rdvusagers.essonne.gouv.fr/coupfil/booking/create/427/2'
validate_string = "Il n'existe plus de plage horaire libre pour votre demande de"
req_std = requests.post(url=url, data=data, headers=headers, cookies=cookies)
c = 0
while True:
    c += 1
    print c
    try:
        req = requests.post(url=url, data=data, headers=headers, cookies=cookies)
        print req.url
    except requests.exceptions.RequestException:
        send_email("""request exception, maybe blocked, maybe maintenance. check it.
        http://www.rdvusagers.essonne.gouv.fr/coupfil/booking/create/427/0""")
    if req.url != obj_url:
        send_email("""object url is not .../2, check it
        http://www.rdvusagers.essonne.gouv.fr/coupfil/booking/create/427/0""")
    if req_std.content != req.content:
        send_email("""have new place for titre de sejour,
        http://www.rdvusagers.essonne.gouv.fr/coupfil/booking/create/427/0""")
    time.sleep(5)
