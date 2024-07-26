import requests
from PIL import Image
from io import BytesIO

class Futbolcu():
    def __init__(self, isim, hiz, sut, pas, dripling, defans, fizik):
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.dripling = dripling
        self.defans = defans
        self.fizik = fizik
    
    def yetenek_gorseli(self):
        grafik_url = "https://image-charts.com/chart"
        payload = {
            'chco' : '3092de',
            'chd' : 't:' + self.yetenek_hazirla(),
            'chdl' : self.isim,
            'chdlp' : 'b',
            'chs' : '580x580',
            'cht' : 'r',
            'chtt': 'Futbolcu özellikleri',
            'chl' : 'hiz|sut|pas|dripling|defans|fizik',
            'chxl': '0:|0|20|40|60|80|100',
            'chxt': 'x',
            'chxr': '0,0.0,100.0',
            'chm' : 'B,AAAAAABB,0,0,0'
         }
        response = requests.post(grafik_url, data=payload)
        
        image = Image.open(BytesIO(response.content))
        image.show()
        
        
    def yetenek_hazirla(self):
        return ",".join([
        str(self.hiz),
        str(self.sut),
        str(self.pas),
        str(self.dripling),
        str(self.defans),
        str(self.fizik),
        str(self.hiz) #ÖNEMLİ!!! chart tamamlanması için tekrar başa dönmek ister
        ]
        )

    def kiyasla(self, hedef_futbolcu):
        grafik_url = "https://image-charts.com/chart"
        payload = {
            'chco' : '3092de,027182',  # Grafik çizgi renkleri (iki oyuncu için iki renk, hex formatında)
            'chd' : 't:' + self.yetenek_hazirla() + '|' + hedef_futbolcu.yetenek_hazirla(),  # Grafik verileri (iki oyuncunun yetenekleri)
            'chdl' : self.isim + '|' + hedef_futbolcu.isim,  # Grafik açıklaması (iki oyuncunun isimleri)
            'chdlp' : 'b',  # Grafik açıklama pozisyonu (bottom)
            'chs' : '580x580',  # Grafik boyutu (genişlik x yükseklik)
            'cht' : 'r',  # Grafik türü (radar)
            'chtt': 'Futbolcu özellikleri',  # Grafik başlığı
            'chl' : 'hiz|sut|pas|dripling|defans|fizik',  # Grafik etiketleri (özellikler)
            'chxl': '0:|0|20|40|60|80|100',  # Grafik eksen etiketleri (değerler)
            'chxt': 'x',  # Grafik eksen türü (x ekseni)
            'chxr': '0,0.0,100.0',  # Grafik eksen aralığı (0 ile 100 arasında)
            'chm' : 'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'  # Grafik dolgu stili (iki oyuncu için renk ve opaklık)
         }
        response = requests.post(grafik_url, data=payload)
        
        image = Image.open(BytesIO(response.content))
        image.show()

messi = Futbolcu("messi",85,92,91,95,38,65)
ronaldo = Futbolcu("ronaldo",89,93,81,89,35,77)

messi.kiyasla(ronaldo)


