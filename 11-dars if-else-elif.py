# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son=int(input("Juft son kiriting:"))
# if son%2==0:
#     a="Raxmat"
# else:
#     a="Bu juft son emas"
# print(a)    
# print("Yoshingizga qarab chipta narxlari xar xil!")
# yosh=int(input("Iltimos yoshingizni kiriting:"))
# if yosh<=4 or yosh>=65:
#     narx=0
# elif yosh<=18:
#     narx=10000
# elif yosh>18:
#     narx=20000
# print(f"Siz uchun chipta narxi {narx} so'm")
# print("Iltimos 2 ta son kiriting!")
# sonlar=[]
# for i in range(2):
#     son=int(input(f"{i+1}-son kiriting:"))
#     sonlar.append(son)
# if sonlar[0]==sonlar[1]:
#     a="teng"
# elif sonlar[0]>sonlar[1]:   
#     a=f"{sonlar[0]}katta"
# elif sonlar[0]<sonlar[1]: 
#     a=f"{sonlar[1]}katta"
# print(a)    
# products=["olma","anor","non","qaymoq","tuxum","mandarin","makaron","saqich","coffe","pomidor"]   
# booked=[]
# for i in range(5):
#     savatcha=input(f"{i+1}-maxusolot:")
#     booked.append(savatcha)
# if booked:
#     for order in booked:
#         if order in products:
#             print(f"Bizda {order} bor ")
#         else:
#             print(f"Bizda {order} maxsuloti yoq")
# products=["olma","anor","non","qaymoq","tuxum","mandarin","makaron","saqich","coffe","pomidor"]   
# booked=[]
# bor_maxsulotlar=[]
# yoq_maxsulotlar=[]
# for i in range(5):
#     savatcha=input(f"{i+1}-maxusolot:")
#     booked.append(savatcha)
# if booked:
#     for order in booked:
#         if order in products:
#             bor_maxsulotlar.append(order)
#         else:
#             yoq_maxsulotlar.append(order)
# if yoq_maxsulotlar:
#     print(f"Bizda yo'q maxsulotlar ro'yxati-{yoq_maxsulotlar}")
#     print(f" bizdagi sizning shu maxsulotlaringiz bor-{bor_maxsulotlar}")    
# else:
#     print(f"Bizda sizga kerakli barcha maxsulotlar bor-{bor_maxsulotlar}")

# loginlar=["ergashev_1207","abduvali007","sardor_899","olmaxon99","okaxon45"]
# login=input("Login yarating:").lower()
# if login not in loginlar:
#     loginlar.append(login)
#     a="Xush kelibsiz"
# else:
#     a="Bu login allaqachon band"    
# print(a)
# sonlar=list(range(2,10))
# son=int(input("Son kiriting:"))
# for number in sonlar:
#     if son%number==0:
#         print(number)
# else:
#     print(f"Bu yerda bu  sonlar bor {sonlar}")


# 1. Sonning holati
# son = -8
# Son musbat bo‘lsa "Musbat", manfiy bo‘lsa "Manfiy",
# nolga teng bo‘lsa "Nol" deb chiqaring.
# if-elif-else ishlating.

# 2. Sonlarni taqqoslash
# a = 25
# b = 25
# Ikki son teng bo‘lsa "Teng",
# a katta bo‘lsa "Birinchi son katta",
# aks holda "Ikkinchi son katta" deb chiqaring.

# 3. Imtihon bahosi
# ball = 86
# 90–100: "A'lo"
# 70–89: "Yaxshi"
# 60–69: "Qoniqarli"
# 0–59: "Yiqildi"
# if-elif-else yordamida bahoni aniqlang.

# 4. Juft yoki toq va musbat yoki manfiy
# son = 17
# Son musbat va juft bo‘lsa "Musbat juft".
# Musbat va toq bo‘lsa "Musbat toq".
# Manfiy bo‘lsa "Manfiy son".
# Nol bo‘lsa "Nol".
# and va if-elif-else ishlating.

