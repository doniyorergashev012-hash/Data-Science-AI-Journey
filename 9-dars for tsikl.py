# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# ismlar=['Doniyor',"Sardor","Alisher",'Olim','Anvar']
# for ism in ismlar:
#     print(f"Salom {ism} bugun choyxonaga borasanmi")
# print(f"Kod {len(ismlar)} marta takrorlandi")
# toq_sonlar=list(range(10,100,3))
# for son in toq_sonlar:
#     print(f"{son} ning kubi {son**3} ga teng") 
# kinolar=[]
# print("Eng yoqtirgan 5 ta filmingiz qaysilar?")
# for i in range(5):
#     kinolar.append(input(f"{i+1}-filmingizni kiriting:"))
# print(kinolar)    
# ismlar=[]
# print("Bugun necha kishi bilan uchrashdingiz va ular kimlar?")
# soni=int(input('Necha kishi:'))
# for i in range(soni):
#     ismlar.append(input(f"{i+1}-ning ismi:"))
# print(ismlar)

# 1. Sonlarni alohida chiqarish
# numbers = [12, 25, 8, 41, 16]
# Ro‘yxatdagi har bir sonni for yordamida alohida qatorda chiqaring.


# 2. Mahsulotlar ro‘yxati
# products = ["Non", "Sut", "Olma", "Guruch", "Tuxum"]
# Har bir mahsulot nomini for yordamida alohida qatorda chiqaring.


# 3. Ismlarni raqamlash
# names = ["Ali", "Vali", "Malika", "Aziza"]
# Har bir ismni oldidan tartib raqami bilan chiqaring.



# 4. Sonlarni ikki baravar qilish
# numbers = [3, 7, 12, 5, 9]
# Ro‘yxatdagi har bir sonning ikki baravarini for yordamida
# hisoblab, natijalarni alohida qatorda chiqaring.


# 5. Narxlarni hisoblash
# prices = [10000, 25000, 15000, 30000]
# Har bir mahsulot narxiga 10% qo‘shib, yangi narxni chiqaring.


# 6. Ismlarni katta harfda chiqarish
# names = ["ali", "malika", "sardor", "aziza"]
# Har bir ismni upper() yordamida katta harflarga o‘tkazib,
# alohida qatorda chiqaring.


# 7. So‘zlar uzunligi
# words = ["Python", "AI", "Dasturlash", "SQL"]
# Har bir so‘zning uzunligini len() yordamida hisoblab,
# so‘z va uning uzunligini bir qatorda chiqaring.


# 8. Sonlar yig‘indisi
# numbers = [10, 20, 30, 40, 50]
# for yordamida ro‘yxatdagi barcha sonlarni qo‘shib,
# umumiy yig‘indini hisoblang.
# sum() metodidan foydalanmang.


# 9. Xaridlar summasi
# prices = [12000, 8000, 25000, 15000]
# for yordamida barcha narxlarni qo‘shib,
# xaridlarning umumiy summasini hisoblang.


# 10. Takroriy salomlashish
# for va range() yordamida "Assalomu alaykum!"
# matnini 5 marta alohida qatorda chiqaring.


# 11. Ko‘paytirish jadvali
# son = 7
# for va range() yordamida 7 sonining 1 dan 10 gacha
# bo‘lgan ko‘paytirish jadvalini chiqaring.

# 12. Sonlarning kvadrati
# numbers = [2, 4, 6, 8, 10]
# for yordamida har bir sonning kvadratini hisoblab,
# natijalarni alohida qatorda chiqaring.


# 13. Tuple elementlari
# subjects = ("Python", "Matematika", "Ingliz tili", "SQL")
# for yordamida tuple ichidagi barcha fan nomlarini
# alohida qatorda chiqaring.


# 14. Elementlar indeksi
# cities = ["Toshkent", "Samarqand", "Buxoro", "Xiva"]
# range() va len() yordamida har bir shaharni
# uning indeksi bilan chiqaring.

# 15. Haftalik xarajatlar
# expenses = [15000, 22000, 10000, 18000, 25000, 12000, 20000]
# for yordamida barcha kunlik xarajatlarni qo‘shib,
# haftalik umumiy xarajatni hisoblang.

# numbers = [12, 25, 8, 41, 16]
# for number in numbers:
#     print(number)

# products = ["Non", "Sut", "Olma", "Guruch", "Tuxum"]
# for i in products:
#     print(i)

