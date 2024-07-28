from imap_tools import MailBox
from imap_tools import AND
import datetime
import os

kullanici = "<kullanici"
sifre = "<sifre>" #mail sunucusu izin vermezse eğer, google üzerinden alinan uygulama şifresi girilir.
gonderen = "<gonderen>"  # Aramak istediğiniz göndericinin e-posta adresi
tarih = datetime.date(yyyy,mm,dd)

def kriter_ve_gonderici(gonderen, tarih, posta_kutusu):
    kriter = AND(from_=gonderen, date_gte=tarih)  # Gönderen ve tarih kriterlerini birleştir
    return posta_kutusu.fetch(kriter)

def oku(gonderen, tarih, kullanici, sifre):
    with MailBox("imap.gmail.com").login(kullanici, sifre, initial_folder="INBOX") as posta_kutusu:
        mesajlar = kriter_ve_gonderici(gonderen, tarih, posta_kutusu)
        for msg in mesajlar:
            print("SUBJECT:",msg.subject)
            print("TEXT:",msg.text)


def ekleri_kaydet(gonderen, tarih, kullanici, sifre):
    with MailBox("imap.gmail.com").login(kullanici, sifre, initial_folder="INBOX") as posta_kutusu: 
        mesajlar = kriter_ve_gonderici(gonderen, tarih, posta_kutusu)
        for msg in mesajlar:
            if msg.attachments:
                klasor_adi = gonderen.split("@")[0]  # @ işaretine göre böler ve ilk olani alir.
                if not os.path.exists(klasor_adi):
                    os.makedirs(klasor_adi)
                
                for attachment in msg.attachments:
                    print("Attachment filename:", attachment.filename)
                    print("Attachment content type:", attachment.content_type)
                    
                    # Ek dosyasını kaydetme
                    dosya_yolu = os.path.join(klasor_adi, attachment.filename)
                    with open(dosya_yolu, 'wb') as f:
                        f.write(attachment.payload)
                
                print(f"Eklentiler '{klasor_adi}' klasörüne kaydedildi.")
            
            else:
                print("Eklenti bulunamadi.")

# E-posta arama ve ekleri kaydetme fonksiyonunu çağır
oku(gonderen, tarih, kullanici, sifre)
ekleri_kaydet(gonderen, tarih, kullanici, sifre)
