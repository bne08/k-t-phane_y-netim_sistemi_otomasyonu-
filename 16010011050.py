#BÜŞRA NUR ECE
#16010011050

import time
import datetime

son_musteri_id = 0
musteri_list = []
yeni_musteri_id = 0
kutuphane_list = []
hesaplama_list = []
son_hesaplama_id =0

#kutuphane kaydina kullanici ekleyin ve kimlik atayin
def musteri_ekle():
    musteri_first = input("Adinizi giriniz :")
    musteri_last = input("Soyadinizi giriniz :")
    yeni_musteri_id = int(son_musteri_id) + 1

    with open("16010011050_Musteri.txt", "a") as txtfile:
        f = (yeni_musteri_id, musteri_first, musteri_last) #Tuple
        print(f)
        txtfile.write("{},{},{} \n".format(f[0],f[1],f[2]))
        print(' yeni {} {} musterisi eklendi'.format(musteri_first, musteri_last))

#kullanicilar kendilerini kullanici listesinden cikartabilirler
def musteri_sil():
    print("Hangi kullaniciyi silmek istersin ?")
    musteri_id_sil = input("musteri id giriniz :")

    with open('16010011050_Musteri.txt', 'w') as txtfile:
        for p in musteri_list:
            if p.musteri_id != musteri_id_sil:
                f = [p.musteri_id, p.adi, p.soyadi]
                txtfile.write("{},{},{}".format(f[0],f[1],f[2]))
    print('musteri {} silindi'.format(musteri_id_sil))

def musteri_id_arama():
    musteri_id = input("İdnizi giriniz : ")
    bul = False
    for p in musteri_list:
        if p.musteri_id == musteri_id:
            bul = True
            print(p)
    if bul == False:
        print("yanlıs id tekrar giriniz..")   
        time.sleep(2) 
        musteri_arama()      
    
            
       
#musteri listesini döndürür ve müsteri ismi  kayıtla eslesmesini kontrol eder
def musteri_isim_arama():
    musteri_first = input("isminizi giriniz :")    
    #musteri_last = input("Soyadinizi giriniz :")
    ara = False
    for x in musteri_list:
        if x.adi == musteri_first:
            #if x.soyadi == musteri_last:
                ara = True
                print(x)
    if ara == False:
        print("tekrar deneyiniz ")
        time.sleep(2)
        musteri_arama() 

    
def musteri_arama():
    arama = input("İd veya isim hangisine göre aramak istersiniz ? ") #isim veya id yazarak arama kriterinizi belirleyebilirisiniz
    if arama.lower() == 'id':
        musteri_id_arama() #id secersek id arama fonksiyonuna gider
    elif arama.lower()=='isim':
        musteri_isim_arama()
    else:
        print("Yanlıs arama tercihi girdiniz tekrar deneyiniz")
        time.sleep(2)
        musteri_arama()


#müsteri listesini okumak için txt dosyasını aktif eder
def musteri_okuma():
    musteri_list.clear()
    with open('16010011050_Musteri.txt', 'r') as txtfile:
        lines = txtfile.readlines()
        for line in lines:
            row = line.split(",")
            musteri =  MusteriObj(row[0], row[1], row[2])
            musteri_list.append(musteri)
            global son_musteri_id
            son_musteri_id = row[0]


#içice fonksiyon kullanımı
def musteri_listele():
   
    def inner_functions():
        global musteri_list
        for p in musteri_list:
            print(p)
           
    inner_functions()
    
    


def kotuphane_oku():
    kutuphane_list.clear()
    with open('16010011050_Kutuphane.txt', 'r') as txtfile:
        reader = txtfile.readlines()
        for line in reader:
            row = line.split(",")
            kutuphane = KutuphaneObj(row[0], row[1], row[2], row[3], row[4], row[5])
            kutuphane_list.append(kutuphane)
            global son_kitap_id
            son_kitap_id = row[0]


