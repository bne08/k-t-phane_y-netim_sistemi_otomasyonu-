# kutuphane_yonetim_sistemi_otomasyonu-
Kütüphane yönetim otomasyonu projesinde kütüphane sistemimize kullanıcıların kitap alma
işlemleri ve kitapların giriş, çıkış ve ceza hesaplama işlemleri gerçekleştirilmektedir. Sisteme
kayıt olan kullanıcılarımız istedikleri kitabı iade süresi boyunca alabilmektedirler. İade süreci
geçen kullanıcılarımıza kitapların belirlenen fiyatlarına göre cezai işlemler uygulanmaktadır.
Sistemizde yönetimimiz tarafından kullanıcıları ekleme ,silme, listeleme ve arama işlemleri
uygulanmaktadır.Bunun yanında kütüphaneden kitapların aranması(belli ölçütlerle),
listelenmesi ve alınan kitapların çıkış, giriş ve cezalarının hesaplama işlemleride yapılmaktadır.
Sisteme eklenen bir kullanıcı mevcut kitaplarımızdan alabilmektedir. Aynı zamanda
kullanıcılarımız kitapların alındığı tarihler kayıt altında tutulmaktadır. Kullanıcı bir kitabı aldığı
zaman kitabın çıkış işlemi uygulanmaktadır ve iade süresi belirlenmektedir. İade süresi 15
gündür, eğer iade süresini geçen kullanıcı varsa 30 günden az olmak şartıyla gün sayısı kadar
ücret belirlenir eğer 30 günü geçen kitap iade işlemleri varsa kitap fiyatı eklenmektedir.
Kullanıcılar kitapları iade ettiği zamanda kitap giriş işlemi yapılmaktadır. Eğer kitabın iadesi
geciktiyse cezai işlemlerde hesaplama .txt dosyasında belirtilmektedir.
Proje işlevlerinin listesi :
   • Tüm kitapları ve kullanıcıları listeleme
   • Arama ölçütleri :
      Kullanıcı isimleri
      Kullanıcı idsi
      Kitap ismi
      Kitap yazar
      Kitap tür
  • Ekleme ,güncelleme ve silme :
      Kullanıcıları ekleme ve silme
      Kitaplara çıkış ve giriş işlemi güncellemeleri
 • Kullanıcı raporları oluşturma :
     Çıkış geçmişi
     Para cezaları
Proje içinde bulunan txt dosyalar :
   Müşteri.txt : kullanıcıların listesi (id,isim,soyad)
   Kutuhane.txt : Kitapların listesi(id,isim,yazar,tarih,tur,fiyat)
   Hesaplama.txt: Kitapların çıkış ve giriş raporlarının tutulduğu kısım (id, userid, kitapid,
   alımtarihi, vadesi, ceza, toplamceza, giriş veya cıkıs )
