import keyboard
import random
import time

def waitForUserInput():
    print("\nDevam etmek için ENTER'a basınız, çıkmak için 'q' yazıp ENTER'a basınız...")
    cevap = input()
    if cevap.lower() == 'q':
        print("Çıkış yapılıyor...")
        exit()
    print("Sonraki soruya geçiliyor...\n")

def question1():
    print("1.Soru: Sen ve ekibin bir restorana gidiyorsunuz. Garson size iyi davranıyor, bu yüzden ona bahşiş vermeye karar veriyorsunuz. \n"
          "Gelen hesap üzerinden %12 oranında bahşiş bırakmak ve hesabı eşit olarak bölüşmek istiyorsunuz. \n"
          "Kişi başı ne kadar hesap ödemeniz gerekir? Lütfen kişi sayısı, fatura ve bahşiş oranını input ile giriniz.")

    while True:
        numberOfPeople = input("Lütfen kişi sayısını giriniz: ")
        billAmount = input("Lütfen fatura tutarını giriniz: ")
        tipPercentage = input("Lütfen bahşiş oranını yüzde olarak giriniz (örn: 12): ")

        if not numberOfPeople.isdigit():
            print("Hata: Kişi sayısı için lütfen sadece sayı giriniz!")
            continue
        if not billAmount.replace(".", "").isdigit():
            print("Hata: Fatura tutarı için lütfen geçerli bir sayı giriniz!")
            continue
        if not tipPercentage.replace(".", "").isdigit():
            print("Hata: Bahşiş oranı için lütfen geçerli bir sayı giriniz!")
            continue
        break

    numberOfPeople = int(numberOfPeople)
    billAmount = float(billAmount)
    tipPercentage = float(tipPercentage)

    tipAmount = billAmount * (tipPercentage / 100)
    totalAmount = billAmount + tipAmount
    amountPerPerson = totalAmount / numberOfPeople

    print(f"\nKişi başı ödemeniz gereken tutar: {amountPerPerson:.2f} TL")

def question2():
    print("2.Soru: Fantasya'da; Her 7 saniyede bir doğum gerçekleşiyor. Her 13 saniyede bir ölüm meydana geliyor. \n"
          "Her 45 saniyede bir göç alınıyor. Önümüzdeki 5 yıl sonraki popülasyonu hesaplamak için bir program yazın. \n"
          "Şu anki Fantasya nüfusunun 3.000.000 kişi, 1 yılda 365 gün olduğunu varsayın.")
    
    currentPopulation = 3000000
    yearsToCalculate = 5
    daysInYear = 365
    secondsInDay = 86400

    totalSeconds = yearsToCalculate * daysInYear * secondsInDay

    birthsPerSecond = 1/7
    totalBirths = totalSeconds * birthsPerSecond

    deathsPerSecond = 1/13
    totalDeaths = totalSeconds * deathsPerSecond

    migrationsPerSecond = 1/45
    totalMigrations = totalSeconds * migrationsPerSecond

    finalPopulation = currentPopulation + totalBirths - totalDeaths + totalMigrations
    
    print(f"\n5 yıl sonraki tahmini nüfus: {int(finalPopulation):,} kişi")
    print(f"Toplam doğum sayısı: {int(totalBirths):,}")
    print(f"Toplam ölüm sayısı: {int(totalDeaths):,}")
    print(f"Toplam göç sayısı: {int(totalMigrations):,}")

