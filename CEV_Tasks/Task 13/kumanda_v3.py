import time
import random



class Kumanda():

    def __init__(self, tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal= kanal

    def tv_ac(self):

        if (self.tv_durum  == "Kapalı"):
            print("Tv açılıyor")
            self.tv_durum="Açık"
        else:
            print("Tv zaten acik")

    def tv_kapat(self):
        
        if (self.tv_durum  == "Kapalı"):
            print("Tv zaten kapalı")
        
        else:
            print("Tv zaten kapaniyor")
            self.tv_durum="Kapalı"
    

    def ses_ayari(self):

        while True:

            cevap=input("Sesi artır :>\nSesi azalt: <\nÇıkış: q")

            if (cevap=='>'):
                if self.tv_ses>=100:
                    print("Max Ses")
                else:
                    self.tv_ses+=1
                print("Tv Sesi: {}".format(self.tv_ses))
            
            elif (cevap=="<"):
                if (self.tv_ses<=0):
                    print("Min ses")
                else:
                    self.tv_ses-=1
                print("tv_ses: {}",format(self.tv_ses))
            elif (cevap=="q"):
                break
            else:
                print("hatalı tuşlama")

    def kanal_ekle(self,kanal):
        if kanal in self.kanal_listesi:
            print("Kanal zaten var")
        else:
            
            print("Kanal ekleniyor...")
            time.sleep(1)
            

            self.kanal_listesi.append(kanal)

            print("Kanal listesi: {}".format(self.kanal_listesi))

    def kanal_sec(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]
        print(self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv_durum: {}\ntv_ses: {}\nkanal listesi: {}\nkanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def kanal_degis(self,kanal):
     
      print("Kanal Değiştiriliyor...")
      time.sleep(1)
      self.kanal = kanal
      print("Kanal Değiştirildi...")      


    def kanal_sil(self,kanal):
      print("Kanal Siliniyor...")
      self.kanal_listesi.remove(kanal)
      print("Kanal Silindi")
      
    
    def uygulama_ac(self):
      print("Uygulamalar Açılıyor...")
      time.sleep(1)
      self.kanal = "Apps"
      print("Uygulamalar Açıldı")

    def uygulama_kapat(self):
      print("Uygulamalar Kapanıyor...")
      time.sleep(1)
      self.kanal = "Apps"
      print("Uygulamalar Kapandı")    




print("""

        1. TV aç
        2. TV kapat
        3. Ses Ayarları
        4. Kanal Ekle
        5. Açık Kanalı Öğren
        6. Kanal Sayısı
        7. TV Bilgileri
        8. Kanal Değiştir
        9. Kanal Sil
        10.Uygulamaları Aç
        11.Uygulamaları Kapat

Çıkmak için q'ya bas.

""")
kumanda=Kumanda()

while True:

    islem= input("İslem seçiniz")

    if islem =="q":
        print("Sonlandırılıyor")
     
    elif islem =="1":
        kumanda.tv_ac()
    
    elif islem=="2":
        kumanda.tv_kapat()

    elif islem=="3":
        kumanda.ses_ayari()
    
    elif islem=="4":

        kanal_isimleri=input("Kanal isimlerini lütfen , ile ayırarak giriniz.")

        x=kanal_isimleri.split(",")

        for i in x:
            kumanda.kanal_ekle(i)
    
    elif islem=="5":
        kumanda.kanal_sec()

    elif islem=="6":
        print("Kanal sayısı: ",len(kumanda))
    
    elif islem=="7":
        print(kumanda)

    elif islem == "8":
      kanal = input("Açmak İstediğiniz Kanalı Girin:") 
      kumanda.kanal_degis(kanal)    

    elif islem == "9":
      kanal = input("Silmek istediginiz kanal ismini giriniz : ")
      kumanda.kanal_sil(kanal)

    elif islem == "10":
      kumanda.uygulama_ac()

    elif islem == "11":
      kumanda.uygulama_kapat()  
    else:
        print("hatalı Tuşlama")