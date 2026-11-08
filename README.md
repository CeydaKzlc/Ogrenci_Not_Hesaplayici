#  Öğrenci Not Sistemi ve Harf Notu Hesaplayıcı (Kayıt Özellikli)

Bu uygulama, Python ve Tkinter kullanılarak geliştirilmiş, görsel arayüze (GUI) sahip bir not hesaplama aracıdır. Öğrencilerin not ortalamasını ve harf notunu hesaplamanın yanı sıra, hesaplanan öğrencileri bellekte tutarak listeleme imkanı sunar.

##  Öne Çıkan Özellikler

* **Veri Yapıları Kullanımı (Liste & Sözlük):**
  * **Sözlük (Dictionary):** Hesaplaması yapılan öğrenciler `ogrenci_kayitlari = {}` adlı sözlükte tutulur. İsimler *Anahtar (Key)*, not bilgileri ise *Değer (Value)* olarak saklanır.
  * **Liste (List):** Öğrencinin tek not veya iki not girmesi ihtimaline karşı girilen geçerli notlar `gecerli_notlar = []` listesinde toplanır ve ortalama bu listenin uzunluğu baz alınarak dinamik şekilde hesaplanır.
* **Geçmiş Kayıtları Görüntüleme:** "Kayıtlı Öğrencileri Göster" butonu sayesinde, uygulama açık kaldığı sürece hesaplanan tüm öğrencilerin listesi (isim, ortalama, harf notu) tek bir ekranda görüntülenebilir.
* **Esnek Not Girişi:** Sadece 1. notu girip 2. notu boş bırakarak da ortalama hesaplanabilir.
* **Kullanıcı Dostu Hata Bildirimi:** Eksik veya hatalı (0-100 aralığı dışı, harf girişi vb.) girişlerde hatalar, kullanıcıyı rahatsız eden pencereler yerine doğrudan arayüzün alt kısmında belirir.

##  Notlandırma Sistemi
* **A:** 85 - 100
* **B:** 70 - 84
* **C:** 50 - 69
* **F:** 0 - 49

##  Nasıl Çalıştırılır?

1. Bilgisayarınızda **Python 3.x** sürümünün yüklü olması gerekmektedir.
2. Proje dosyasını (`arayuz_not.py`) indirin veya kodları kopyalayıp bilgisayarınıza bu isimle kaydedin.
3. Dosyaya çift tıklayarak veya komut satırında `python arayuz_not.py` komutunu çalıştırarak arayüzü başlatabilirsiniz.