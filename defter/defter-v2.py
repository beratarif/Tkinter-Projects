import tkinter as tk
import os

sayac = 1  # Varsayılan dosya numarası

# Daha önceki en son not dosyasını bul
while os.path.exists(f"not{sayac}.txt"):
    sayac += 1

def kaydet(event=None):  # event parametresi, Ctrl+S için gerekli
    global sayac
    metin = yazi.get("1.0", "end-1c")
    dosya_adi = f"not{sayac}.txt"
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(metin)
    sayac += 1

pencere = tk.Tk()
pencere.title("Karanlık Tema Not Defteri")
pencere.configure(bg="#2b2b2b")

yazi = tk.Text(pencere, bg="#1e1e1e", fg="white", insertbackground="white")
yazi.pack(fill="both", expand=True)

kaydetButonu = tk.Button(pencere, text="Kaydet", bg="#444", fg="white", command=kaydet)
kaydetButonu.pack()

# Ctrl+S kısayolu tanımla
pencere.bind("<Control-s>", kaydet)

pencere.mainloop()
