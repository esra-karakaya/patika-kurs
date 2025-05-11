#1. Girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul:

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

#2. Girilen sayının tek mi çift mi olduğunu yazan koşul:

sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")

#3. Girilen nota göre harf aralığını yazan koşul (örnek: 80-100 A, 60-80 B):

not_ = int(input("Notunuzu girin: "))

if 80 <= not_ <= 100:
    print("Harf notunuz: A")
elif 60 <= not_ < 80:
    print("Harf notunuz: B")
elif 40 <= not_ < 60:
    print("Harf notunuz: C")
else:
    print("Harf notunuz: F")

#4. Girilen ismin karakter sayısı 5'ten büyükse "uzun bir isminiz var", değilse ismini yazsın:

isim = input("İsminizi girin: ")

if len(isim) > 5:
    print("Uzun bir isminiz var.")
else:
    print(f"İsminiz: {isim}")


#5. Girilen sayının asal olup olmadığını bulan kod dizisi (for ve while)

#for döngüsü ile:

sayi = int(input("Bir sayı girin: "))

if sayi < 2:
    print("Asal sayı değildir.")
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            print("Asal sayı değildir.")
            break
    else:
        print("Asal sayıdır.")

#while döngüsü ile:

sayi = int(input("Bir sayı girin: "))
i = 2
asal = True

if sayi < 2:
    asal = False
else:
    while i < sayi:
        if sayi % i == 0:
            asal = False
            break
        i += 1

if asal:
    print("Asal sayıdır.")
else:
    print("Asal sayı değildir.")

#6. [45, 85, 75, 50] içinde 75 değerinin indeksini yazdıran döngü:

notlar = [45, 85, 75, 50]

for i in range(len(notlar)):
    if notlar[i] == 75:
        print("75'in indisi:", i)
        break

#7. Girilen sayının faktöriyelini alma (for ve while)

#for döngüsü ile:

sayi = int(input("Bir sayı girin: "))
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i

print("Faktöriyel:", faktoriyel)

#while döngüsü ile:

sayi = int(input("Bir sayı girin: "))
faktoriyel = 1
i = 1

while i <= sayi:
    faktoriyel *= i
    i += 1

print("Faktöriyel:", faktoriyel)

#8. Kullanıcıdan pozitif sayı bekleyen, pozitifi görünce yazdıran, negatif gelirse daha sonra tekrar soran kod (for döngüsüyle):

for _ in range(100):  # Çok büyük bir aralık veriyoruz
    sayi = int(input("Pozitif bir sayı girin: "))
    if sayi > 0:
        print("Pozitif sayı girdiniz:", sayi)
        break
    else:
        print("Negatif girdiniz, tekrar deneyin.")

#9. Fonksiyon ile girilen sayının asal olup olmadığını bulan kod dizisi (for ve while):

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

sayi = int(input("Bir sayı girin: "))

if asal_mi(sayi):
    print("Asal sayıdır.")
else:
    print("Asal değildir.")

#10. Fonksiyon ile girilen sayının faktöriyelini alma (for ve while)

def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

sayi = int(input("Bir sayı girin: "))
print("Faktöriyeli:", faktoriyel(sayi))

