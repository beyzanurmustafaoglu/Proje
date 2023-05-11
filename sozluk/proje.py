class Sozluk:
    def __init__(self):
        with open('proje.txt', 'r') as dosya:
            satirlar = dosya.readlines()
        self.sozluk = {}
        for satir in satirlar:
            kelime, tanim = satir.strip().split(":")
            self.sozluk[kelime]=tanim
        self.kelime_defteri = []
    
    def cumleEkle(self):
        kelime = input("Hakkinda cumle eklemek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime not in self.sozluk:
            print("Aradiginiz kelime bulunamadi!\n Eger kelimeyi sozluge eklemek istiyorsaniz kelime ekle kismina gidebilirsiniz.")
        else:
            with open('proje.txt','r') as dosya:
                satirlar=dosya.readlines()
            with open('proje.txt','w') as dosya:
                for satir in satirlar:
                    if kelime in satir:
                        cumle=input("Eklemek istediginiz cumleyi giriniz:")
                        dosya.write(satir.strip() + f",ornek cumle = {cumle}\n")
                        print(f"'{cumle}' cümlesi,{kelime} kelimesine eklendi.")   
                    else:
                        dosya.write(satir)
                    
    def yorumEkle(self):
        kelime = input("Hakkinda yorum eklemek istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime not in self.sozluk:
            print("Aradiginiz kelime bulunamadi!\n Eger kelimeyi sozluge eklemek istiyorsaniz kelime ekle kismina gidebilirsiniz.")
        else:
            with open('proje.txt','r') as dosya:
                satirlar=dosya.readlines()
            with open('proje.txt','w') as dosya:
                for satir in satirlar:
                    if kelime in satir:
                        yorum=input("Eklemek istediginiz yorumu giriniz:")
                        dosya.write(satir.strip() + f",yorum = {yorum}\n")
                        print(f"'{yorum}' yorumu,{kelime} kelimesine eklendi.")   
                    else:
                        dosya.write(satir)        
    
    def kelime_bilgi_goster(self):
        kelime=input("lutfen aratmak istediginiz kelimeyi giriniz:")
        kelime=kelime.capitalize()
        if kelime in self.sozluk:
            print(f"{kelime} kelimesi için bilgiler:{self.sozluk[kelime]}")  

    def tanim_degistir(self, kelime, tanim):
         if kelime in self.sozluk:
             self.sozluk[kelime] = tanim
             print("Kelimenin tanımı güncellendi.")
         else:
             self.sozluk[kelime] = tanim
             print("Kelime sözlüğe eklendi.")

    def es_anlamli_kelime_ekle(self, kelime, es_anlam):
        if kelime in self.sozluk:
            self.sozluk[kelime].append(es_anlam)
            print("Eş anlamlı sözcük sözlüğe eklendi.")
        else:
            self.sozluk[kelime] = es_anlam


    
    def kelimeyi_deftere_ekle(dosya_adi):
        kelime = input("Anlamını bilmediğiniz kelimeyi giriniz: ")
        anlam=input("Bilmediğiniz kelimenin anlamını giriniz: ")
        with open(dosya_adi, "a") as dosya:
            dosya.write(kelime+":"+anlam+"\n")
    #kelimeyi_deftere_ekle("defter.txt")

    def kelime_defterini_goster(dosya_adi):
        with open(dosya_adi, "r") as dosya:
            for satir in dosya:
                kelime_anlami = satir.strip().split(":")
                kelime = kelime_anlami[0]
                anlam = kelime_anlami[0]
                print(f"{kelime}: {anlam}")
    #kelime_defterini_goster("defter.txt")


    





        
def main():
    sozluk=Sozluk()
    #sozluk.kelime_bilgi_goster()
    #sozluk.cumleEkle()
    #sozluk.yorumEkle()
    #sozluk.kelime_defterine_ekle("defter.txt")

    
main()