def question3():
    print("3.Soru: Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.\n"
          "BKİ 18.5'un altındaysa -------> Zayıf\n"
          "BKİ 18.5 ile 25 arasındaysa ------> Normal\n"
          "BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu\n"
          "BKİ 30'un üstündeyse -------------> Obez\n"
          "Beden Kitle İndeksi, kişinin ağırlığının (kg olarak) boyunun karesine (m olarak) bölünmesiyle hesaplanır.")

    while True:
        weightKg = input("\nLütfen kilonuzu kg cinsinden giriniz: ")
        if not weightKg.replace(".", "").isdigit():
            print("Hata: Kilo için lütfen geçerli bir sayı giriniz!")
            continue
        break

    while True:
        heightMeters = input("Lütfen boyunuzu metre cinsinden giriniz (örn: 1.75): ")
        if not heightMeters.replace(".", "").isdigit():
            print("Hata: Boy için lütfen geçerli bir sayı giriniz!")
            continue
        break

    weightKg = float(weightKg)
    heightMeters = float(heightMeters)
    bodyMassIndex = weightKg / (heightMeters ** 2)
    
    print(f"\nBeden Kitle İndeksiniz: {bodyMassIndex:.2f}")
    
    if bodyMassIndex < 18.5:
        print("Sonuç: Zayıf")
    elif 18.5 <= bodyMassIndex < 25:
        print("Sonuç: Normal")
    elif 25 <= bodyMassIndex < 30:
        print("Sonuç: Fazla Kilolu")
    else:
        print("Sonuç: Obez")

def question4():
    print("4.Soru: Şimdiyse senden numbers isimli bir liste oluşturmanı istiyoruz. \n"
          "Tekrar eden elemanları repeatNumbers adındaki listeye;\n"
          "tekrar etmeyen elemanları uniqueNumbers adındaki listeye kopyalayan bir kod yazmanı ve listeleri ekrana bastırmanı bekliyoruz.")

    while True:
        print("\nLütfen sayıları virgülle ayırarak giriniz (örn: 1,2,3,4,5):")
        inputNumbers = input("Sayıları giriniz: ")
        numbers = inputNumbers.split(",")
        
        isValid = True
        for num in numbers:
            if not num.strip().isdigit():
                print("Hata: Lütfen sadece sayı giriniz!")
                isValid = False
                break
        
        if isValid:
            break

    numbers = [int(num.strip()) for num in numbers]
    repeatNumbers = []
    uniqueNumbers = []
    
    for num in numbers:
        if numbers.count(num) > 1 and num not in repeatNumbers:
            repeatNumbers.append(num)
        elif numbers.count(num) == 1:
            uniqueNumbers.append(num)

    print("Tekrar Eden Sayılar:", repeatNumbers)
    print("Tekrar Etmeyen Sayılar:", uniqueNumbers)

def question5():
    print("5.Soru: 5 öğrenciden oluşan bir öğrenci not sözlüğü oluşturun. Bu sözlükte öğrencilerin notları value olarak bir listede toplansın.\n"
          "Kullanıcıya hangi öğrencinin notlarını görmek istediğini sorun.\n"
          "Öğrencinin notu görüntülendiğinde program sonunda şöyle bir çıktı elde etmelisiniz:")

    studentGrades = {
        "Ahmet": [85, 90, 78],
        "Mehmet": [75, 88, 92],
        "Ayşe": [95, 82, 89],
        "Fatma": [70, 85, 88],
        "Ali": [88, 84, 91]
    }

    print("\nMevcut öğrenciler:")
    for student in studentGrades.keys():
        print(f"- {student}")

    studentName = input("\nNotlarını görmek istediğiniz öğrenicini ismini giriniz:").strip().title()

    foundStudent = None
    for student in studentGrades:
        if student.lower() == studentName.lower():
            foundStudent = student
            break

    if foundStudent:
        grades = studentGrades[foundStudent]
        average = sum(grades) / len(grades)
        
        print(f"\n{foundStudent} isimli öğrencinin;")
        print(f"1. Notu: {grades[0]}")
        print(f"2. Notu: {grades[1]}")
        print(f"3. Notu: {grades[2]}")
        print(f"Not Ortalaması: {average:.2f}")
    else:
        print(f"\nHata: {studentName} isimli öğrenci bulunamadı!")

