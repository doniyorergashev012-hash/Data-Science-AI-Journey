# otam (onam, akam, ukam, va hokazo) degan lug'at yarating
# va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.


# otam={"ismi":"Shavkat",'familiya':'Baratov',"tugilgan_yili":1974,'manzil':'Jizzax','tuman':'Mirzachol tumani'}
# print(f" {otam["ismi"]} {otam['familiya']}, {otam['tugilgan_yili']}-yilda tug'ilgan ,yashash manzili {otam['manzil']}")

# taomlar={}
# for i in range(5):
#     ism=input('Ismingizni kiriting:').lower().title()
#     taom=input("Sevimli taomingizni kiriting:")
#     taomlar[ism]=taom
# for k,q in taomlar.items():
#     print(f"{k} ning sevimli taomi {q}") 

# types={'str':"matn ko'rinishdagi ma'lumotlar","int":"Butun son","float":"Kasr sonlar",'dict':'Lugat'}   
# savol=input("Nima xolavosan?")
# javob=types.get(savol,"Natija topilmadi")
# print(javob)

# types={'str':"matn ko'rinishdagi ma'lumotlar","int":"Butun son","float":"Kasr sonlar",'dict':'Lugat'}   
# savol=input("Nima xolavosan?")
# if savol in types.keys():
#     print(types[savol])
# else:
#     print("Bunday natija topilmadi")    

# types={'str':"matn ko'rinishdagi ma'lumotlar","int":"Butun son","float":"Kasr sonlar",'dict':'Lugat'}
# for k,q  in types.items():
#     print(k,'-',q)

# countries={"Uzbekiston":"Toshkent","Qozog'iston":"Almata","Britaniya":"Angilya","Turkiya":"Istanbul"}
# for davlat,poytaxt in sorted(countries.items()):
#     print(davlat,"-",poytaxt)
# countries={"Uzbekiston":"Toshkent","Qozog'iston":"Almata","Britaniya":"Angilya","Turkiya":"Istanbul"}
# davlat=input("Davlat nomi:")
# for k,q in sorted(countries.items()):
#     if davlat==k:
#         print(f"{k} ning poytaxti {q}")
#         break
# else:
#     print("Bizda bunday davlat yoq")
# buturtmalar=[]
# menu={'shashlik':25000,
#       'somsa':42000,
#       'lagmon':20000,
#       'tandir':250000,
#       'lavash':40000,
#       'burger':30000,
#       'cola':15000
# }
# for i in range(3):
#     buyurtma=input(f"{i+1}-buyurtma:")
#     buturtmalar.append(buyurtma)
# for taom in menu.keys():
#     if taom in buturtmalar:
#         print(f"{taom}-{menu[taom]} so'm")
# for zakas in buturtmalar:
#     if zakas not in menu:
#         print(f"Kechirasiz bizda {zakas} qolmagan")
    


# 1. Lug‘atni chiqarish
# student = {
#     "ism": "Ali",
#     "yosh": 19,
#     "kurs": 1
# }
# Lug‘atni ekranga chiqaring.
# student = {
#     "ism": "Ali",
#     "yosh": 19,
#     "kurs": 1
# }
# print(student)

# 2. Ismni olish
# student = {
#     "ism": "Malika",
#     "yosh": 20,
#     "shahar": "Toshkent"
# }
# Lug‘atdan ismni alohida chiqaring.



# 3. Bir nechta qiymatni chiqarish
# car = {
#     "model": "Malibu",
#     "rang": "oq",
#     "yil": 2024
# }
# Mashinaning modeli, rangi va yilini alohida chiqaring.

# 4. Lug‘atdagi qiymatni o‘zgartirish
# phone = {
#     "model": "Samsung A10",
#     "narx": 1000000
# }
# Telefon narxini 1200000 ga o‘zgartiring.
# Yangilangan lug‘atni chiqaring.

