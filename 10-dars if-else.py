# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=="gm":
#         print(car.upper())
#     else:
#         print(car.title())
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car!="gm":
#         print(car.title())
#     else:
#         print(car.upper())
# login=input("Iltimos login kiriting: ")
# if login=="Admin":
#     print(f"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {login}")
# print('2 ta son kiriting')
# sonlar = []
# for i in range(2):
#     son = int(input(f"{i+1}-son: "))
#     sonlar.append(son)
# if sonlar[0] == sonlar[1]:
#     print("Sonlar teng", sonlar)
# else:
#     print("Sonlar teng emas", sonlar)
# son=float(input("Istagan soningizni kirting:"))
# if son>0:
    
#     print('musbat')
# else:
#     print('manfiy')
# son=float(input("1 ta son kirting:"))
# if son>0:
#     print(son**0.5)
# else:
#     print("Musbat son kiriting:")

# 1. Musbat, manfiy yoki nol
# son = 15
# son musbat bo‘lsa "Musbat", manfiy bo‘lsa "Manfiy",
# nolga teng bo‘lsa "Nol" deb chiqaring.

# 2. Juft yoki toq
# son = 24
# Son juft yoki toq ekanligini if-else yordamida aniqlang.

# 3. Ikki sonni taqqoslash
# a = 25
# b = 18
# Qaysi son katta ekanligini aniqlang.
# Agar teng bo‘lsa, "Sonlar teng" deb chiqaring.

# 4. Yoshni tekshirish
# yosh = 17
# Yosh 18 yoki undan katta bo‘lsa "Ruxsat berildi",
# aks holda "Ruxsat berilmadi" deb chiqaring.

# 5. Imtihon natijasi
# ball = 76
# Ball 60 yoki undan yuqori bo‘lsa "O‘tdi",
# aks holda "Yiqildi" deb chiqaring.

# 6. Haroratni tekshirish
# harorat = 12
# Harorat 0 dan yuqori yoki teng bo‘lsa "Muzlash yo‘q",
# aks holda "Sovuq: harorat noldan past" deb chiqaring.

# 7. Chegirma
# narx = 150000
# Agar narx 100000 yoki undan yuqori bo‘lsa,
# 10% chegirma hisoblang.
# Aks holda chegirmasiz narxni chiqaring.

# 8. Parolni tekshirish
# parol = "python123"
# togri_parol = "python123"
# Parol to‘g‘ri bo‘lsa "Kirish mumkin",
# aks holda "Parol xato" deb chiqaring.

# 9. Sonning 10 dan kattaligini tekshirish
# son = 14
# Son 10 dan katta bo‘lsa "Katta",
# aks holda "10 dan katta emas" deb chiqaring.

# 10. Uch xonali sonni tekshirish
# son = 245
# Son 100 dan 999 gacha bo‘lsa "Uch xonali son",
# aks holda "Uch xonali son emas" deb chiqaring.

# 11. Ikki sonning yig‘indisi
# a = 12
# b = 8
# Yig‘indi 20 ga teng bo‘lsa "Yig‘indi 20",
# aks holda "Yig‘indi 20 emas" deb chiqaring.

# 12. Mahsulot narxi
# narx = 45000
# Narx 50000 dan kam bo‘lsa "Arzonroq mahsulot",
# aks holda "Qimmatroq mahsulot" deb chiqaring.

# 13. Ro‘yxat uzunligi
# names = ["Ali", "Vali", "Malika", "Aziza"]
# Ro‘yxatda 3 tadan ko‘p ism bo‘lsa "Ko‘p ismlar",
# aks holda "Ismlar soni 3 ta yoki undan kam" deb chiqaring.

# 14. Matnni tekshirish
# word = "Python"
# Agar matn uzunligi 5 dan katta bo‘lsa "Uzun so‘z",
# aks holda "Qisqa so‘z" deb chiqaring.

# 15. Sonni 3 ga bo‘linishini tekshirish
# son = 27
# Son 3 ga qoldiqsiz bo‘linsa "3 ga bo‘linadi",
# aks holda "3 ga bo‘linmaydi" deb chiqaring.

