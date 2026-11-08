import tkinter as tk
from tkinter import messagebox

# SÖZLÜK (Dictionary) KULLANIMI: Öğrencileri hafızada tutmak için boş bir sözlük oluşturuyoruz.
ogrenci_kayitlari = {}

def hesapla():
    isim = entry_isim.get().strip()
    
    if not isim:
        lbl_sonuc.config(text="⚠️ Lütfen isim ve soyisim giriniz.", fg="red")
        return

    not1_metin = entry_not1.get().strip()
    not2_metin = entry_not2.get().strip()

    if not not1_metin and not not2_metin:
        lbl_sonuc.config(text="⚠️ Lütfen en az bir not giriniz.", fg="red")
        return

    # LİSTE (List) KULLANIMI: Girilen geçerli notları tutmak için liste oluşturuyoruz.
    gecerli_notlar = []

    try:
        if not1_metin:
            not1 = float(not1_metin)
            if not (0 <= not1 <= 100):
                lbl_sonuc.config(text="⚠️ 1. Not 0-100 arasında olmalıdır.", fg="red")
                return
            gecerli_notlar.append(not1)

        if not2_metin:
            not2 = float(not2_metin)
            if not (0 <= not2 <= 100):
                lbl_sonuc.config(text="⚠️ 2. Not 0-100 arasında olmalıdır.", fg="red")
                return
            gecerli_notlar.append(not2)

    except ValueError:
        lbl_sonuc.config(text="⚠️ Lütfen notlara sadece sayı giriniz!", fg="red")
        return

    ortalama = sum(gecerli_notlar) / len(gecerli_notlar)

    if ortalama >= 85:
        harf = "A"
    elif ortalama >= 70:
        harf = "B"
    elif ortalama >= 50:
        harf = "C"
    else:
        harf = "F"

    # SÖZLÜĞE VERİ EKLEME: Hesaplanan öğrenciyi sözlüğe kaydediyoruz (Anahtar: İsim)
    ogrenci_kayitlari[isim] = {"ortalama": ortalama, "harf": harf}

    sonuc_metni = f"Öğrenci: {isim}\nOrtalama: {ortalama:.2f}\nHarf Notu: {harf}"
    lbl_sonuc.config(text=sonuc_metni, fg="#564A70")

def temizle():
    entry_isim.delete(0, tk.END)
    entry_not1.delete(0, tk.END)
    entry_not2.delete(0, tk.END)
    lbl_sonuc.config(text="")

def kayitlari_goster():
    # Sözlüğün içi boş mu diye kontrol ediyoruz
    if not ogrenci_kayitlari:
        messagebox.showinfo("Kayıtlar", "Henüz kayıtlı öğrenci bulunmuyor.")
        return
        
    kayit_metni = "📋 KAYITLI ÖĞRENCİLER\n" + "-"*30 + "\n"
    # Sözlükteki elemanları (isim ve bilgiler) döngü ile alıp yazdırıyoruz
    for ogrenci, bilgiler in ogrenci_kayitlari.items():
        kayit_metni += f"👤 {ogrenci} | Ort: {bilgiler['ortalama']:.2f} | Harf: {bilgiler['harf']}\n"
        
    messagebox.showinfo("Öğrenci Kayıtları", kayit_metni)

# --- ARAYÜZ (GUI) KURULUMU ---
root = tk.Tk()
root.title("Öğrenci Not Sistemi")
root.geometry("400x500") # Pencere boyutu yeni buton için biraz uzatıldı
root.configure(bg="#BDDEDD")
root.resizable(False, False)

frame = tk.Frame(root, bg="white", padx=30, pady=30, relief=tk.GROOVE, bd=1)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

lbl_baslik = tk.Label(frame, text="🎓 Not Hesaplayıcı", font=("Arial", 16, "bold"), bg="white", fg="#34283F")
lbl_baslik.grid(row=0, column=0, columnspan=2, pady=(0, 20))

lbl_isim = tk.Label(frame, text="İsim Soyisim:", font=("Arial", 10), bg="white", fg="#34283F")
lbl_isim.grid(row=1, column=0, sticky=tk.W, pady=5)
entry_isim = tk.Entry(frame, font=("Arial", 10), width=20, highlightthickness=1, highlightcolor="#88B9C1")
entry_isim.grid(row=1, column=1, pady=5)

lbl_not1 = tk.Label(frame, text="1. Not:", font=("Arial", 10), bg="white", fg="#34283F")
lbl_not1.grid(row=2, column=0, sticky=tk.W, pady=5)
entry_not1 = tk.Entry(frame, font=("Arial", 10), width=20, highlightthickness=1, highlightcolor="#88B9C1")
entry_not1.grid(row=2, column=1, pady=5)

lbl_not2 = tk.Label(frame, text="2. Not:", font=("Arial", 10), bg="white", fg="#34283F")
lbl_not2.grid(row=3, column=0, sticky=tk.W, pady=5)
entry_not2 = tk.Entry(frame, font=("Arial", 10), width=20, highlightthickness=1, highlightcolor="#88B9C1")
entry_not2.grid(row=3, column=1, pady=5)

lbl_bilgi = tk.Label(frame, text="Tek bir not girerek de hesaplayabilirsiniz.", font=("Arial", 8, "italic"), bg="white", fg="#88B9C1")
lbl_bilgi.grid(row=4, column=0, columnspan=2, pady=(5, 10))

btn_frame = tk.Frame(frame, bg="white")
btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

btn_hesapla = tk.Button(btn_frame, text="Hesapla", font=("Arial", 10, "bold"), bg="#7F5388", fg="white", 
                        width=12, relief=tk.FLAT, cursor="hand2", command=hesapla)
btn_hesapla.grid(row=0, column=0, padx=5)

btn_temizle = tk.Button(btn_frame, text="Temizle", font=("Arial", 10, "bold"), bg="#88B9C1", fg="#34283F", 
                        width=12, relief=tk.FLAT, cursor="hand2", command=temizle)
btn_temizle.grid(row=0, column=1, padx=5)

# YENİ EKLENEN BUTON: Sözlükteki verileri gösterir
btn_kayitlar = tk.Button(frame, text="Kayıtlı Öğrencileri Göster", font=("Arial", 10, "bold"), bg="#34283F", fg="white", 
                         width=26, relief=tk.FLAT, cursor="hand2", command=kayitlari_goster)
btn_kayitlar.grid(row=6, column=0, columnspan=2, pady=(5, 0))

lbl_sonuc = tk.Label(frame, text="", font=("Arial", 10, "bold"), bg="white", justify=tk.CENTER)
lbl_sonuc.grid(row=7, column=0, columnspan=2, pady=(15, 0))

root.mainloop()