# 5. Yangi kalit qo‘shish
# student = {
#     "ism": "Sardor",
#     "yosh": 18
# }
# Lug‘atga "fakultet": "AI" kalit-qiymatini qo‘shing.
# Yangilangan lug‘atni chiqaring.

# 6. Lug‘at uzunligi
# countries = {
#     "UZ": "O‘zbekiston",
#     "US": "AQSH",
#     "TR": "Turkiya",
#     "KR": "Janubiy Koreya"
# }
# Lug‘atda nechta element borligini len() bilan aniqlang.

# 7. Barcha kalitlarni chiqarish
# laptop = {
#     "model": "Asus Vivobook",
#     "ram": 16,
#     "ssd": 512,
#     "narx": 6500000
# }
# Lug‘atdagi barcha kalitlarni keys() yordamida chiqaring.

# 8. Barcha qiymatlarni chiqarish
# laptop = {
#     "model": "Asus Vivobook",
#     "ram": 16,
#     "ssd": 512,
#     "narx": 6500000
# }
# Lug‘atdagi barcha qiymatlarni values() yordamida chiqaring.

# 9. Kalit va qiymatlarni chiqarish
# student = {
#     "ism": "Aziza",
#     "yosh": 19,
#     "kurs": 1
# }
# items() va for yordamida har bir kalit va qiymatni chiqaring.

# 10. Lug‘atdagi qiymatlarni hisoblash
# prices = {
#     "non": 4000,
#     "sut": 12000,
#     "olma": 15000
# }
# for yordamida barcha narxlar yig‘indisini hisoblang.
# sum() ishlatmang.

# 11. Mahsulot narxini yangilash
# products = {
#     "non": 4000,
#     "sut": 12000,
#     "tuxum": 3000
# }
# "sut" narxini 14000 ga o‘zgartiring.
# Natijani chiqaring.

# 12. Yangi fan qo‘shish
# scores = {
#     "Python": 85,
#     "SQL": 90
# }
# Lug‘atga "Matematika": 78 elementini qo‘shing.

# 13. Elementni o‘chirish
# student = {
#     "ism": "Vali",
#     "yosh": 20,
#     "shahar": "Buxoro"
# }
# pop() yordamida "shahar" elementini o‘chiring.
# Yangilangan lug‘atni chiqaring.

# 14. Lug‘atni nusxalash
# original = {
#     "ism": "Ali",
#     "yosh": 19
# }
# copy() yordamida lug‘atdan nusxa oling.
# Nusxada yoshni 20 ga o‘zgartiring.
# Ikkala lug‘atni chiqaring.

# 15. Lug‘atdagi sonlar
# numbers = {
#     "birinchi": 15,
#     "ikkinchi": 25,
#     "uchinchi": 10
# }
# for yordamida qiymatlarni qo‘shib,
# umumiy yig‘indini hisoblang.


# student = {
#     "ism": "Ali",
#     "yosh": 19,
#     "kurs": 1
# }
# print(student)

# student = {
#     "ism": "Malika",
#     "yosh": 20,
#     "shahar": "Toshkent"
# }
# a=student.get('ism')
# print(a)


# car = {
#     "model": "Malibu",
#     "rang": "oq",
#     "yil": 2024
# }
# print(f"modeli-{car['model']},rangi-{car['rang']},yili--{car['yil']}")

# phone = {
#     "model": "Samsung A10",
#     "narx": 1000000
# }
# phone["narx"]=1200000
# print(phone)

# student = {
#     "ism": "Sardor",
#     "yosh": 18
# }

# student["fakultet"]="Raqamli iqtisodiyot"
# print(student)



# countries = {
#     "UZ": "O‘zbekiston",
#     "US": "AQSH",
#     "TR": "Turkiya",
#     "KR": "Janubiy Koreya"
# }
# print(len(countries))



# laptop = {
#     "model": "Asus Vivobook",
#     "ram": 16,
#     "ssd": 512,
#     "narx": 6500000
# }