def question6():
    print("6.Soru: 1'den 100'e kadar tam sayıları aşağıdaki kurallara göre işlemleri yaptırınız.\n"
          "Sayı 3'e tam bölünüyorsa fizz listesine,\n"
          "Sayı 5'e tam bölünüyorsa buzz listesine,\n"
          "Sayı hem 3'e hem 5'e tam bölünüyorsa fizzBuzz listesine,\n"
          "Geri kalan sayıları ise numbers listesine ekleyelim.\n"
          "Oluşturduğunuz listeleri ekrana bastırınız.")
    
    fizzList = []
    buzzList = []
    fizzBuzzList = []
    numbersList = []
    
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            fizzBuzzList.append(number)
        elif number % 3 == 0:
            fizzList.append(number)
        elif number % 5 == 0:
            buzzList.append(number)
        else:
            numbersList.append(number)
    
    print("\nFizz Listesi:", fizzList)
    print("Buzz Listesi:", buzzList)
    print("FizzBuzz Listesi:", fizzBuzzList)
    print("Diğer Sayılar:", numbersList)

def question7():
    print("7.Soru: Aşağıda kullanıcıya her defasınıda yerlerini karıştıracak şekilde 3 soru soran ve ondan cevaplarını alan \n"
          "ardından cevapların doğruluğunu kontrol eden bir program verilmiştir.\n"
          "Bu programdaki ..... olarak bırakılan yerleri doldurunuz.")

    questions = [
        {
            "text": "Hangisi string methodlarından birisi değildir?",
            "options": ["len", "upper", "lower", "return"],
            "answer": "return"
        },
        {
            "text": "Hangisi Bootcamp eğitimlerine katılan Insider çalışanlarından biri değildir?",
            "options": ["Oğulcan", "Kemal", "Gizem", "Semi", "Gül"],
            "answer": "Gül"
        },
        {
            "text": "Bootcamp programına kaç kişi kabul almıştır?",
            "options": ["20", "30", "90", "120"],
            "answer": "90"
        }
    ]

    random.shuffle(questions)
    correctAnswers = 0

    for i in range(3):
        print(f"\n****Toplam 3 sorunun {i+1}. sorusundasınız.*****\n")
        print(f"Soru {i+1}: {questions[i]['text']}\n")

        for option in questions[i]['options']:
            print(f"-{option}")
            
        answer = input("\ncevap: ").strip()
        
        if answer.lower() == questions[i]['answer'].lower():
            print("\ntebrikler bildiniz.")
            correctAnswers += 1
    
    print(f"\n***Test Özetiniz****")
    print(f"Toplam 3 sorunun {correctAnswers} tanesini bildiniz.")
    print(f"Kazandığınız puan: {int(correctAnswers/3 * 100)}")

def question8():
    print("8.Soru: Kumanda isminde bir sınıf oluşturarak aşağıdaki işlemleri yapmasını sağlayan fonksiyonları sınıf içerisinde yazalım."
          "Kumandayı kapatmak için q tuşuna basılmalı ve diğer durumlarda hangi işlemi yapmak istediği sorulmalıdır. \n"
          "Her işlemde gerekli fonksiyonunun sınıf içerisinden çağırılması gerekmektedir.\n"
          "Random ve time kütüphanesini araştırarak kullanabilirsiniz.\n"
          "Kendi istediğiniz özellikleri eklemekte serbetsiniz.")

    class Kumanda:
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

    kumanda = Kumanda()
    
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
        else:
            print("Geçersiz işlem!")

def main():
    print("*********************INSIDER QA BOOTCAMP SPRINT3 GUN3 PROJESİ*********************")
    waitForUserInput()
    question1()
    waitForUserInput()
    question2()
    waitForUserInput()
    question3()
    waitForUserInput()
    question4()
    waitForUserInput()
    question5()
    waitForUserInput()
    question6()
    waitForUserInput()
    question7()
    waitForUserInput()
    question8()

if __name__ == "__main__":
    main()