# 5. Harorat
# harorat = 28
# Harorat 0 dan past bo‘lsa "Sovuq".
# 0–15 oralig‘ida bo‘lsa "Salqin".
# 16–25 oralig‘ida bo‘lsa "Iliq".
# 25 dan yuqori bo‘lsa "Issiq".
# if-elif-else ishlating.

# 6. Yosh toifasi
# yosh = 19
# 0 dan kichik bo‘lsa "Noto‘g‘ri yosh".
# 0–12: "Bola"
# 13–17: "O‘smir"
# 18–59: "Katta yoshli"
# 60 va undan yuqori: "Keksa yosh"
# if-elif-else ishlating.

# 7. Chegirma hisoblash
# narx = 250000
# Narx 300000 yoki undan yuqori bo‘lsa 20% chegirma.
# Narx 150000 yoki undan yuqori bo‘lsa 10% chegirma.
# Aks holda chegirma berilmasin.
# Yakuniy narxni chiqaring.

# 8. Login va parol
# login = "admin"
# parol = "python123"
# togri_login = "admin"
# togri_parol = "python123"
# Login va parol ikkalasi to‘g‘ri bo‘lsa "Kirish mumkin".
# Aks holda "Login yoki parol xato".
# and ishlating.

# 9. Dam olish kuni
# kun = "shanba"
# Kun "shanba" yoki "yakshanba" bo‘lsa "Dam olish kuni".
# Aks holda "Ish kuni".
# or operatoridan foydalaning.

# 10. Sonning oraliqqa tegishliligi
# son = 45
# Son 10 dan 50 gacha, chegaralari bilan birga bo‘lsa
# "Oraliqda", aks holda "Oraliqdan tashqarida" deb chiqaring.
# and ishlating.
# son=40
# if son<=10 or son>50:
#     a="Oraliqdan tashqarida"
# elif son<=50:
#     a="Oraliqda"
# print(a)    


# 11. Uch xonali son
# son = 245
# Son 100–999 oralig‘ida bo‘lsa "Uch xonali musbat son".
# Son -999 dan -100 gacha bo‘lsa "Uch xonali manfiy son".
# Aks holda "Uch xonali son emas" deb chiqaring.
# son=-245
# if son>=100 and son<=999:
#     a="Uch xonali musbat son"
# elif son<=-100 and son>=-999:
#     a="Uch xonali manfiy son"
# else:
#     a="Uch xonali son emas"
# print(a)    

# 12. Mahsulot mavjudligi
# mahsulot_soni = 12
# mahsulot_soni 0 bo‘lsa "Tugagan".
# 1–5 bo‘lsa "Kam qoldi".
# 6 yoki undan yuqori bo‘lsa "Yetarli".
# if-elif-else ishlating.
# mahsulot_soni =67
# if mahsulot_soni>1 and mahsulot_soni<5:
#     a="Kam qoldi"
# elif mahsulot_soni>=6:
#     a="Yetarli"
# elif mahsulot_soni==0:
#     a="Tugagan"    
# print(a)    

# 13. Ikki fandan natija
# python_balli = 85
# sql_balli = 72
# Ikkala fan bali ham 60 yoki yuqori bo‘lsa "Ikkalasidan o‘tdi".
# Faqat bittasi 60 yoki yuqori bo‘lsa "Bittasidan o‘tdi".
# Ikkalasi ham 60 dan past bo‘lsa "Ikkalasidan yiqildi".
# and va or dan foydalanishingiz mumkin.
# python_balli = 85
# sql_balli = 72
# ballar={"python_balli":55 ,"sql_balli":72}
# for fan,ball in ballar.items():
#     if ball>=60:
#         natija="O'tdi"
#         print(f"{fan} dan {ball} bilan o'tdi")
#     elif ball<60:
#         natija="Yiqildi"
#         print(f"{fan} dan {ball} bilan yiqldi")


