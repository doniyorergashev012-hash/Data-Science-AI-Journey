# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# x va y sonlarini foydalanuvchidan olib, z ni konsolga chiqaruvchi funksiya yozing. x va y o'rtasida qanday amal bajarishingiz ixtiyoriy. Muhimi natija ya'ni z ni konsolga chiqaring.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
# def t_yil(ism,yosh,joriy_yil=2026):   
#    """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan"""
#    print(f"{ism.title()} ning tug'ilgani yili {joriy_yil-yosh}")
# ism=input("Ism kiriting:")
# yosh=int(input("Yoshingizni kiriting:"))
# t_yil(ism, yosh)   
# def kub(son):
#     """Sonning kvadratini hisoblash"""
#     print(son**3)
# son=int(input("Son kiriting:"))
# kub(son)    
# def kopaytma(x,y=9):
#     """Sonlar ortadida kopaytma"""
#     z=x*y
#     return z
# x=int(input("x:"))
# print(kopaytma(x))
# juft_sonlar=[]   
# def juftlar(son):
#     """2 dan 10 gacha sonlar ichidan"""
#     if son%2==0:
#         juft_sonlar.append(son)
# son=2        
# while son<=10:
#     juftlar(son)
#     son+=1
# print(juft_sonlar)
  
# def oraliq(min,max,qadam=1):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# print(oraliq(1, 20,3))a
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...   
# def malumotnoma(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email=None,telefon_num=None):
#     talaba={'ism':ismi,
#             'familiya':familiyasi,
#             'birth_data':tugilgan_yili,
#             'location':tugilgan_joyi,
#             'email':email,
#             'number':telefon_num}
#     return talaba
# malumotnomalar=[]
# while True:
#     sorov=input("Malumotnoma to'ldirishni xoxlaysizmi: Yes/no")
#     if sorov=='no':
#         break
#     ismi=input("ismingiz:").title()
#     familiyasi=input("familiyangiz:").title()
#     tugilgan_yili=input("tug'ildan yil:")
#     tugilgan_joyi=input("Joyi:")
#     email=input("email:")
#     malumotnomalar.append(malumotnoma(ismi,familiyasi,tugilgan_yili,tugilgan_joyi,email))
# print(malumotnomalar)
# for odam in malumotnomalar:
#     if odam['email']:
#         print(odam['ism'],odam['familiya'],odam['email'])
#     else:
#         print(odam['ism'],odam['familiya']) 
       
# def geometriya(radiusini, diametrini, perimetri,yuzini):
#     """Geometrik hisob kitoblar"""
#     javob={
#         'radius':radiusini,
#         'diametr':diametrini,
#         'uzunlig':uzunligi,
#         'yuzi':yuzini
#         }
#     return javob
# radiusini=int(input("radiusini kiriting:"))    
# diametrini=2*radiusini
# uzunligi=2*3.14*radiusini
# yuzini=2*3.14*(radiusini**2)
# natija=geometriya(radiusini, diametrini, uzunligi, yuzini)
# print(natija)
# son=0
# sonlar=[]
# while son<3:
#     a=int(input(f"{son+1}-sonni kiriting:"))
#     sonlar.append(a)
#     son+=1
# def maxs(x,y,z):
#     maxsim=x
#     if y>x and y>z:
#         maxsim=y
#     elif z>x and z>y:
#         maxsim=z
#     return maxsim
# print(maxs(sonlar[0],sonlar[1],sonlar[2])) 
# tub_sonlar=[]
# sonlar=[]
# def oraliq(min,max):
#     """Tubsonlar topish oraliqdagi"""
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# print(oraliq(2, 15))
# while sonlar:
#     a=sonlar.pop()
#     if a%2==0 or a%3==0 or a%4==0 or a%5==0 or a%6==0 or a%7==0 or a%8==0 or a%9==0:
#         print("Tub son emas") 
#     else:
#         tub_sonlar.append(a) 
# print(tub_sonlar)
# sonlar=[0,1]         
# def fibonachi(n):
#     while len(sonlar)<n:
#         yangi_son=sonlar[-1]+sonlar[-2]
#         sonlar.append(yangi_son)
#     return sonlar
# print(fibonachi(15))    


# 📘 19-DARS. FUNKSIYALAR

# 1-DARAJA: 15 TA AMALIY MASALA

# 1. Salomlashish funksiyasi
# salom() nomli funksiya yarating.
# Funksiya "Assalomu alaykum!" matnini ekranga chiqarsin.
# Funksiyani 3 marta chaqiring.
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assaom aleykum")
# for i in range(3):    
#     salom_ber()

