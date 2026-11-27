# # 1. Quyidagi lug‘atdan Azizaning Python ballini chiqaring.
# students = {
#     "Aziza": {"Python": 90, "SQL": 85},
#     "Ali": {"Python": 75, "SQL": 80}
# }
# for ism,ball in students.items():
#     if ism=='Aziza':
#         for k,q in ball.items():
#             if k=="Python":
#                 print(q)

# # 2. Ali ning SQL ballini chiqaring.
# students = {
#     "Aziza": {"Python": 90, "SQL": 85},
#     "Ali": {"Python": 75, "SQL": 80}
# }
# print(students["Ali"]["SQL"])
# # 3. Quyidagi lug‘atdan barcha talabalar ismlarini chiqaring.
# students = {
#     "Aziza": {"Python": 90},
#     "Ali": {"Python": 75},
#     "Vali": {"Python": 88}
# }
# for ism in students:
#     print(ism)

# # 4. Azizaning barcha fanlari va ballarini chiqaring.
# students = {
#     "Aziza": {"Python": 90, "SQL": 85, "Matematika": 80}
# }
# for k,q in students.items():
#     for key, value in q.items():
#         print(key,'-',value)


# # 5. Har bir talabaning Python ballini chiqaring.
# students = {
#     "Aziza": {"Python": 90, "SQL": 85},
#     "Ali": {"Python": 75, "SQL": 80},
#     "Vali": {"Python": 88, "SQL": 92}
# }
# for k,q in students.items():
#     for fan,ball in q.items():
#         if fan=="Python":
#             print(ball)


# # 6. Har bir talabaning barcha fanlari va ballarini chiqaring.
# students = {
#     "Aziza": {"Python": 90, "SQL": 85},
#     "Ali": {"Python": 75, "SQL": 80}
# }
# for key,value in students.items():
#     print(f"\n{key}")
#     for fan,ball in value.items():
#         print(fan,'-',ball)


# # 7. Quyidagi mahsulotlardan olma narxini chiqaring.
# shop = {
#     "mevalar": {"olma": 12000, "banan": 18000},
#     "ichimliklar": {"suv": 3000, "sharbat": 10000}
# }
# for key,value in shop.items():
#     for k,q in value.items():
#         if k=="olma":
#             print(k,q)
# print(shop["mevalar"]["olma"])


# # 8. Ichimliklar bo‘limidagi barcha mahsulotlarni chiqaring.
# shop = {
#     "mevalar": {"olma": 12000, "banan": 18000},
#     "ichimliklar": {"suv": 3000, "sharbat": 10000}
# }
# for k,q in shop.items():
#     if k=="ichimliklar":
#         for key,value in q.items():
#             print(key,'-',value)



# # 9. Har bir bo‘limdagi mahsulotlar va narxlarni chiqaring.
# shop = {
#     "mevalar": {"olma": 12000, "banan": 18000},
#     "ichimliklar": {"suv": 3000, "sharbat": 10000}
# }
# for k,q in shop.items():
#     print(f"\n{k}")
#     for key,value in q.items():
#         print(key,'-',value)


# # 10. Quyidagi lug‘atdan Toshkent shahridagi aholi sonini chiqaring.
# countries = {
#     "O‘zbekiston": {"poytaxt": "Toshkent", "aholi": 37000000},
#     "Qozog‘iston": {"poytaxt": "Astana", "aholi": 20000000}
# }
# for key,value in countries.items():
#     if key=="O‘zbekiston":
#         for k,q in value.items():
#             if q=="Toshkent":
#                 print(q,'=',value["aholi"])

# # 11. Har bir davlatning poytaxtini chiqaring.
# countries = {
#     "O‘zbekiston": {"poytaxt": "Toshkent", "aholi": 37000000},
#     "Qozog‘iston": {"poytaxt": "Astana", "aholi": 20000000}
# }
# for k,q in countries.items():
#     for key,value in q.items():
#         if key=="poytaxt":
#             print(value)


# # 12. Har bir o‘quvchining baholari ro‘yxatini chiqaring.
# students = {
#     "Aziza": {"baholar": [5, 4, 5]},
#     "Ali": {"baholar": [4, 3, 5]}
# }
# for k,q in students.items():
#     print(f"{k} ning baholari {q["baholar"]}")

# # 13. Azizaning baholari ro‘yxatidagi birinchi bahoni chiqaring.
# students = {
#     "Aziza": {"baholar": [5, 4, 5]},
#     "Ali": {"baholar": [4, 3, 5]}
# }
# for k,q in students.items():
#     if k=="Aziza":
#         for key,value in q.items():
#             print(value[0])

# # 14. Quyidagi ro‘yxatdagi har bir mahsulot nomini chiqaring.
# products = [
#     {"nom": "Noutbuk", "narx": 7000000},
#     {"nom": "Telefon", "narx": 3000000},
#     {"nom": "Planshet", "narx": 2500000}
# ]
# for maxsulot in products:
#     for k,q in maxsulot.items():
#         if k=="nom":
#             print(q)
# print(maxsulot['nom'])
    

# # 15. Har bir mahsulot nomi va narxini chiqaring.
# products = [
#     {"nom": "Noutbuk", "narx": 7000000},
#     {"nom": "Telefon", "narx": 3000000},
#     {"nom": "Planshet", "narx": 2500000}
# ]
# for maxsulot in products:
#     for q in maxsulot.values():
#         print(q)

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
# "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
# mashxur_shaxslar=[
#     {'Anvar Narullayev':'AI mutaxasis','unvon':'PHD sohibi','t_yil':1992},
#     {"Azim Pulat":"Kuchli dasturchi",'unvon':'FANG kampaniyada ishlagan','t_yil':2000},
#     {"Ergashev :Doniyor":"AI mutaxasis ",'unvon':'Ko\'plab kampaniyalar egasi','t_yil':2007}
  
# ]
# for shaxslar in mashxur_shaxslar:
#     print()
#     for k,q in shaxslar.items():
#         print(f"{k}-{q}")


# mashxur_shaxslar=[
#     {'ism':'Anvar Narullayev','job':'AI mutaxasis','unvon':'PHD sohibi','t_yil':1992,'proect':"Mohirdev"},
#     {'ism':"Azim Pulat",'job':"Kuchli dasturchi",'unvon':'FANG kampaniyada ishlagan','t_yil':2000,'proect':"42.uz"},
#     {'ism':"Ergashev :Doniyor",'job':"AI mutaxasis ",'unvon':'Ko\'plab kampaniyalar egasi','t_yil':2007,'proect':"Big database"}
# ]  
# for shaxslar in mashxur_shaxslar:
#     for k,q in shaxslar.items():
#         if k=="ism" or k=='proect':
#             print(k,'-',q)

# kinolar={"Ali":['Merlin','Prison break','Ashka'],
#          'Vali':['Sariq devni minib','Ashka','Prison break'],
#          'G\'ani':['Baliq ovi','Otalar sozi','Sariq devni minib']
#          }
# for k,q in kinolar.items():
#     print(f"\n{k}")
#     for kino in q:
#         print(kino)
davlatlar={"O'zbekiston":{"poytaxt":"Toshkent","aholi":"44mln","til":"Uzbek"},
          "Turkiya":{'poytaxt':'Boku','aholi':'58mln','til':'turk'},   
          'Qozg\'iston':{'poytaxt':'Astana','aholi':'20mln','til':'qozoqcha'}
    }
for key,value in davlatlar.items():
    for k,q in value.items():
       print(f"{key}={k,q}")










