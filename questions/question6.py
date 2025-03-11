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