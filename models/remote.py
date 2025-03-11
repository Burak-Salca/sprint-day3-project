import random
import time
from interfaces.remote import remoteMethods

class Remote(remoteMethods):
    def __init__(self):
        self.tv_durum = False
        self.ses = 50
        self.kanallar = ["Kanal1", "Kanal2", "Kanal3"]
        self.suanki_kanal = self.kanallar[0]
        self.favori_kanallar = []
    
    def tv_ac(self):
        if not self.tv_durum:
            print("TV açılıyor...")
            time.sleep(1)
            self.tv_durum = True
            print("TV açıldı")
        else:
            print("TV zaten açık")
    
    def tv_kapat(self):
        if self.tv_durum:
            print("TV kapanıyor...")
            time.sleep(1)
            self.tv_durum = False
            print("TV kapandı")
        else:
            print("TV zaten kapalı")
    
    def ses_ayari(self):
        while True:
            print(f"\nŞu anki ses seviyesi: {self.ses}")
            cevap = input("Sesi azaltmak için '<', artırmak için '>', çıkmak için 'q' tuşuna basın: ")
            
            if cevap == "<":
                if self.ses > 0:
                    self.ses -= 10
                    print("Ses azaltılıyor...")
            elif cevap == ">":
                if self.ses < 100:
                    self.ses += 10
                    print("Ses artırılıyor...")
            elif cevap == "q":
                break
    
    def kanal_ekle(self):
        kanal = input("Eklemek istediğiniz kanalın adını girin: ")
        if kanal in self.kanallar:
            print("Bu kanal zaten mevcut!")
            return
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanallar.append(kanal)
        print(f"{kanal} başarıyla eklendi")

    def kanal_sil(self):
        if not self.kanallar:
            print("Silinecek kanal yok")
            return
        
        print("\nMevcut Kanallar:")
        for i, kanal in enumerate(self.kanallar, 1):
            print(f"{i}. {kanal}")

        secim = int(input("\nSilmek istediğiniz kanalın numarasını girin: "))
        if 1 <= secim <= len(self.kanallar):
            silinecek_kanal = self.kanallar[secim-1]
            print(f"{silinecek_kanal} siliniyor...")
            time.sleep(1)
                
            if silinecek_kanal in self.favori_kanallar:
                self.favori_kanallar.remove(silinecek_kanal)

            self.kanallar.pop(secim-1)
            print(f"{silinecek_kanal} başarıyla silindi")
        else:
            print("Geçersiz kanal numarası")

    def kanal_ara(self):
        aranan = input("Aramak istediğiniz kanalın adını girin: ").lower()
        bulunan_kanallar = [kanal for kanal in self.kanallar if aranan in kanal.lower()]
        
        if bulunan_kanallar:
            print("\nBulunan Kanallar:")
            for i, kanal in enumerate(bulunan_kanallar, 1):
                print(f"{i}. {kanal}")
        else:
            print("Aranan kriterlere uygun kanal bulunamadı")

    def favorilere_ekle(self):
        if not self.kanallar:
            print("Favori eklemek için önce kanal eklemelisiniz")
            return
        
        print("\nKanal Listesi:")
        for i, kanal in enumerate(self.kanallar, 1):
            print(f"{i}. {kanal}")
        
        print("\nFavori Kanallar:")
        if self.favori_kanallar:
            for i, kanal in enumerate(self.favori_kanallar, 1):
                print(f"{i}. {kanal}")
        else:
            print("Henüz favori kanal yok")

        try:
            secim = int(input("\nFavorilere eklemek istediğiniz kanalın numarasını girin: "))
            if 1 <= secim <= len(self.kanallar):
                kanal = self.kanallar[secim-1]
                if kanal in self.favori_kanallar:
                    print(f"{kanal} zaten favorilerde!")
                else:
                    self.favori_kanallar.append(kanal)
                    print(f"{kanal} favorilere eklendi!")
            else:
                print("Geçersiz kanal numarası!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

    def favorilerden_cikar(self):
        if not self.favori_kanallar:
            print("Favori listeniz boş!")
            return
        
        print("\nFavori Kanallar:")
        for i, kanal in enumerate(self.favori_kanallar, 1):
            print(f"{i}. {kanal}")

        try:
            secim = int(input("\nFavorilerden çıkarmak istediğiniz kanalın numarasını girin: "))
            if 1 <= secim <= len(self.favori_kanallar):
                kanal = self.favori_kanallar.pop(secim-1)
                print(f"{kanal} favorilerden çıkarıldı!")
            else:
                print("Geçersiz kanal numarası!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

    def kanal_sayisi(self):
        return len(self.kanallar)
    
    def rastgele_kanal(self):
        if not self.kanallar:
            print("Kanal listesi boş")
            return
        rastgele = random.choice(self.kanallar)
        print("Kanal değiştiriliyor...")
        time.sleep(1)
        self.suanki_kanal = rastgele
        print(f"Şu anki kanal: {self.suanki_kanal}")
    
    def tv_bilgileri(self):
        print("\n=== TV BİLGİLERİ ===")
        print(f"TV Durumu: {'Açık' if self.tv_durum else 'Kapalı'}")
        print(f"Şu anki ses: {self.ses}")
        print("\nKanal Listesi:")
        for i, kanal in enumerate(self.kanallar, 1):
            print(f"{i}. {kanal}")
        print(f"\nŞu anki kanal: {self.suanki_kanal}")
        print("\nFavori Kanallar:")
        if self.favori_kanallar:
            for i, kanal in enumerate(self.favori_kanallar, 1):
                print(f"{i}. {kanal}")
        else:
            print("Henüz favori kanal eklenmemiş")

    def kanallari_goster(self):
        if not self.kanallar:
            print("Kanal listesi boş!")
            return
        
        print("\n=== MEVCUT KANALLAR ===")
        for i, kanal in enumerate(self.kanallar, 1):
            print(f"{i}. {kanal}")
        print("=====================") 