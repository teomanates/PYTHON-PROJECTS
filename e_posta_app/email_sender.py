import ssl
import smtplib
from email.mime.multipart import MIMEMultipart #Multipurpose Internet Mail Extensions
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(kullanici, sifre, alici, baslik, mesaj):
    posta = MIMEMultipart()
    posta["From"] = kullanici
    posta["To"] = alici
    posta["Subject"] = baslik

    posta.attach(MIMEText(mesaj, "plain"))

    eklenti_dosya_ismi="hatirlatma.txt"

   
    with open(eklenti_dosya_ismi, "rb") as eklenti_dosyasi:
        payload = MIMEBase("application", "octate-stream")
        payload.set_payload(eklenti_dosyasi.read())
        encoders.encode_base64(payload)
        payload.add_header("Content-Disposition", "attachment", filename=eklenti_dosya_ismi)
        posta.attach(payload)

    posta_str = posta.as_string()
    context = ssl.create_default_context()
    port = 465
    host = "smtp.gmail.com"

    eposta_sunucu=smtplib.SMTP_SSL(host=host, port=port, context=context) 
    eposta_sunucu.login(kullanici, sifre)
    eposta_sunucu.sendmail(kullanici, alici, posta_str)
