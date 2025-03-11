from models.remote import Remote
from utils.InputValidator import validate_menu_choice

def question8():
    print(
        "8.Soru: Kumanda isminde bir sınıf oluşturarak aşağıdaki işlemleri yapmasını sağlayan fonksiyonları sınıf içerisinde yazalım."
        "Kumandayı kapatmak için q tuşuna basılmalı ve diğer durumlarda hangi işlemi yapmak istediği sorulmalıdır. \n"
        "Her işlemde gerekli fonksiyonunun sınıf içerisinden çağırılması gerekmektedir.\n"
        "Random ve time kütüphanesini araştırarak kullanabilirsiniz.\n"
        "Kendi istediğiniz özellikleri eklemekte serbetsiniz.")

    kumanda = Remote()
    valid_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "q"]

    while True:
        print("""
        1. TV Aç
        2. TV Kapat
        3. Ses Ayarları
        4. Kanal Ekle
        5. Kanal Sil
        6. Kanal Ara
        7. Favorilere Ekle
        8. Favorilerden Çıkar
        9. Kanal Sayısı
        10. Rastgele Kanal
        11. TV Bilgileri
        12. Mevcut Kanallar
        q. Çıkış
        """)

        islem = input("Yapmak istediğiniz işlemi seçin: ")

        if not validate_menu_choice(islem, valid_choices):
            print("Geçersiz işlem!")
            continue

        if islem == "q":
            print("Programdan çıkılıyor...")
            break

        if not kumanda.tv_durum and islem != "1":
            print("Önce TV'yi açmalısınız!")
            continue

        if islem == "1":
            kumanda.tv_ac()
        elif islem == "2":
            kumanda.tv_kapat()
        elif islem == "3":
            kumanda.ses_ayari()
        elif islem == "4":
            kumanda.kanal_ekle()
        elif islem == "5":
            kumanda.kanal_sil()
        elif islem == "6":
            kumanda.kanal_ara()
        elif islem == "7":
            kumanda.favorilere_ekle()
        elif islem == "8":
            kumanda.favorilerden_cikar()
        elif islem == "9":
            print(f"Kanal Sayısı: {kumanda.kanal_sayisi()}")
        elif islem == "10":
            kumanda.rastgele_kanal()
        elif islem == "11":
            kumanda.tv_bilgileri()
        elif islem == "12":
            kumanda.kanallari_goster()