# names = ["Ali", "Vali", "Malika", "Aziza"]
# for i in range(len(names)):
#     print(i+1,names[i])

# numbers = [3, 7, 12, 5, 9]
# for number in numbers:
#     print(number*2)    

# prices = [10000, 25000, 15000, 30000]
# for price in prices:
#     print(f"Narxlarimiz 10% ga oshdi : {price*0.1+price}")
    
# names = ["ali", "malika", "sardor", "aziza"]
# for name in names:
#     print(f"{name.upper()}")    

# words = ["Python", "AI", "Dasturlash", "SQL"]
# for word in words:
#     print(f"{len(word)} {word}")

# numbers = [10, 20, 30, 40, 50]
# yigindi=0
# for son in numbers:
#     yigindi=son+yigindi
# print(yigindi)    
    
# prices = [12000, 8000, 25000, 15000]
# umumiy=0
# for price in prices:
#     umumiy=price+umumiy
# print(f"Men bugun {umumiy} suma ishlatdim yangi yil uchun")    

# for i in range(5):
#     print(i+1,"Assalom aleykum")

# son = 7
# for i in range(10):
#     print(f"{son}x{i+1}={son*(i+1)}")

# numbers = [2, 4, 6, 8, 10]
# for son in numbers:
#     print(f"{son} ning kvadrati={son**2}")

# subjects = ("Python", "Matematika", "Ingliz tili", "SQL")
# for fan in subjects:
#     print(fan)

# cities = ["Toshkent", "Samarqand", "Buxoro", "Xiva"]
# for i in range(len(cities)):
#     print(i,cities[i])

# expenses = [15000, 22000, 10000, 18000, 25000, 12000, 20000]
# jami=0

# for expens in expenses:
#     jami=expens+jami
# print(jami)


# 16. Do‘kon cheki
# products = ["Non", "Sut", "Olma", "Tuxum"]
# prices = [4000, 12000, 15000, 3000]
# for yordamida har bir mahsulot nomi va narxini
# bitta qatorda chiqaring.
# Oxirida barcha mahsulotlarning umumiy narxini hisoblang.
# Mahsulot va narx indekslari bir-biriga mos bo‘lsin.
# products = ["Non", "Sut", "Olma", "Tuxum"]
# prices = [4000, 12000, 15000, 3000]
# tolov=0
# for i in range(len(products)):
#     print(f"{products[i]}-{prices[i]}")
#     tolov+=prices[i]
# print(f"Sizdan {tolov} so'm")    
    

# 17. O‘quvchilar natijalari
# names = ["Ali", "Vali", "Malika", "Aziza"]
# scores = [78, 92, 85, 96]
# Har bir o‘quvchining ismi va ballini bitta qatorda chiqaring.
# for yordamida barcha ballarning yig‘indisini hisoblang.
# So‘ng o‘rtacha ballni aniqlang.


# 18. Kunlik daromad hisoboti
# income = [120000, 150000, 90000, 180000, 130000, 200000, 160000]
# Har bir kunning daromadini tartib raqami bilan chiqaring.
# for yordamida haftalik jami daromadni hisoblang.
# Keyin o‘rtacha kunlik daromadni aniqlang.


# 19. Mahsulotlar miqdori
# products = ["Non", "Sut", "Olma", "Guruch"]
# quantities = (20, 12, 30, 8)
# Har bir mahsulot nomini va uning miqdorini alohida qatorda chiqaring.
# Oxirida barcha mahsulotlarning umumiy miqdorini hisoblang.


# 20. Bir nechta ko‘paytirish jadvali
# numbers = [2, 3, 4]
# Ichma-ich for yordamida 2, 3 va 4 sonlarining
# har biri uchun 1 dan 5 gacha ko‘paytirish jadvalini chiqaring.
# numbers = [2, 3, 4]
# sonlar=list(range(1,5))
# for son in sonlar:
#     for number in numbers:
#         print(son*number)


# 21. Matn tahlili
# word = "PROGRAMMING"
# for yordamida matndagi har bir harfni alohida qatorda chiqaring.
# Keyin len() yordamida matndagi jami belgilar sonini aniqlang.


# 22. Tuple ichidagi ballar
# scores = (15, 18, 20, 12, 17, 19)
# Tuple ichidagi barcha ballarni for yordamida qo‘shing.
# Umumiy yig‘indini va o‘rtacha ballni hisoblang.
# Tuple'ni listga aylantirmang.


