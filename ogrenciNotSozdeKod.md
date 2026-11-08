BAŞLA

SÖZLÜK OLUŞTUR ogrenci_kayitlari = {}

FONKSİYON hesapla():
    OKU isim = Arayüzden isim girdisini al ve boşlukları sil
    OKU not1_metin = Arayüzden 1. not girdisini al
    OKU not2_metin = Arayüzden 2. not girdisini al

    EĞER isim BOŞ İSE:
        SONUÇ ETİKETİNE YAZ ("⚠️ Lütfen isim ve soyisim giriniz.", Renk: Kırmızı)
        FONKSİYONDAN ÇIK
    BİTİR EĞER

    EĞER not1_metin BOŞ VEYA not2_metin BOŞ İSE (İkisi de boşsa):
        SONUÇ ETİKETİNE YAZ ("⚠️ Lütfen en az bir not giriniz.", Renk: Kırmızı)
        FONKSİYONDAN ÇIK
    BİTİR EĞER

    LİSTE OLUŞTUR gecerli_notlar = []

    DENEME (Hata Yakalama):
        EĞER not1_metin DOLU İSE:
            not1 = SAYIYA_ÇEVİR(not1_metin)
            EĞER not1 < 0 VEYA not1 > 100 İSE:
                SONUÇ ETİKETİNE YAZ ("⚠️ 1. Not 0-100 arasında olmalıdır.", Kırmızı)
                FONKSİYONDAN ÇIK
            gecerli_notlar LİSTESİNE EKLE (not1)
        BİTİR EĞER

        EĞER not2_metin DOLU İSE:
            not2 = SAYIYA_ÇEVİR(not2_metin)
            EĞER not2 < 0 VEYA not2 > 100 İSE:
                SONUÇ ETİKETİNE YAZ ("⚠️ 2. Not 0-100 arasında olmalıdır.", Kırmızı)
                FONKSİYONDAN ÇIK
            gecerli_notlar LİSTESİNE EKLE (not2)
        BİTİR EĞER
    HATA DURUMUNDA:
        SONUÇ ETİKETİNE YAZ ("⚠️ Lütfen notlara sadece sayı giriniz!", Kırmızı)
        FONKSİYONDAN ÇIK
    BİTİR DENEME

    ortalama = gecerli_notlar İÇİNDEKİLERİN TOPLAMI / gecerli_notlar ELEMAN SAYISI

    EĞER ortalama >= 85 İSE harf_notu = "A"
    DEĞİLSE EĞER ortalama >= 70 İSE harf_notu = "B"
    DEĞİLSE EĞER ortalama >= 50 İSE harf_notu = "C"
    DEĞİLSE harf_notu = "F"
    BİTİR EĞER

    ogrenci_kayitlari SÖZLÜĞÜNE EKLE (Anahtar: isim, Değer: ortalama ve harf_notu)

    sonuc_metni = "Öğrenci: " + isim + " | Ortalama: " + ortalama + " | Harf Notu: " + harf_notu
    SONUÇ ETİKETİNE YAZ (sonuc_metni, Renk: Koyu Mor)
BİTİR FONKSİYON

FONKSİYON temizle():
    GİRDİ KUTULARINI VE SONUÇ ETİKETİNİ TEMİZLE
BİTİR FONKSİYON

FONKSİYON kayitlari_goster():
    EĞER ogrenci_kayitlari SÖZLÜĞÜ BOŞ İSE:
        EKRANA YAZ (Pop-up: "Henüz kayıtlı öğrenci bulunmuyor.")
        FONKSİYONDAN ÇIK
    BİTİR EĞER

    kayit_metni = "KAYITLI ÖĞRENCİLER \n"
    DÖNGÜ BAŞLA (ogrenci_kayitlari içindeki her bir öğrenci ve bilgisi için):
        kayit_metni = kayit_metni + öğrenci adı + ortalaması + harf notu
    DÖNGÜ BİTİR

    EKRANA YAZ (Pop-up: kayit_metni)
BİTİR FONKSİYON

# --- ARAYÜZ (GUI) BAŞLATMA ---
PENCERE OLUŞTUR (Boyut: 400x500)
GİRDİ KUTULARINI VE ETİKETLERİ EKLE
BUTON EKLE ("Hesapla", İşlev: hesapla)
BUTON EKLE ("Temizle", İşlev: temizle)
BUTON EKLE ("Kayıtlı Öğrencileri Göster", İşlev: kayitlari_goster)
PENCEREYİ SÜREKLİ AÇIK TUT
BİTİR