# son = 15
# if son>0:
#     print("Musbat")
# elif son<0:
#     print("manfiy")
# else:
#     print("0 ga teng")
# son = 24
# if son%2==0:
#     print("juft")
# else:
#     print("toq")

# x,y = 25,18
# print("x>y") if x>y else print("x<y")

# yosh=int(input('Yoshingizni kiriting:'))
# if yosh>=18:
#     print("Kirishga ruxsat bor")
# else:
#     print('Yoshingizni yetmaydi')

# ball = 76
# if ball>60:
#     print("o'tdi")
# else:
#     print("yiqildi")

# harorat = 12
# if harorat>=0:
#     print("Muzlash yoq")
# else:
#     print("Sovuq")

# narx = 150000
# if narx>=100000:
#     print(f"Sizda 10% chegirma qilib beramaiz {narx-narx*0.1}")
# else:
#     print("Hech qanday chegirma yoq") 
   
# parol =input("Parolni kiriting:")
# togri_parol = "python123"
# if parol==togri_parol:
#     print("Kirish mumkin")
# else:
#     print("Xato")

# son = 14
# if son>10:
#     print("Son 10 dan katta")
# else:
#     print("Son kichik")

# son = 245
# if son>=100 and son<=999:
#     print("Son 3 xonali")
# else:
#     print("Son 3 xonali emas")

# a,b = 12, 8
# if a+b==20:
#     print("Xa")
# else:
#     print("Yoq")

# narx = 45000
# if narx<50000:
#     print("Arzon maxsulot")
# else:
#     print("Qimmat maxsulot")


# names = ["Ali", "Vali", "Malika", "Aziza"]
# if len(names)>3:
#     print("True")
# else:
#     print('False')

# word = "Python"
# if len(word)>3:
#     print("True")
# else:
#     print('False')

# son = 29
# if son%3==0:
#     print("3 ga bo'linadi")
# else:
#     print("bo'linmaydi")

# 16. Eng katta son
# a = 35
# b = 72
# c = 48
# Uchta sondan eng kattasini if-else yordamida aniqlang.
# Hozircha faqat if-else ishlating, elif mavzusini ishlatmang.

# 17. Ikki sonning tengligi
# a = 45
# b = 45
# Agar sonlar teng bo‘lsa "Teng",
# aks holda "Teng emas" deb chiqaring.

# 18. Chegirmali do‘kon
# narx = 240000
# Agar narx 200000 yoki undan yuqori bo‘lsa,
# 15% chegirma qo‘llang.
# Yakuniy narxni chiqaring.
# Aks holda asl narxni chiqaring.

# 19. Talabaning natijasi
# ball = 85
# Agar ball 86 yoki undan yuqori bo‘lsa "A'lo",
# aks holda "A'lo daraja emas" deb chiqaring.

# 20. Elektron hamyon
# balans = 100000
# xarid = 75000
# Balans xarid uchun yetarli bo‘lsa, qolgan pulni hisoblang.
# Aks holda "Mablag‘ yetarli emas" deb chiqaring.

# 21. Yetkazib berish
# buyurtma_narxi = 180000
# Agar buyurtma 150000 yoki undan yuqori bo‘lsa,
# yetkazib berish bepul.
# Aks holda yetkazib berish narxi 15000 so‘m.
# Jami to‘lovni chiqaring.

# 22. Ishga kechikish
# kelish_vaqti = 8
# Agar kelish vaqti 9 dan kichik bo‘lsa "Vaqtida keldi",
# aks holda "Kechikdi" deb chiqaring.
# Vaqt soat bilan berilgan deb oling.

# 23. Ombordagi mahsulot
# mahsulot_soni = 0
# Mahsulot soni 0 dan katta bo‘lsa "Mavjud",
# aks holda "Tugagan" deb chiqaring.

# 24. Parol uzunligi
# parol = "python2026"
# Parol uzunligi 8 yoki undan ko‘p bo‘lsa "Parol yetarli",
# aks holda "Parol juda qisqa" deb chiqaring.

