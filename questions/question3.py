from utils.InputValidator import is_valid_number


def question3():
    print(
        "3.Soru: Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.\n"
        "BKİ 18.5'un altındaysa -------> Zayıf\n"
        "BKİ 18.5 ile 25 arasındaysa ------> Normal\n"
        "BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu\n"
        "BKİ 30'un üstündeyse -------------> Obez\n"
        "Beden Kitle İndeksi, kişinin ağırlığının (kg olarak) boyunun karesine (m olarak) bölünmesiyle hesaplanır.")

    while True:
        weightKg = input("\nLütfen kilonuzu kg cinsinden giriniz: ")
        if not is_valid_number(weightKg):
            print("Hata: Kilo için lütfen geçerli bir sayı giriniz!")
            continue
        break

    while True:
        heightMeters = input("Lütfen boyunuzu metre cinsinden giriniz (örn: 1.75): ")
        if not is_valid_number(heightMeters):
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
