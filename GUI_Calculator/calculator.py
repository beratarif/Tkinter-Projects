import tkinter as tk

def topla():
    try:
        sayi1 = float(giris1.get())
        sayi2 = float(giris2.get())
        sonuc_str = f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
        sonuc.config(text=f"Sonuç: {sayi1 + sayi2}")
        gecmis_ekle(sonuc_str)
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def cikar():
    try:
        sayi1 = float(giris1.get())
        sayi2 = float(giris2.get())
        sonuc_str = f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
        sonuc.config(text=f"Sonuç: {sayi1 - sayi2}")
        gecmis_ekle(sonuc_str)
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def carp():
    try:
        sayi1 = float(giris1.get())
        sayi2 = float(giris2.get())
        sonuc_str = f"{sayi1} × {sayi2} = {sayi1 * sayi2}"
        sonuc.config(text=f"Sonuç: {sayi1 * sayi2}")
        gecmis_ekle(sonuc_str)
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def böl():
    try:
        sayi1 = float(giris1.get())
        sayi2 = float(giris2.get())
        if sayi2 == 0:
            sonuc.config(text="Sıfıra bölünemez!")
        else:
            sonuc_str = f"{sayi1} ÷ {sayi2} = {sayi1 / sayi2}"
            sonuc.config(text=f"Sonuç: {sayi1 / sayi2}")
            gecmis_ekle(sonuc_str)
    except ValueError:
        sonuc.config(text="Lütfen sayıları doğru girin!")

def temizle():
    giris1.delete(0, tk.END)
    giris2.delete(0, tk.END)
    sonuc.config(text="Sonuç: ")

def gecmis_ekle(islem):
    gecmis_listbox.insert(tk.END, islem)

def gecmis_temizle():
    gecmis_listbox.delete(0, tk.END)

def tema_degistir():
    global koyu_tema
    koyu_tema = not koyu_tema
    
    if koyu_tema:
        bg_renk = "gray"
        fg_renk = "black"
        buton_renk = "dimgray"
        entry_bg = "lightgray"
    else:
        bg_renk = "white"
        fg_renk = "black"
        buton_renk = "lightgray"
        entry_bg = "white"
    
    pencere.configure(bg=bg_renk)
    for widget in pencere.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(bg=buton_renk, fg=fg_renk)
        elif isinstance(widget, tk.Label):
            widget.configure(bg=bg_renk, fg=fg_renk)
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=entry_bg, fg=fg_renk)
        elif isinstance(widget, tk.Listbox):
            widget.configure(bg=entry_bg, fg=fg_renk)

# Ana pencere
pencere = tk.Tk()
pencere.title("Python Hesap Makine Projesi")
pencere.geometry("800x400")
koyu_tema = True

font_ayar = ("Arial", 16)

# Giriş alanları
giris1 = tk.Entry(pencere, font=font_ayar, width=15)
giris1.place(x=50, y=10)

giris2 = tk.Entry(pencere, font=font_ayar, width=15)
giris2.place(x=50, y=50)

# İşlem butonları
tk.Button(pencere, font=font_ayar, text="+", width=2, command=topla).place(x=50, y=100)
tk.Button(pencere, font=font_ayar, text="-", width=2, command=cikar).place(x=100, y=100)
tk.Button(pencere, font=font_ayar, text="*", width=2, command=carp).place(x=150, y=100)
tk.Button(pencere, font=font_ayar, text="/", width=2, command=böl).place(x=200, y=100)

# Sonuç etiketi
sonuc = tk.Label(pencere, text="Sonuç: ", font=font_ayar)
sonuc.place(x=50, y=150)

# Temizleme ve tema butonları
tk.Button(pencere, font=font_ayar, text="Temizle", command=temizle).place(x=50, y=200)
tk.Button(pencere, font=font_ayar, text="Tema Değiştir", command=tema_degistir).place(x=160, y=200)

# Geçmiş listbox
gecmis_label = tk.Label(pencere, text="Geçmiş", font=("Arial", 14, "bold"))
gecmis_label.place(x=500, y=10)

gecmis_listbox = tk.Listbox(pencere, font=("Arial", 12), width=30, height=15)
gecmis_listbox.place(x=500, y=40)

tk.Button(pencere, text="Geçmişi Sil", font=("Arial", 12), command=gecmis_temizle).place(x=500, y=340)

# İlk tema uygula
tema_degistir()

pencere.mainloop()
