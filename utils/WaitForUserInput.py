def waitForUserInput():
    print("\nDevam etmek için ENTER'a basınız, çıkmak için 'q' yazıp ENTER'a basınız...")
    cevap = input()
    if cevap.lower() == 'q':
        print("Çıkış yapılıyor...")
        exit()
    print("Sonraki soruya geçiliyor...\n")