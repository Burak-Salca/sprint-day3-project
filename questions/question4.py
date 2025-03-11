from utils.InputValidator import is_valid_integer


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
            if not is_valid_integer(num.strip()):
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