# 2. Ism bilan salomlashish
# salom_ber(ism) nomli funksiya yarating.
# Funksiya berilgan ism bilan salomlashsin.
# Funksiyani "Ali", "Vali", "Sardor" ismlari bilan chaqiring.

# def salom_ber(ism):
#     """Funksiya berilgan ism bilan salomlashish"""
#     print(f"Salom {ism.title()}")
# for i in range(3):
#     ism=input("Ismingizni kiriting:")
#     salom_ber(ism)    
    

# 3. Ikki sonni qo‘shish
# qoshish(a, b) nomli funksiya yarating.
# Ikkita sonni qabul qilib, ularning yig‘indisini chiqaring.
# a = 25
# b = 15

# def sonlar_ustida_ammallar(a,b):
#     """Ikkita sonni qabul qilib, ularning yig‘indisini chiqaring"""
#     print(a+b)
# a=int(input("a:"))
# b=int(input("b:"))
# sonlar_ustida_ammallar(a, b)    

# 4. Sonning kvadrati
# kvadrat(son) nomli funksiya yarating.
# Berilgan sonning kvadratini hisoblab chiqaring.
# son = 8
# def kvadrat(son):
#     """Soni kvadratini hisoblash"""
#     print(son**2)
# a=int(input("Son kiriting:"))
# kvadrat(a)    


# 5. Sonning kubi
# kub(son) nomli funksiya yarating.
# Berilgan sonning kubini hisoblab chiqaring.
# son = 4
# def sonning_kubi(son):
#     """"Berilgan sonning kubini hisoblab chiqarish"""
#     print(son**3)
# son=int(input("Son kiriitng:"))
# sonning_kubi(son)    

# 6. Juft yoki toq
# juft_toq(son) nomli funksiya yarating.
# Son juft bo‘lsa "Juft", aks holda "Toq" deb chiqaring.
# son = 17
# def juft_toq(son):
#     """Son juft bo‘lsa "Juft", aks holda "Toq" deb chiqaring"""
#     if son%2==0:
#         print("Juft son")
#     elif son%2!=0:
#         print("Toq son")
# a=int(input("Son kiriting:"))    
# juft_toq(a)

# 7. Yoshni aniqlash
# yosh_aniqla(yosh) nomli funksiya yarating.
# Yosh 18 yoki undan katta bo‘lsa "Voyaga yetgan",
# aks holda "Voyaga yetmagan" deb chiqaring.
# yosh = 20
# def yosh_aniqla(yosh):
#     """Yosh aniqlovchi funksiya"""
#     if yosh>=18:
#         a="Vayaga yetgan"
#     else:
#         a="Og'zidan sut xidi ketmagan"
#     return a    
# yosh=int(input("Yosh kiriting:"))
# print(yosh_aniqla(yosh))

# 8. Ikki sonning kattasini topish
# kattasini_top(a, b) nomli funksiya yarating.
# Ikkita son ichidan kattasini aniqlab chiqaring.
# a = 45
# b = 78
# def kattasini_top(a, b):
#     """Ikki sonning kattasini topish"""
#     if a>b:
#         print(f"{a} katta {b} dan")
#     elif b>a:
#         print(f"{b} katta {a} dan")
#     else:
#         print(f"{a} va {b} teng!")
# a=int(input("a:"))        
# b=int(input("b:"))
# kattasini_top(a, b)

# 9. Matn uzunligini aniqlash
# uzunlik(matn) nomli funksiya yarating.
# Berilgan matndagi belgilar sonini aniqlab chiqaring.
# len() metodidan foydalaning.
# matn = "Python dasturlash"
# def uzunlik(matn):
#     """Matn uzunligini aniqlash"""
#     print(len(matn))
# a=input("Malumot kiriting:")
# uzunlik(a)    

# 10. Matnni katta harflarga o‘tkazish
# katta_harf(matn) nomli funksiya yarating.
# Berilgan matnni katta harflarda chiqaring.
# matn = "python dasturlash"
# def katta_harf(matn):
#     """Matnni katta harflarga o‘tkazish"""
#     print(matn.upper())
# matn=input("Nimadir kiriting:")
# katta_harf(matn)    

# 11. Ro‘yxat yig‘indisi
# royxat_yigindi(sonlar) nomli funksiya yarating.
# Ro‘yxatdagi barcha sonlarni qo‘shib, natijani chiqaring.
# sum() ishlatmang.
# sonlar1 = [10, 20, 30, 40, 50]
# def royxat_yigindi(sonlar):
#     jami=0
#     while sonlar:
#         a=sonlar.pop()
#         jami+=a
#     return jami
# print(royxat_yigindi(sonlar1[:]))    
 