# 25. Ikki fanning umumiy bali
# python_balli = 78
# sql_balli = 82
# Umumiy ballni hisoblang.
# Umumiy ball 150 yoki undan yuqori bo‘lsa "Yaxshi natija",
# aks holda "Ko‘proq tayyorlanish kerak" deb chiqaring.

# 26. Sayohat budjeti
# budjet = 500000
# chipta = 180000
# mehmonxona = 250000
# Chipta va mehmonxona xarajatlari yig‘indisini hisoblang.
# Budjet yetarli bo‘lsa qolgan pulni,
# aks holda yetishmayotgan pulni chiqaring.

# 27. Do‘kon cheki
# products = ["Non", "Sut", "Olma"]
# prices = [4000, 12000, 15000]
# jami = 0
# for yordamida umumiy narxni hisoblang.
# Jami 30000 yoki undan yuqori bo‘lsa "Katta xarid",
# aks holda "Kichik xarid" deb chiqaring.

# 28. Ro‘yxatdagi son
# numbers = [12, 25, 8, 41, 16]
# for yordamida har bir sonni tekshiring.
# Son 20 yoki undan yuqori bo‘lsa, uni chiqaring.
# Aks holda uni chiqarmang.
# Eslatma: if-else ichida faqat kerakli sonlarni chiqarish mumkin.

# 29. Talabalar ballari
# names = ["Ali", "Malika", "Sardor", "Aziza"]
# scores = [75, 92, 58, 88]
# for yordamida har bir talabaning ismi va balini chiqaring.
# Ball 60 yoki undan yuqori bo‘lsa "O‘tdi",
# aks holda "Yiqildi" deb chiqaring.
# Ism va ball indekslari mos bo‘lsin.

# 30. Bankomat
# balans = 500000
# yechish = 200000
# Agar balans yechiladigan pulga yetarli bo‘lsa,
# yangi balansni hisoblang.
# Aks holda "Mablag‘ yetarli emas" deb chiqaring.
# Yangi balansni natijada ko‘rsating.


# a = 35
# b = 72
# c = 48
# maxx=a
# if b>maxx:
#     maxx=b
# if c>maxx and c>b:
#     maxx=c
# print(maxx)    

# buyurtma_narxi = 180000
# if buyurtma_narxi>=150000:
#     print('Yetkazib berish bepul')
# else:
#     print(f"Yetkazib berish 15000 ming som+")    

# parol =input("Parol kiriting:")
# if len(parol)<=7:
#     print('Parol  eng kami 8 ta belgingan kop bolishi kerak' )
# else:
#     print("Xush kelibsiz") 

# python_balli = 78
# sql_balli = 82
# umumiy=sql_balli+python_balli
# if umumiy>=150:
#     print("Yaxshi natija")
# else:
#     print("Yaxshilab tayyorlanish kerak")

# budjet = 500000
# chipta = 180000
# mehmonxona = 250000
# expence=chipta+mehmonxona
# if budjet>=expence:
#     print(f"Pul yetarli,ortib qoladi{budjet-expence}")
# else:
#     print(f"Bizga {expence-budjet} summa yetmayabdi")

# products = ["Non", "Sut", "Olma"]
# prices = [4000, 12000, 15000]
# jami = 0
# for i in range(len(prices)):
#     print(f"{products[i]}-{prices[i]}")
# if sum(prices)>=30000:
#     print(f"Paket tekin,sizdan{sum(prices)}")    
# else:
#     print(f"sizdan{sum(pices)+500}") 
   
# numbers = [12, 25, 8, 41, 16]
# for son in numbers:
#     if son>=20:
#         print(son)
    
# names = ["Ali", "Malika", "Sardor", "Aziza"]
# scores = [75, 92, 58, 88]  
# for i in range(len(names)):
#     if scores[i]>=78:
#         print("O'tganlar ro'yxati")
#         print(f"{names[i]}-{scores[i]}")
# pinkod=1234
# parol=int(input('parolni kiriting:'))
# if parol==pinkod:
#      print("Xush kelibsiz")
#      yechish =int(input("Yechiladigan summani kiriting:"))
#      if yechish>100000:
#          print("foizsiz")
# else:
#      print("1% olib qolinadi")
    
    
    
    
    
    
    
    
    
    
    
    
    