def kitap_isim_ara():
    sonuc = ""
    kitap_isim = input("Aradiğiniz kitabin adi nedir?")
    for c in kutuphane_list:
        if kitap_isim.lower() in c.isim.lower():
            sonuc = c
            print(sonuc)

    if sonuc == "":
        print("uzgunuz kayitlarimizla eşleşmiyor. Tekrar arama yapin")
        kitap_isim_ara()

def kitap_tur_ara():
    sonuc = ""
    kitap_tur = input("Ne tur bir kitap aradiniz roman, tarih, bilim ?")
    for f in kutuphane_list:
        if kitap_tur.lower() in f.tur.lower():
            sonuc = f
            print(sonuc)
    if sonuc == "":
        print("uzgunuz kayit bulamadik tekrar deneyin")
        kitap_tur_ara()

def kitap_yazar_ara():
    sonuc = ""
    kitap_yazar = input("Hangi yazari aramak istersiniz?")
    for a in kutuphane_list:
        if kitap_yazar.lower() in a.yazar.lower():
            sonuc = a
            print(sonuc)
    if sonuc == "":
        print("uzgunuz kayit bulamadik tekrar deneyin")
        kitap_yazar_ara()


def kitap_arama():
    arama = input("isim ,yazar veya ture göre mi arama yapmak istersiniz ")
    if arama.lower() == "isim":
        kitap_isim_ara()
    if arama.lower() == "yazar":
        kitap_yazar_ara()
    if arama.lower() == "tur":
        kitap_tur_ara()


#içice fonksiyonla kitapların listelenmesi
def kitap_listele():
    def listele():
        for c in kutuphane_list:
            print(c)
        
    listele()
       
  

