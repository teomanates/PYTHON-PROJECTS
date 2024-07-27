#!/bin/python3
#adam asmaca oyunu
import random
import os
from colorama import init, Fore
from hayvanlar import hayvanlar
from arabalar import arabalar
from alfabe import alfabe
from gorseller import gorseller


def ipucu_harf(sorulan_kelime):
	a=random.randint(0,len(sorulan_kelime)-1)
	if sorulan_kelime[a] not in yeni_tahmin:
		return sorulan_kelime[a]
	else:
		return ipucu_harf(sorulan_kelime)

def tekrar_onleme(harf):
	if harf in tahmin_edilen_harfler:
		print("Bu harfi zaten söylediniz!\n")
	else:
		tahmin_edilen_harfler.add(harf)	

def uyari(mesaj):
	print(Fore.RED + mesaj)

def kategori(secim):
	
	if secim == "a":
		kelime = random.choice(arabalar)
		uyari("KAÇOVVVVVVVVVVVV")
		return kelime
	elif secim == "h":
		kelime = random.choice(hayvanlar)
		print("HAYVANLAR YÜKLENİYOR")
		return kelime
	else:
		
		return "gecersiz secim!"		
init(autoreset=True)			
can = 6
yeni_tahmin = ""
tahmin_edilen_harfler = set()

print("OYUNA HOŞ GELDİNİZ.\nArabalar için: a, Hayvanlar için: h tuşuna basınız\n")
sec = (input("kategori seçiniz lütfen: "))
sorulan_kelime = kategori(sec)
print("İpucu için help yazabilirsiniz. 2 hakkınız bulunmaktadır. Başarılarr.\n")

x=len(sorulan_kelime.replace(" ",""))
print("_ "*x)
i=2
while can > 0:
	kelime = ""
	
	for harf in sorulan_kelime:
		if harf in yeni_tahmin:
			kelime += harf
		else:
			kelime += " _ "	
	if (kelime == sorulan_kelime):
		print("Tebrikler, kazandınn!!!. CEVAP: {}".format(kelime))
		break
	
	print(gorseller[6-can],"\n\n\n")
	print("tahmin edin: ",kelime)
	
		
	tahmin = (str(input("Harf giriniz: ")))
	tekrar_onleme(tahmin)
	if tahmin in alfabe:
		yeni_tahmin+=tahmin
		if tahmin not in sorulan_kelime:
			can -=1
			uyari("\nKalan canlarınız: {}\n".format(can))
	if tahmin == "help":
		while i > 0:
			acilan_harf = ipucu_harf(sorulan_kelime)
			print("Harfiniz: ",acilan_harf)
			i-=1
			break
		else:	
			print("İpucu hakkınız kalmadı :c\n")	
	else:
		continue
else:
	print(gorseller[6])
	uyari("KAYBETTİN")
	print("Cevap: {}".format(sorulan_kelime))
	 		
