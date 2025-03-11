from utils.InputValidator import is_valid_number, is_valid_integer


def question1():
    print("1.Soru: Sen ve ekibin bir restorana gidiyorsunuz. Garson size iyi davranıyor, bu yüzden ona bahşiş vermeye karar veriyorsunuz. \n"
          "Gelen hesap üzerinden %12 oranında bahşiş bırakmak ve hesabı eşit olarak bölüşmek istiyorsunuz. \n"
          "Kişi başı ne kadar hesap ödemeniz gerekir? Lütfen kişi sayısı, fatura ve bahşiş oranını input ile giriniz.")

    while True:
        numberOfPeople = input("Lütfen kişi sayısını giriniz: ")
        billAmount = input("Lütfen fatura tutarını giriniz: ")
        tipPercentage = input("Lütfen bahşiş oranını yüzde olarak giriniz (örn: 12): ")

        if not is_valid_integer(numberOfPeople):
            print("Hata: Kişi sayısı için lütfen sadece sayı giriniz!")
            continue
        if not is_valid_number(billAmount):
            print("Hata: Fatura tutarı için lütfen geçerli bir sayı giriniz!")
            continue
        if not is_valid_number(tipPercentage):
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