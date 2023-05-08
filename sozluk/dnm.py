dictionary={
    "Hallo":"Merhaba",
    "Auf Wiedersehen":"Güle güle, Hoşça kalın",
    "Guten Morgen":"Günaydın",
    "Guten Abend":"İyi akşamlar",
    "Gute Nacht":"İyi geceler",
    "Heute":"Bugün",
    "Gestern":"Dün",
}
sentence=input("Bir cümle giriniz: ")
words=sentence.lower().split() # cümledeki ökelimeleri ayırmak için, lower ise büyük küçük harf farklılığından oluşacak sorunları önlemek için
for word in words:
    wordMeaning=dictionary.get(word, "[ANLAMI BULUNAMADI]")
    print(f"{word} : {wordMeaning}")