# laptop = {
#     "model": "Asus Vivobook",
#     "ram": 16,
#     "ssd": 512,
#     "narx": 6500000
# }
# print("Noutbook ma'lumotlari:")
# for key,value in laptop.items():
#     print(key,'-',value)

# student = {
#     "ism": "Aziza",
#     "yosh": 19,
#     "kurs": 1
# }
# for k,q in student.items():
#     print(f"Kalit:{k}")
#     print(f"Qiymat:{q} \n")

# prices = {
#     "non": 4000,
#     "sut": 12000,
#     "olma": 15000
# }
# print("Xarid qilingan maxsulotlar")
# shot=0
# for k,q in prices.items():
#     print(k,'-',q)
#     shot=shot+q
# print(f"Sizning tolov miqdoringiz:{shot}\nAgar 1% keshbek kerak bolsa QR kodni skanerlang!")    
    

# products = {
#     "non": 4000,
#     "sut": 12000,
#     "tuxum": 3000
# }
# products['sut']=14000
# print(products)


# scores = {
#     "Python": 85,
#     "SQL": 90
# }
# umumiy_ball=0
# scores["Matematika"]=95
# for fan,ball in scores.items():
#     print(fan,'=',ball)
#     umumiy_ball+=ball    
# average=umumiy_ball/len(scores)
# if average<=70:
#     baho=3
# elif average<=80:
#     baho=4
# elif average>=90:
#     baho=5
# print(f"Siznign o'rgacha balingiz={average}")    
# print(f"Yakuniy baho={baho}")

# student = {
#     "ism": "Vali",
#     "yosh": 20,
#     "shahar": "Buxoro"
# }
# del student["shahar"]
# print(student)

# original = {
#     "ism": "Ali",
#     "yosh": 19
# }
# x=original.copy()
# x['yosh']=20
# print(original)
# print(x)

# numbers = {
#     "birinchi": 15,
#     "ikkinchi": 25,
#     "uchinchi": 10
# }
# jami=0
# for q in numbers.values():
#     jami+=q
# print(jami)    

# 16. Talaba ma’lumotlari
# student = {
#     "ism": "Malika",
#     "yosh": 19,
#     "kurs": 1,
#     "yonalish": "Artificial Intelligence"
# }
# Har bir kalit va qiymatni alohida qatorda chiqaring.

# student = {
#     "ism": "Malika",
#     "yosh": 19,
#     "kurs": 1,
#     "yonalish": "Artificial Intelligence"
# }
# for k,q in student.items():
#     print(f"Key:{k}")
#     print(f"Value:{q}\n")


# 17. Do‘kon cheki
# products = {
#     "non": 4000,
#     "sut": 12000,
#     "olma": 15000,
#     "tuxum": 3000
# }
# for yordamida barcha narxlarni qo‘shing.
# Mahsulotlar narxlari va umumiy summani chiqaring.
# products = {
#     "non": 4000,
#     "sut": 12000,
#     "olma": 15000,
#     "tuxum": 3000
# }
# jami=0
# print("Sizning maxsulotlar:")
# for k,q in products.items():
#     print(k,'-',q)
#     jami+=q
# print(f"Sizning tolov summangiz:{jami}")
# print("Agar 1% miqdorda qatrim kerak bolsa, Iltimos QR kodni skanerlang")


# 18. Fanlar va ballar
# scores = {
#     "Python": 85,
#     "SQL": 92,
#     "Matematika": 78,
#     "Ingliz tili": 88
# }
# Har bir fan va uning balini chiqaring.
# Ballarning umumiy yig‘indisini hisoblang.