# 12. Ro‘yxatdagi eng katta son
# eng_katta(sonlar) nomli funksiya yarating.
# Ro‘yxatdagi eng katta sonni topib chiqaring.
# max() ishlatmang.
# sonlar1 = [15, 42, 8, 67, 23, 51]
# def eng_katta(sonlar):
#     """Ro‘yxatdagi eng katta sonni topish"""
#     max=sonlar[1]
#     while sonlar:
#         a=sonlar.pop()
#         if a>max:
#             max=a
#     return max
# print(eng_katta(sonlar1))        
        

# 13. Ro‘yxatdagi eng kichik son
# eng_kichik(sonlar) nomli funksiya yarating.
# Ro‘yxatdagi eng kichik sonni topib chiqaring.
# min() ishlatmang.
# raqamlar = [45, 12, 78, 3, 29, 16]
# def eng_kichik(sonlar):
#     """Ro‘yxatdagi eng kichik sonni topish"""
#     min=sonlar[1]
#     while sonlar:
#         a=sonlar.pop()
#         if a<min:
#             min=a
#     return min
# print(f" Eng kichik son-{eng_kichik(raqamlar)}")        
     
# 14. Lug‘atdagi ma’lumotlarni chiqarish
# talaba_haqida(talaba) nomli funksiya yarating.
# Lug‘atdagi barcha kalit va qiymatlarni chiqaring.
# malumot = {
#     "ism": "Ali",
#     "familiya": "Valiyev",
#     "yosh": 20,
#     "kurs": 2
# }
# def talaba_haqida(talaba):
#     for key,value in talaba.items():
#         print(key,'-',value)
# talaba_haqida(malumot)

# 15. Ro‘yxatdagi sonlarni ko‘paytirish
# kopaytir(sonlar, son) nomli funksiya yarating.
# Ro‘yxatdagi har bir sonni berilgan songa ko‘paytiring.
# Natijalarni yangi ro‘yxatga joylashtirib chiqaring.
# sonlar1 = [2, 4, 6, 8, 10]
# son1 = 3
# sonlar2=[]
# x=sonlar1.copy()
# def kopaytir(sonlar, son):
#     """Ro‘yxatdagi har bir sonni berilgan songa ko‘paytiring"""
#     for i in sonlar:
#         b=i*son
#         sonlar2.append(b)
#     return sonlar2
# print(kopaytir(x, son1))    

# 2-DARAJA: 10 TA MANTIQIY MASALA

# 16. Return yordamida yig‘indi
# yigindi(a, b) nomli funksiya yarating.
# Ikkita sonni qo‘shib, natijani return orqali qaytaring.
# Funksiyani chaqirib, natijani alohida o‘zgaruvchiga saqlang.
# y = 35
# x = 65
# def yigindi(a,b):
#     '''Return yordamida yig‘indi'''
#     z=a+b
#     return z
# print(yigindi(x, y))

# 17. Uchta sonning o‘rtacha qiymati
# ortacha(a, b, c) nomli funksiya yarating.
# Uchta sonning o‘rtacha arifmetigini hisoblab qaytaring.
# a = 15
# b = 25
# c = 50
# def ortacha(a,b,c):
#     z=(a+b+c)/3
#     return z
# print(ortacha(a, b, c))

# 18. Tub sonni aniqlash
# tub_son(son) nomli funksiya yarating.
# Son tub bo‘lsa True, aks holda False qaytaring.
# 1 tub son emasligini hisobga oling.
# son = 17
# def tub_son(son):
#     boluvchi=2
#     shart=True
#     if son<2:
#         shart=False
#     while boluvchi<son:
#         if son%boluvchi==0:
#             shart=False
#             break
#         boluvchi+=1
#     return shart
# if tub_son(son):
#     print("Tub son")
# else:
#     print("Toq son")    

# 19. Raqamlar yig‘indisi
# raqamlar_yigindisi(son) nomli funksiya yarating.
# Berilgan son raqamlarining yig‘indisini hisoblab qaytaring.
# Masalan: 456 -> 15.
# son = 456
# def raqamlar_yigindisi(son):
#     """Raqamlar yig‘indisi"""
#     jami=0
#     while son>0:
#         a=son%10
#         jami+=a
#         son=son//10
#     return jami
# print(raqamlar_yigindisi(456))

