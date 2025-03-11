import random

def question7():
    print(
        "7.Soru: Aşağıda kullanıcıya her defasınıda yerlerini karıştıracak şekilde 3 soru soran ve ondan cevaplarını alan \n"
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
        print(f"\n****Toplam 3 sorunun {i + 1}. sorusundasınız.*****\n")
        print(f"Soru {i + 1}: {questions[i]['text']}\n")

        for option in questions[i]['options']:
            print(f"-{option}")

        answer = input("\ncevap: ").strip()

        if answer.lower() == questions[i]['answer'].lower():
            print("\ntebrikler bildiniz.")
            correctAnswers += 1

    print(f"\n***Test Özetiniz****")
    print(f"Toplam 3 sorunun {correctAnswers} tanesini bildiniz.")
    print(f"Kazandığınız puan: {int(correctAnswers / 3 * 100)}")