# 14. Parol uzunligi
# parol = "python2026"
# Uzunligi 12 yoki undan ko‘p bo‘lsa "Kuchliroq parol".
# 8–11 ta belgi bo‘lsa "O‘rtacha parol".
# 8 tadan kam bo‘lsa "Qisqa parol".
# len() va if-elif-else ishlating.
# parol=input("Iltimos parol kiriting:")
# p=len(parol)
# if p>=12:
#     natija="Kuchliroq parol"
# elif p>=8 and p<=11:
#     natija="O'rtacha parol"
# elif p<8:
#     natija="8 ta belgidan uzunroq parol qoying!"
# print(natija)    

# 15. Ikki sonning bo‘linishi
# a = 24
# b = 6
# Agar b nolga teng bo‘lsa "Nolga bo‘lish mumkin emas".
# Aks holda a soni b ga qoldiqsiz bo‘linsa "Qoldiqsiz bo‘linadi".
# Qoldiq qolsa "Qoldiq bilan bo‘linadi".
# if-elif-else ishlating.
# print("2 ta son kiriting!")
# sonlar=[]
# for i in range(2):
#     son=int(input(f"{i+1} sonni kiriting:"))
#     sonlar.append(son)    
# if sonlar[1]==0:
#     natija="ikkinchi son teng bola olmaydi 0 ga"
# elif sonlar[0]%sonlar[1]==0:
#     natija="Qoldiqsiz bo‘linadi"
# elif sonlar[0]%sonlar[1]!=0:
#     natija="Qoldiq bilan bo‘linadi"
# print(natija)    
    

# son = -8
# if son>0:
#     a="musbat"
# elif son<0:
#     a="manfiy"
# else:
#     a=0
# print(a)    

# a = 25
# b = 25
# if a==b:
#     c="a va b teng"
# elif a>b:
#     c="a katta b dan"
# elif a<b:
#     c="b katta a dan"
# print(c)

# ball = 86
# if ball>=90 and ball<=100: 
#     a="A'lo"
# elif ball>=70 and ball<=89: 
#     a="Yaxshi"
# elif ball>=60 and ball<=69: 
#     a="Qoniqarli"
# elif ball>=50 and ball<=59: 
#     a="Yiqildi"
# print(a)    

# son = 17
# if son>0 and son%2==0:
#     a="Musbat juft"
# elif son>0 and son%2!=0:
#     a="Musbat toq"
# elif son<0:
#     a="Manfiy"    
# print(a)


# harorat=33
# if harorat<0:
#     a="Sovuq"
# elif harorat>0 and harorat<15:
#     a="Salqin"
# elif harorat>16 and harorat<25:
#     a="Illiq"
# elif harorat>=25:
#     a="Issiq"
# print(a)



# yosh=78
# if yosh<0:
#     a="Notog'ri yosh"
# elif yosh>0 and yosh<12:
#     a="Bola"
# elif yosh>13 and yosh<17:
#     a="O'smir"
# elif yosh>18 and yosh<59:
#     a="Katta yoshli"
# elif yosh>60:
#     a="Keksa yosh"
# print(a)


# narx=2500000
# if narx>=300000:
#     a=f"20% chegirma {narx-narx*0.2}"
# elif narx>=150000:
#     a=f"10% chegirma {narx-narx*0.1}"  
# else:
#     a="Hech qanday chegirma yoq"    
# print(a)
    
    
# 8. Login va parol
# togri_login = "admin"
# togri_parol = "python123"    
# login = input("Iltimos loginizni kiriting:")
# parol = input("Parol kiriting:")
# if togri_login==login and togri_parol==parol:
#     a="Kirish mumkin"
# elif togri_login!=login and togri_parol==parol:
#     a="Sizning loginingiz xato"
# elif togri_login==login and togri_parol!=parol:
#     a="Sizning parolingiz xato"
# else:
#     a="Login va parol xato"
# print(a)    






