# 20. Matndagi unli harflar
# unli_hisobla(matn) nomli funksiya yarating.
# Matnda nechta unli harf qatnashganini hisoblab qaytaring.
# Unli harflar: a, e, i, o, u.
# matn = "Men Python dasturlashni o‘rganyapman"
# unli=['a', 'e', 'i', 'o', 'u']
# matn = "Men Python dasturlashni o‘rganyapman"
# def unli_harf(matn):
#     jami=0
#     for harf in matn:
#         if harf in unli:
#             jami+=1
#     return jami
# print(unli_harf(matn))       

# 21. Ro‘yxatdagi juft sonlar
# juft_sonlar(sonlar) nomli funksiya yarating.
# Ro‘yxatdan faqat juft sonlarni ajratib,
# yangi ro‘yxat sifatida return qiling.
sonlar1 = [12, 7, 8, 15, 20, 3, 10, 25]
juft_sonlarr=[]
def juft_sonlar(sonlar):
    """Ro‘yxatdagi juft sonlar"""
    while sonlar:
        a=sonlar.pop()
        if a%2==0:
            juft_sonlarr.append(a)
    return juft_sonlarr
print(juft_sonlar(sonlar1[:]))        

# 22. So‘zni teskari qilish
# teskari(matn) nomli funksiya yarating.
# Berilgan matnni teskari tartibda qaytaring.
# Masalan: "Python" -> "nohtyP".
# matn = "Python"
# def teskari(matn):
#    """So‘zni teskari qilish""" 
#    a=matn[::-1]
#    return a
# print(teskari(matn))

# 23. Lug‘atdagi narxlar yig‘indisi
# jami_narx(narxlar) nomli funksiya yarating.
# Lug‘atdagi barcha mahsulotlar narxini qo‘shib qaytaring.
# narxlar = {
#     "non": 4000,
#     "sut": 12000,
#     "tuxum": 18000,
#     "yog": 25000
# }
# def jami_narx(narxlar):
#     """Lug‘atdagi narxlar yig‘indisi"""
#     jami=0
#     for i in narxlar.values():
#         jami+=i
#     return jami
# print(jami_narx(narxlar))    

# 24. Bahoni aniqlash
# baho_aniqla(ball) nomli funksiya yarating.
# 90-100: "A'lo"
# 70-89: "Yaxshi"
# 60-69: "Qoniqarli"
# 0-59: "Qoniqarsiz"
# Natijani return orqali qaytaring.
# ball =94
# def baho_aniqla(ball):
#     """Bahoni aniqlash"""
#     if ball>=90 and ball<=100:
#         natija="A'lo"
#     elif ball>=70 and ball<=89:
#         natija="Yaxshi"
#     elif ball>=60 and ball<=69:
#         natija="Qoniqarli"
#     elif ball>=0 and ball<=59:
#         natija="Qoniqarsiz"
        
#     return natija
# print(baho_aniqla(ball))


# 25. Parolni tekshirish
# parol_tekshir(parol) nomli funksiya yarating.
# Parol uzunligi 8 yoki undan ko‘p bo‘lsa True,
# aks holda False qaytaring.
# len() dan foydalaning.
# parol = "python2026"
# def parol_tekshir(parol):
#     soni=0
#     for harf in parol:
#         soni+=1
#     if soni>=8:    
#          return True
#     else:
#         return False
# print(parol_tekshir(parol))        

# 🔥 3-DARAJA: 5 TA KICHIK LOYIHA

# 26. KALKULYATOR
# kalkulyator(a, b, amal) nomli funksiya yarating.
# Amal quyidagilardan biri bo‘ladi: "+", "-", "*", "/".
# Tanlangan amalga qarab hisob-kitob bajaring.
# Agar bo‘luvchi 0 bo‘lsa, xatolik haqida xabar chiqaring.
# Noto‘g‘ri amal kiritilsa, "Noto‘g‘ri amal" deb chiqaring.
# Foydalanuvchidan amal va ikkita sonni input() orqali oling.
# def  kalkulyator(a, b, amal):
#     """KALKULYATOR"""
#     if amal=="+":
#         n=a+b
#     elif amal=="-":
#         n=a-b
#     elif amal=="*":
#         n=a*b
#     elif amal==":":
#         if b==0:
#             n="0 ga bolish mumkin emas"
#         else:
#             n=a/b
#     elif amal!="+" or amal!="-" or amal!="*" or amal!=":":
#         n="Notog'ri amal"
#     return n
# print(kalkulyator(120,0, ":"))
    


