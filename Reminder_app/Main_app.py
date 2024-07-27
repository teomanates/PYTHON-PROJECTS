from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from email_sender import send_email

kullanici = "<kullanici_adi>" #Kendi posta adresimiz.
sifre = "<sifre>" # NOT: Eğer çift aşamalı doğrulama varsa, google ayarlardan uygulama şifresi alınıp buraya o yazılmalıdır.
alici = kullanici # Başka birine atmak için değiştirilmelidir.

def on_click(event):
    # Eğer metin alanı hala karşılama metnini içeriyorsa, metni siler
    if metin_alani.get("1.0", END).strip() == karsilama_metni:
        metin_alani.delete("1.0", END)
        metin_alani.tag_configure("style", foreground="black")  # Metin rengini normal hale getirir

def on_key_release(event):
    # Metin alanındaki tüm metne stil uygular
    metin_alani.tag_add("default_style", "1.0", "end")

def gonder():
    son_mesaj= ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz başariyla sisteme kaydedilmistir!"

                tip = hatirlatma_tipi_opsiyon.get() if not hatirlatma_tipi_opsiyon.get() == "" else "Genel"
                tarih= hatirlatma_tarih_secici.get() 
                mesaj= metin_alani.get("1.0", "end")

                with open ("path\of\file\hatirlatma.txt", "w") as dosya:
                    dosya.write(
                        '{} kategorisinde {} tarihine ve "{}" notuyla hatirlatma'.format(
                            tip,
                            tarih,
                            mesaj
                        )
                    )
                    dosya.close()

            elif var.get() == 2:
                baslik= "HATIRLATMA!"
                mesaj = metin_alani.get("1.0",END).strip() 
                send_email(kullanici, sifre, alici, baslik, mesaj)
                son_mesaj += "E-posta yoluyla hatirlatma size gönderilecektir!"
            messagebox.showinfo("Başarili İslem", son_mesaj)

        else:
            son_mesaj += "Gerekli alanlari doldurunuz!!"
            messagebox.showwarning("Basarisiz islem", son_mesaj)
    except Exception as e:
          print(f"E-posta gönderimi sirasinda hata oluştu: {e}")
    
    finally:
        master.destroy() #sistemi kapatır

master = Tk()

canvas = Canvas(master, height=450, width=900)
canvas.pack()

frame_ust = Frame(master, bg="#8b795e") 
frame_ust.place(relx=0.1, rely=0.11, relwidth=0.8, relheight=0.1)

frame_alt_sol = Frame(master, bg="#8b795e") 
frame_alt_sol.place(relx=0.1, rely=0.23, relwidth=0.2, relheight=0.5)

frame_alt_sag = Frame(master, bg="#8b795e") 
frame_alt_sag.place(relx=0.31, rely=0.23, relwidth=0.59, relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg="#8b795e", text="Hatirlatma Tipi:", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("")

hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust, 
    hatirlatma_tipi_opsiyon,
    "Dogum Gunu",
    "Alisveris",
    "Odeme",
    )
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust, width =12, background = "#faebd7", foreground="black", borderwidth=1, locale="tr_TR")
hatirlatma_tarih_secici._top_cal.overrideredirect(True)
hatirlatma_tarih_secici.pack(padx= 10, pady=10, side=RIGHT)

hatirlatma_tarihi_etiket = Label(frame_ust, bg="#8b795e", text="Hatirlatma Tarihi:", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)

Label(frame_alt_sol, text="Hatirlatma Yöntemi:", bg="#8b795e", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)#north west

var = IntVar()
R1 = Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable=var, value=1, bg="#8b795e", font="Verdana 10")
R1.pack(anchor=NW, pady=5, padx=15 )

R2 = Radiobutton(frame_alt_sol, text="E-posta Gönder", variable=var, value=2, bg="#8b795e", font="Verdana 10")
R2.pack(anchor=NW, pady=5, padx=15 )

var1 = IntVar()
Checkbutton(frame_alt_sol, text="Bir Hafta Önce", variable=var1, onvalue=1, offvalue=0, bg="#8b795e", font="Verdana 7").pack(anchor=NW, pady=4, padx=40)

var2 = IntVar()
Checkbutton(frame_alt_sol, text="Bir Gün Önce", variable=var2, onvalue=1, offvalue=0, bg="#8b795e", font="Verdana 7").pack(anchor=NW, pady=4, padx=39)

var3 = IntVar()
Checkbutton(frame_alt_sol, text="Bir Saat Önce", variable=var3, onvalue=1, offvalue=0, bg="#8b795e", font="Verdana 7").pack(anchor=NW, pady=4, padx=39)

Label(frame_alt_sag, text="Hatirlatma Mesaji:", bg="#8b795e", font="Verdana 10 bold").pack(padx=10, pady=9, anchor=NW)
metin_alani = Text(frame_alt_sag, height=7, width=60, bg="#faebd7", pady=15)

metin_alani.tag_configure("style", foreground="#838b83", font=("Verdana",7,"bold" ))
metin_alani.tag_configure("default_style", foreground="#8b795e", font=("Verdana", 10, "bold"))

metin_alani.pack()

karsilama_metni =( "Mesaji buraya gir...")

metin_alani.insert(END, karsilama_metni, "style" )

#bind metodu, Tkinter widget'larına belirli olaylar gerçekleştiğinde belirli işlevleri çalıştırmak için kullanılır. 
metin_alani.bind("<FocusIn>", on_click) #<FocusIn> olayı, bir widget odaklandığında (aktif hale geldiğinde) tetiklenir.
metin_alani.bind("<KeyRelease>", on_key_release) #<KeyRelease> olayı, bir tuş bırakıldığında tetiklenir.

gonder_butonu = Button(frame_alt_sag, text="Gönder", command=gonder)
gonder_butonu.pack(anchor=S, pady=10)


master.mainloop()
