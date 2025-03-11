def question2():
    print("2.Soru: Fantasya'da; Her 7 saniyede bir doğum gerçekleşiyor. Her 13 saniyede bir ölüm meydana geliyor. \n"
          "Her 45 saniyede bir göç alınıyor. Önümüzdeki 5 yıl sonraki popülasyonu hesaplamak için bir program yazın. \n"
          "Şu anki Fantasya nüfusunun 3.000.000 kişi, 1 yılda 365 gün olduğunu varsayın.")

    currentPopulation = 3000000
    yearsToCalculate = 5
    daysInYear = 365
    secondsInDay = 86400

    totalSeconds = yearsToCalculate * daysInYear * secondsInDay

    birthsPerSecond = 1 / 7
    totalBirths = totalSeconds * birthsPerSecond

    deathsPerSecond = 1 / 13
    totalDeaths = totalSeconds * deathsPerSecond

    migrationsPerSecond = 1 / 45
    totalMigrations = totalSeconds * migrationsPerSecond

    finalPopulation = currentPopulation + totalBirths - totalDeaths + totalMigrations

    print(f"\n5 yıl sonraki tahmini nüfus: {int(finalPopulation):,} kişi")
    print(f"Toplam doğum sayısı: {int(totalBirths):,}")
    print(f"Toplam ölüm sayısı: {int(totalDeaths):,}")
    print(f"Toplam göç sayısı: {int(totalMigrations):,}")