# scores = {
#     "Python": 34,
#     "SQL": 62,
#     "Matematika":50,
#     "Ingliz tili": 70
# }
# umumiy_ball=0
# for k,q in scores.items():
#     print(k,'-',q)
#     umumiy_ball+=q
# if umumiy_ball/len(scores)<=59:
#     baho=2
#     print("Siz yiqildingiz!\n")
# elif umumiy_ball/len(scores)<=70:
#     baho=3
# elif umumiy_ball/len(scores)<90:
#     baho=4
# elif umumiy_ball/len(scores)<=100:
#     baho=5
# print(f"O'rtacha ball={umumiy_ball/len(scores)}")
# print(f"Sizning bahoyingiz={baho}")
    

# 19. Mahsulotlar ombori
# stock = {
#     "non": 20,
#     "sut": 12,
#     "olma": 30,
#     "tuxum": 8
# }
# Barcha mahsulotlarning umumiy miqdorini hisoblang.
# Har bir mahsulot nomi va miqdorini chiqaring.

# 20. Shaharlar lug‘ati
# cities = {
#     "Toshkent": 3000000,
#     "Samarqand": 600000,
#     "Buxoro": 300000
# }
# Har bir shahar nomi va aholi sonini chiqaring.
# Aholi sonlarining yig‘indisini hisoblang.

# 21. Xodimlar maoshi
# salaries = {
#     "Ali": 4000000,
#     "Malika": 5500000,
#     "Sardor": 4800000
# }
# Barcha xodimlarning maoshlarini qo‘shing.
# O‘rtacha maoshni hisoblang.

# 22. Savdo hisoboti
# sales = {
#     "dushanba": 150000,
#     "seshanba": 200000,
#     "chorshanba": 175000,
#     "payshanba": 250000
# }
# Har bir kun savdosini chiqaring.
# Umumiy savdo summasini hisoblang.

# 23. Mahsulot narxini o‘zgartirish
# prices = {
#     "klaviatura": 150000,
#     "sichqoncha": 80000,
#     "monitor": 1200000
# }
# Barcha mahsulotlar narxini 10% ga oshiring.
# Yangilangan narxlarni chiqaring.

# 24. Lug‘atdagi qiymatlarni ikki baravar qilish
# numbers = {
#     "a": 5,
#     "b": 10,
#     "c": 15,
#     "d": 20
# }
# for yordamida har bir qiymatni ikki baravar qiling.
# Yangilangan qiymatlarni lug‘atga yozing.

# 25. Talabaning umumiy natijasi
# student = {
#     "ism": "Aziza",
#     "Python": 90,
#     "SQL": 85,
#     "Matematika": 80
# }
# Fanlar ballarini qo‘shing.
# O‘rtacha ballni hisoblab chiqaring.
# "ism" qiymatini ballar yig‘indisiga qo‘shmang.

# 26. Valyuta qiymatlari
# currency = {
#     "USD": 12500,
#     "EUR": 13500,
#     "RUB": 140
# }
# Har bir valyuta nomi va qiymatini chiqaring.
# Har bir qiymatni 2 ga ko‘paytirib, alohida chiqaring.

# 27. Lug‘atni to‘ldirish
# student = {
#     "ism": "Sardor",
#     "yosh": 18
# }
# Quyidagi elementlarni qo‘shing:
# "kurs": 1
# "yonalish": "AI"
# "shahar": "Toshkent"
# Yakuniy lug‘atni chiqaring.

# 28. Mahsulot va sotilgan miqdor
# sold = {
#     "non": 50,
#     "sut": 20,
#     "sharbat": 15
# }
# Har bir mahsulot va sotilgan miqdorni chiqaring.
# Umumiy sotilgan mahsulotlar sonini hisoblang.

# 29. Haftalik xarajatlar
# expenses = {
#     "dushanba": 18000,
#     "seshanba": 25000,
#     "chorshanba": 12000,
#     "payshanba": 30000,
#     "juma": 22000
# }
# Umumiy xarajat va o‘rtacha xarajatni hisoblang.
# Har bir kunning xarajatini ham chiqaring.

