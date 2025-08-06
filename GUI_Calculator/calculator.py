import tkinter as tk

def topla():
    try:
        sayi1 = int(giris1.get())
        sayi2 = int(giris2.get())
        sonuc.config(text=f"Sonuç: {sayi1+sayi2}")
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def cikar():
    try:
        sayi1 = int(giris1.get())
        sayi2 = int(giris2.get())
        sonuc.config(text=f"Sonuç: {sayi1-sayi2}")
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def böl():
    try:
        sayi1 = int(giris1.get())
        sayi2 = int(giris2.get())
        if sayi2 == 0:
            sonuc.config(text="Sıfıra bölünemez!")
        else:
            sonuc.config(text=f"Sonuç: {sayi1 / sayi2}")
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def carp():
    try:
        sayi1 = int(giris1.get())
        sayi2= int(giris2.get())
        sonuc.config(text=f"Sonuç: {sayi1*sayi2}")
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def temizle():
    giris1.delete(0,tk.END)
    giris2.delete(0,tk.END)
    sonuc.config(text="Sonuç: ")

#Ana Pencere
pencere = tk.Tk()
pencere.title("Python Calculator GUI")
pencere.configure(bg="gray")
pencere.geometry("600x400")

#Font Ayarı
font_ayar = ("Arial", 16)

# 1. Sayı girişi
giris1 = tk.Entry(pencere,font=font_ayar, width=15)
giris1.place(x=180  ) # Sol'a hizalama

# 2. Sayı girişi
giris2 = tk.Entry(pencere,font=font_ayar,width=15)
giris2.place(x=180,y=30) # Giriş 1'in altına hizalama

temizle_butonu = tk.Button(text="Temizle",font=font_ayar, background="gray", fg="white", command=temizle)
temizle_butonu.place(x=180, y=150)

# Buton toplama
buton = tk.Button(pencere,font=font_ayar,background="gray",text="+",
                 fg="white",width=2, command=topla) 
buton.place(x=180,y=65) # Giriş 2'nin altına hizalama

# Çıkarma butonu
buton2 = tk.Button(pencere,font=font_ayar,background="gray",text="-",
                   fg="white",width=2, command=cikar)
buton2.place(x=230, y=65) # Buton2 hizalama

# Çarpma butonu
buton3 = tk.Button(pencere,font=font_ayar,background="gray",text="*",
                   fg="white",width=2,command=carp)
buton3.place(x=280, y=65) # Buton3 hizalama

# Bölme butonu
buton4 = tk.Button(pencere,font=font_ayar,background="gray", text="/",
                   fg="white",width=2, command=böl)
buton4.place(x=330, y=65) # Buton4 hizalaması

# Sonuçların gözüküceği yer
sonuc = tk.Label(text="Sonuç: ",font=font_ayar,background="gray", fg="white")
sonuc.place(x=180, y=117) # Sonuc'un hizalaması

#Çalıştırma
pencere.mainloop()

