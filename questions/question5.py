def question5():
    print(
        "5.Soru: 5 öğrenciden oluşan bir öğrenci not sözlüğü oluşturun. Bu sözlükte öğrencilerin notları value olarak bir listede toplansın.\n"
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