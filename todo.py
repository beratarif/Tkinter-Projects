import tkinter as tk
from tkinter import messagebox
import os

# --- Görevleri dosyaya kaydetme ---
def gorevleri_kaydet():
    with open("gorevler.txt", "w", encoding="utf-8") as f:
        for i in range(gorev_listbox.size()):
            f.write(gorev_listbox.get(i) + "\n")

# --- Görevleri yükleme ---
def gorevleri_yukle():
    if os.path.exists("gorevler.txt"):
        with open("gorevler.txt", "r", encoding="utf-8") as f:
            for satir in f:
                gorev_listbox.insert(tk.END, satir.strip())

# --- Görev ekleme ---
def gorev_ekle():
    gorev = gorev_entry.get().strip()
    if gorev:
        gorev_listbox.insert(tk.END, gorev)
        gorev_entry.delete(0, tk.END)
        gorevleri_kaydet()
    else:
        messagebox.showwarning("Uyarı", "Lütfen boş görev eklemeyin!")

# --- Görev silme ---
def gorev_sil():
    secili = gorev_listbox.curselection()
    if secili:
        gorev_listbox.delete(secili)
        gorevleri_kaydet()
    else:
        messagebox.showwarning("Uyarı", "Silmek için görev seçin!")

# --- Tema değiştirme ---
def tema_degistir():
    global koyu_tema
    koyu_tema = not koyu_tema

    if koyu_tema:
        bg = "#2c2c2c"
        fg = "white"
        btn_bg = "#444"
        entry_bg = "#555"
    else:
        bg = "white"
        fg = "black"
        btn_bg = "#ddd"
        entry_bg = "white"

    pencere.configure(bg=bg)
    gorev_label.config(bg=bg, fg=fg)
    for widget in pencere.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(bg=btn_bg, fg=fg)
        elif isinstance(widget, tk.Entry):
            widget.config(bg=entry_bg, fg=fg, insertbackground=fg)
        elif isinstance(widget, tk.Listbox):
            widget.config(bg=entry_bg, fg=fg)

# --- Ana pencere ---
pencere = tk.Tk()
pencere.title("To-Do List (Tema Destekli)")
pencere.geometry("400x400")

koyu_tema = True

# --- Arayüz Elemanları ---
gorev_label = tk.Label(pencere, text="Görev Ekle:", font=("Arial", 14))
gorev_label.pack(pady=5)

gorev_entry = tk.Entry(pencere, font=("Arial", 12))
gorev_entry.pack(pady=5)

tk.Button(pencere, text="Ekle", command=gorev_ekle).pack(pady=5)
tk.Button(pencere, text="Sil", command=gorev_sil).pack(pady=5)
tk.Button(pencere, text="Tema Değiştir", command=tema_degistir).pack(pady=5)

gorev_listbox = tk.Listbox(pencere, font=("Arial", 12), height=10)
gorev_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# --- Açılışta görevleri yükle ve tema uygula ---
gorevleri_yukle()
tema_degistir()

pencere.mainloop()