# 23. Ombor hisoboti
# products = ["Klaviatura", "Sichqoncha", "Monitor"]
# prices = [150000, 80000, 1200000]
# quantities = [10, 15, 4]
# Har bir mahsulot uchun narxni miqdorga ko‘paytirib,
# uning ombordagi umumiy qiymatini chiqaring.
# Oxirida barcha mahsulotlarning umumiy qiymatini hisoblang.


# 24. Shaharlarni teskari chiqarish
# cities = ["Toshkent", "Samarqand", "Buxoro", "Xiva", "Andijon"]
# for va range() yordamida shaharlarni ro‘yxatning
# oxiridan boshiga qarab chiqaring.
# Boshlang‘ich ro‘yxatni o‘zgartirmang.


# 25. Kurslar va kreditlar
# courses = (("Python", 3), ("SQL", 2), ("English", 4), ("Math", 5))
# Ichma-ich tuple ichidan har bir kurs nomi va kredit sonini
# indekslar yordamida chiqaring.
# So‘ng for yordamida jami kreditlar sonini hisoblang.


# 26. Oylik budjet
# expenses = [18000, 25000, 12000, 30000, 22000, 15000, 28000]
# for yordamida haftalik xarajatlar yig‘indisini hisoblang.
# O‘rtacha kunlik xarajatni aniqlang.
# Keyin har bir kunlik xarajat bilan o‘rtacha xarajat
# orasidagi farqni hisoblab chiqaring.


# 27. Tartibli savat hisoboti
# products = ["Daftar", "Ruchka", "Kitob", "Sumka", "Qalam"]
# prices = [8000, 3000, 45000, 180000, 5000]
# range() va len() yordamida har bir mahsulotning tartib raqami,
# nomi va narxini chiqaring.
# Oxirida barcha narxlarning umumiy summasini hisoblang.


# 28. Harflarning takrorlanishi
# text = "banana"
# Matndagi har bir belgini va uning matnda necha marta
# uchrashini count() yordamida chiqaring.
# Hozircha if-else ishlatmang.
# Bir xil harflar bir necha marta chiqarilishi mumkin.


# 29. Sotuv hisoboti
# products = ["Non", "Sut", "Sharbat"]
# prices = [4000, 12000, 10000]
# sold = [50, 20, 15]
# Har bir mahsulot uchun sotilgan miqdorni narxga
# ko‘paytirib, tushumni hisoblang.
# Har bir mahsulot tushumini alohida chiqaring.
# Oxirida jami tushumni hisoblang.


# 30. Mini-loyiha: Talabalar hisoboti
# students = ["Ali", "Malika", "Sardor", "Aziza", "Vali"]
# scores = [75, 92, 68, 88, 95]
# for yordamida har bir talabaning ismi, balli va foizini chiqaring.
# Maksimal ball 100 ga teng.
# Keyin barcha ballarning yig‘indisini va o‘rtacha ballni hisoblang.
# Barcha natijalar tartib bo‘yicha to‘g‘ri mos kelishi kerak.
# if-else ishlatmang.

# products = ["Non", "Sut", "Olma", "Tuxum"]
# prices = [4000, 12000, 15000, 3000]
# for i in range(len(products)):
#     print(f"{products[i]}-- {prices[i]}")

# names = ["Ali", "Vali", "Malika", "Aziza"]
# scores = [78, 92, 85, 96]
# for i in range(len(names)):
#     print(f"{names[i]} ning bali {scores[i]}")
# a=max(scores)
# x=scores.index(a)    
# print(f"1-o'rinni {names[x]} qo'lga kiritdi ")

# income = [120000, 150000, 90000, 180000, 130000, 200000, 160000]
# week=['Dushanba','Seshanba','Chorshanba','Payshanba','Juma','Shanba','Yakshanba']
# for i in range(len(income)):
#     print(f"{week[i]}={income[i]}")
# print(f"{sum(income)/len(income)} average expence for one day")

# products = ["Non", "Sut", "Olma", "Guruch"]
# quantities = (20, 12, 30, 8)
# for i in range(len(products)):
#     print(f"{products[i]}-{quantities[i]} dona ")
# print(f"Barcha mahsulotlar soni-{sum(quantities)}")    
















    