#tum dosyayı oku
def hesap_oku():
    hesaplama_list.clear()
    with open('16010011050_Hesaplama.txt', 'r') as txtfile:
        reader = txtfile.readlines()
        for line in reader:
            row = line.split(",")
            hesapla = HesaplamaObj(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            hesaplama_list.append(hesapla)
            global son_hesaplama_id #listedeki son kimliği globallestir yani yukarıdan tekrar cek
            son_hesaplama_id = row[0] #daha sonra eklenecek son kimliği tanı
    
            

#Kullanıcı kimliğini kontrol ediyor eşleşmezse tekrar deneme işlemi yapıyor ve tekrar hesaplama yapıyor
def check_out():
    musteri_id = input("Kullanici idinizi giriniz ? ")
    bul = False
    for i in musteri_list:
        if musteri_id == i.musteri_id:
            bul = True
    if bul == False:
        print("Hata kimliğinizi tekrar girmeyi deneyin. ")
        check_out()


    kitap_id = input("Kontrol etmek istediğiniz kitabın idsini giriniz ?  ")
    now = datetime.datetime.now() #suanki tarihe bakıyorum
    simdiki_zaman = now.strftime("%m/%d/%y")
    # kullanıcıların her kitap için max 2 hafta suresi var
    cikis_donemi = datetime.timedelta(days=14)
    bitis_tarihi = now + cikis_donemi
    zaman = bitis_tarihi.strftime("%m/%d/%y")
    #txt dosyalarında görülen kimliği, yeni kimlikle artırarak kontrol etmek için kitap eklendi.
    yeni_hesaplama_id = int(son_hesaplama_id) + 1
    #print(son_hesaplama_id)

    #kitap teslim alınmıssa kullanıcı iade edene kadar teslim alamaz
    bul = False
    for i in hesaplama_list:
        if kitap_id == i.kutuphane_id and i.islem_tipi == str("cikis"):
            # program zamanı geldiginde size bilgi verir
            print("uzgunum bu kitap suan alinmiyor. İşlem tarihi " + i.vadesi)
            bul = True

     #eger kitap varsa okuyun,inceleyin ve teslim edin
     #kitabın alındıktan sonra kayıt edilme dosyaya yazılma kısmı
    if bul == False:
        with open('16010011050_Hesaplama.txt', 'a', newline='') as txtfile:
            f = [yeni_hesaplama_id, musteri_id, kitap_id, simdiki_zaman, zaman, "$0.00", "$0.00", "cikis"] #List
            txtfile.write("{},{},{},{},{},{},{},{}\n".format(f[0],f[1], f[2], f[3], f[4], f[5], f[6], f[7]))
            print('{} nolu kullanıcıya {} kitabı verildi'.format(musteri_id, kitap_id))


#kullanıcının kitabı geri iade işlemi için iade listesine yeni bir kitap ekleme kısmı ve kullanıcının borcunu hesapla
def check_in_guncelle():
    musteri_id = input("musteri idsi giriniz:")
    kitap_id = input("İade etmek istediğiniz kitabın id'si nedir?")
    yeni_hesaplama_id = int(son_hesaplama_id) + 1
    for row in hesaplama_list:
        # kullanıcı bilgilerini hesaplama dosyasıyla eslesmesini kontrol etme
        if musteri_id == row.musteri_id and kitap_id == row.kutuphane_id and row.islem_tipi.__contains__("cikis") :
            print("Girdi1")
            with open('16010011050_Hesaplama.txt', 'a', newline='') as txtfile:
                now = datetime.datetime.now()
                vade_tarihi = datetime.datetime.strptime(row.vadesi, "%m/%d/%y")#iade etmesi gereken tarihi atadık
                fark = (now - vade_tarihi).days #iade ettiği suanki tarihle etmesi gereken tarihi farkını aldık


                tum_ceza = 0
                ceza = 0

                #eger zaman uzunluğu 30 gunden fazla ise normal para cezasına kitap fiyatını ekleyin
                if fark > 30:
                    tum_ceza = (fark * .25) + float((kitap_fiyat_bul(row.kutuphane_id).replace('$','')).replace('\n',''))
                    print(tum_ceza)

                #verdiği tarih iade etmesi gereken tarihten buyukse ve 30dan azsa fark kadar ceza guncelle
                elif now > vade_tarihi:
                    ceza = fark * .25
                    print(ceza)
                #güncellenmis para cezalarıyla txt dosyasına satır ekleme
                f = [yeni_hesaplama_id, musteri_id, kitap_id, row.cikis_tarihi, row.vadesi,ceza,tum_ceza,"giris"]
                txtfile.write("{},{},{},{},{},${},${},{}\n".format(f[0],f[1], f[2], f[3], f[4], f[5], f[6], f[7]))
                print('{} kullanıcısı  {}.kitabı iade etmistir.'.format(musteri_id, kitap_id))



def ceza_hesapla():
    total_ceza =0.0
    musteri_id = eval(input("musteri id si giriniz ?"))             
    for row in hesaplama_list:
        if str(musteri_id) == row.musteri_id:
            kitap_bulunan = kitap_bul(row.kutuphane_id, musteri_id)
            if kitap_bulunan.islem_tipi == 'cikis':

                now = datetime.datetime.now()
                vade_tarihi = datetime.datetime.strptime(kitap_bulunan.vadesi, "%m/%d/%y")
                ceza = 0
                fark = (now - vade_tarihi).days

                if fark > 30:
                    ceza = (fark * .25) + int(kitap_fiyat_bul(kitap_bulunan.kutuphane_id))

                elif now > vade_tarihi:
                    ceza = fark * .25

                total_ceza += ceza
                print('{} kimlikli kitap için cezanız ${:,.2f}'.format(kitap_bulunan.kutuphane_id, float(ceza)))
            else:
                total_ceza += float(row.toplam_ceza.replace('$', ''))
                print(' {} nolu kitabınızın cezası {}'.format(row.kutuphane_id, row.toplam_ceza))
    print('Total = ${:,.2f}'.format(float(total_ceza)))

#def ceza() ve def check-in_guncelle() işlemleri için para cezalarını hesaplamak için kullanılır
def kitap_fiyat_bul(kitap_id):
    for row in kutuphane_list:
        if str(kitap_id) == row.id:
            return row.tam_fiyat

        

#kullanıcı ve kitap id ye göre check-out listesinden kitap ara
#txt dosyasından verileri dondur
def kitap_bul(kitap_id, musteri_id):
    for row in hesaplama_list:
        if str(kitap_id) == row.kutuphane_id and str(musteri_id) == row.musteri_id:
            return row


def menu():
    print ("""\n
    -------------------------MENU-----------------------
    1. Müşteri Ekle
    2. Müşteri Silme
    3. Müşteri Kaydı Ara
    4. Müşteri Listesinin Tamamını Görüntüle
    5. Kitap Ara
    6. Tüm Kitapları Görüntüle
    7. Kitap Çıkış İşlemi Yapma 
    8. Kitap iade İşlemi
    9. Cezaları hesapla

    ----------------------------------------------------
    """)
    secim = input("Lütfen seçim yapınız? \n\n(Lütfen giriniz [1-9]):  ")
    print('\n')
    # Tüm fonksiyonların cagırıldığı kısım
    if secim == "1":
        musteri_ekle()
    if secim == "2":
        musteri_sil()
    if secim == "3":
        musteri_arama()
    if secim == "4":
        musteri_listele()
    if secim == "5":
        kitap_arama()
    if secim == "6":
        kitap_listele()
    if secim == "7":
        check_out()
    if secim == "8":
        check_in_guncelle()
    if secim == "9":
        ceza_hesapla()
       
    soru = input('\nAna menüye geri dönmek ister misiniz ?  [yes/no]')
    if soru.lower() == 'yes':
       main()

def main():


    #Dosyalarımızın cagırılması
    musteri_okuma()
    kotuphane_oku()
    hesap_oku()

    menu()









class KutuphaneObj:

    def __init__(self, id, isim, yazar, tur, yayin_tarihi, tam_fiyat):
        self.id = id
        self.isim = isim
        self.yazar = yazar
        self.tur = tur
        self.yayin_tarihi = yayin_tarihi
        self.tam_fiyat = tam_fiyat

    def __str__(self):
        return "[{}]\t{}\n\t\tyazar = {}\n\t\ttur = {}\n\t\tyayin_tarihi = {}\n\t\ttam_fiyat = {}"\
            .format(self.id,
                    self.isim,
                    self.yazar,
                    self.tur,
                    self.yayin_tarihi,                  
                    self.tam_fiyat)
class HesaplamaObj:

    def __init__(self, id, musteri_id, kutuphane_id, cikis_tarihi, vadesi, cezasi, toplam_ceza, islem_tipi):
        self.id = id
        self.musteri_id = musteri_id
        self.kutuphane_id = kutuphane_id
        self.cikis_tarihi = cikis_tarihi
        self.vadesi = vadesi
        self.cezasi = cezasi
        self.toplam_ceza = toplam_ceza
        self.islem_tipi = islem_tipi

    def __str__(self):
        return "ID = {}\n\t\tmusteri_id = {}\n\t\tkutuphane_id = {}\n\t\tcikis_tarihi = {}\n\t\tvadesi = {}\n\t\tceza = {}\n\t\ttoplam_ceza = {}\n\t\tislem_tipi = {}"\
            .format(self.id,
                    self.musteri_id,
                    self.kutuphane_id,
                    self.cikis_tarihi,
                    self.vadesi,
                    self.cezasi,
                    self.toplam_ceza,
                    self.islem_tipi)
class MusteriObj:

    def __init__(self, musteri_id, adi, soyadi):
       self.musteri_id = musteri_id
       self.adi = adi
       self.soyadi = soyadi
        

    def __str__(self):
        return "[{}] {} {}".format(self.musteri_id, self.adi, self.soyadi)
main()