# 30. Mini-loyiha: Universitet ma’lumotlari
# university = {
#     "nomi": "TDIU",
#     "talabalar_soni": 20000,
#     "fakultetlar_soni": 10,
#     "yonalish": "Artificial Intelligence"
# }
# Barcha kalit va qiymatlarni chiqaring.
# Lug‘atga "shahar": "Toshkent" elementini qo‘shing.
# Talabalar sonini 21000 ga yangilang.
# Yakuniy lug‘atni chiqaring.

# student = {
#     "ism": "Malika",
#     "yosh": 19,
#     "kurs": 1,
#     "yonalish": "Artificial Intelligence"
# }
# for k,q in student.items():
#     print(k,'-',q)
   

# products = {
#     "non": 4000,
#     "sut": 12000,
#     "olma": 15000,
#     "tuxum": 3000
# }
# hisobot=0
# print("Siz xarid qilgan maxsulotlar:")
# for k,q in products.items():
#     print(k,'-',q)
#     hisobot+=q
# print(f"Siznig tolov miqdoringiz={hisobot}")


# 18. Fanlar va ballar
# scores = {
#     "Python": 85,
#     "SQL": 92,
#     "Matematika": 78,
#     "Ingliz tili": 88
# }
# Har bir fan va uning balini chiqaring.
# Ballarning umumiy yig‘indisini hisoblang.


# scores = {
#     "Python": 85,
#     "SQL": 92,
#     "Matematika": 78,
#     "Ingliz tili": 88
# }
# jami=0
# for fan,ball in scores.items():
#     print(fan,'-',ball)
#     jami+=ball
# print(f"Jami ball={jami}, O'rtacha ball={jami/len(scores)}")


# 23. Mahsulot narxini o‘zgartirish
# prices = {
#     "klaviatura": 150000,
#     "sichqoncha": 80000,
#     "monitor": 1200000
# }
# Barcha mahsulotlar narxini 10% ga oshiring.
# Yangilangan narxlarni chiqaring.


# prices = {
#     "klaviatura": 150000,
#     "sichqoncha": 80000,
#     "monitor": 1200000
# }
# for k,q in prices.items():
#     prices[k]=q+q*0.1
# print(prices)

# 24. Lug‘atdagi qiymatlarni ikki baravar qilish
# numbers = {
#     "a": 5,
#     "b": 10,
#     "c": 15,
#     "d": 20
# }
# for yordamida har bir qiymatni ikki baravar qiling.
# Yangilangan qiymatlarni lug‘atga yozing.

# numbers = {
#     "a": 5,
#     "b": 10,
#     "c": 15,
#     "d": 20
# }
# for k,q in numbers.items():
#     numbers[k]=q*2
# print(numbers)


# 25. Talabaning umumiy natijasi
# student = {
#     "ism": "Aziza",
#     "Python": 90,
#     "SQL": 85,
#     "Matematika": 80
# }
# Fanlar ballarini qo‘shing.
# O‘rtacha ballni hisoblab chiqaring.
# "ism" qiymatini ballar yig‘indisiga qo‘shmang.

# student = {
#     "ism": "Aziza",
#     "Python": 90,
#     "SQL": 85,
#     "Matematika": 80
# }
# umumiy_ball=0
# for fan,ball in student.items():
#     print(fan,'=',ball)
#     if type(ball)==int:      
#         umumiy_ball+=ball
# print(umumiy_ball)        
    

# 26. Valyuta qiymatlari
# currency = {
#     "USD": 12500,
#     "EUR": 13500,
#     "RUB": 140
# }
# Har bir valyuta nomi va qiymatini chiqaring.
# Har bir qiymatni 2 ga ko‘paytirib, alohida chiqaring.

# currency = {
#     "USD": 12500,
#     "EUR": 13500,
#     "RUB": 140
# }
# for k,q in currency.items():
#     currency[k]=q*2
#     print(k,'=',q)
# print(currency)