# 27. TALABALAR BAHOLARI HISOBOTI
# hisobot(baholar) nomli funksiya yarating.
# Quyidagi lug‘atdan foydalaning:
# baholar = {
#     "Ali": 5,
#     "Vali": 4,
#     "Sardor": 5,
#     "Jasur": 3,
#     "Akmal": 4,
#     "Aziz": 2
# }
# Funksiya quyidagilarni aniqlasin:
# 1. Talabalar soni.
# 2. Baholar yig‘indisi.
# 3. O‘rtacha baho.
# 4. 5 baho olgan talabalar soni.
# 5. 3 dan past baho olgan talabalar soni.
# def hisobot(baholar):
#     """TALABALAR BAHOLARI HISOBOTI"""
#     print(len(baholar))
#     yigindi=0
#     soni=0
#     for k,q in baholar.items():
#         yigindi+=q
#         if q==5:
#             soni+=1
#         if q<4:
#             print(k,"-",q)
#     return yigindi,soni
# yigindi,soni=hisobot(baholar) 
# print(f"baholar umumiy yigindisi-{yigindi}")
# print(f"5 baholar soni -{soni}")       

# 28. BANK HISOBI
# bank_hisobi() nomli funksiya yarating.
# Boshlang‘ich balans 100000 so‘m bo‘lsin.
# Quyidagi menyuni yarating:
# 1 - Pul qo‘shish
# 2 - Pul yechish
# 3 - Balansni ko‘rish
# 0 - Chiqish
# Foydalanuvchi 0 ni tanlamaguncha dastur ishlasin.
# Balansdan ortiq pul yechishga ruxsat berilmasin.
# Har bir amal alohida funksiya yordamida bajarilsin.
# Barcha ma’lumotlar input() orqali olinsin.

# def bankamat_ishlashi():
#     hisob=100000
#     while True:
#         print("""1 - Pul qo‘shish
#         2 - Pul yechish
#         3 - Balansni ko‘rish
#         0 - Chiqish""")
#         amal=int(input("Menyudan amalni tanlang:"))
#         if amal==1:
#             summa=int(input("Qancha summa kiritiasiz:"))
#             hisob+=summa
#         elif amal==2:
#             summa=int(input("Qancha summa yechmoqchisiz:"))
#             if summa<=hisob:
#                 hisob-=summa
#             else:
#                 print("Mablag' yetarli emas!")
#                 continue
#         elif amal==3:
#              print(hisob)
#         elif amal==0:
#              break
#     return hisob
# bankamat_ishlashi()     
        

# 29. TELEFON RAQAMLAR KITOBI
# telefon_kitob() nomli funksiya yarating.
# Quyidagi lug‘atdan foydalaning:
# telefonlar = {
#     "Ali": "901112233",
#     "Vali": "931234567",
#     "Sardor": "991234567",
#     "Jasur": "971112233"
# }
# Menyu yarating:
# 1 - Kontakt qidirish
# 2 - Barcha kontaktlarni ko‘rish
# 3 - Yangi kontakt qo‘shish
# 4 - Kontaktni o‘chirish
# 0 - Chiqish
# Har bir amalni alohida funksiya orqali bajaring.
# Foydalanuvchi kerakli ma’lumotlarni input() orqali kiritsin.




















# 30. DO‘KON BOSHQARUV TIZIMI
# dokon() nomli asosiy funksiya yarating.
# Quyidagi mahsulotlar lug‘atidan foydalaning:
# mahsulotlar = {
#     "non": 4000,
#     "sut": 12000,
#     "tuxum": 18000,
#     "yog": 25000,
#     "shakar": 15000
# }
# Menyu yarating:
# 1 - Barcha mahsulotlarni ko‘rish
# 2 - Mahsulot qidirish
# 3 - Yangi mahsulot qo‘shish
# 4 - Mahsulot narxini o‘zgartirish
# 5 - Mahsulotni o‘chirish
# 6 - Barcha mahsulotlar narxini hisoblash
# 0 - Chiqish
# Har bir amalni alohida funksiya orqali bajaring.
# Foydalanuvchi kerakli ma’lumotlarni input() orqali kiritsin.


# ==========================================
# ESLATMA:
# - Har bir topshiriqni funksiya yordamida bajaring.
# - Funksiyalarni chaqirishni unutmang.
# - print() va return farqiga e'tibor bering.
# - Avval o‘zingiz ishlang, tayyor yechimlardan foydalanmang.
# ==========================================

