# 1. 1 dan 10 gacha bo'lgan sonlarni chiqaring.
# Boshlanish: son = 1
# son=1
# while son<10:
#     print(son,end=' ')
#     son+=1


# 2. 10 dan 1 gacha bo'lgan sonlarni kamayish tartibida chiqaring.
# Boshlanish: son = 10
# son=10
# while son>0:
#     print(son,end=' ')
#     son-=1

# 3. 1 dan 20 gacha bo'lgan juft sonlarni chiqaring.
# Boshlanish: son = 2
# son=2
# while son<=20:
#     if son%2!=0:
#         print(son,end=' ')
#         son+=1



# 4. 1 dan 20 gacha bo'lgan toq sonlarni chiqaring.
# Boshlanish: son = 1
# son=1
# while son<=20:
#     if son%2!=0:
#         print(son)
#     son+=1
        

# 5. 1 dan 50 gacha bo'lgan sonlarni chiqaring.
# Har bir son orasida bo'sh joy bo'lsin.
# sonlar=list(range(1,51))
# for son in sonlar:
#     print(son,end=" ")
# son=1
# while son<=50:
#     print(son,end=' ')
#     son+=1

# 6. 1 dan 10 gacha bo'lgan sonlarning kvadratini chiqaring.
# Masalan: 1 - 1, 2 - 4, 3 - 9.
# son=1
# while son<10:
#     print(f"{son}ning kvadrati {son**2}")
#     son+=1

# 7. 1 dan 10 gacha bo'lgan sonlarning kubini chiqaring.
# Masalan: 2 ning kubi 8.
# son=1
# while son<=10:
#     print(f"{son}ning kubi {son**3}")
#     son+=1


# 8. 5 dan 50 gacha 5 ga karrali sonlarni chiqaring.
# son=5
# while son<=50:
#     if son%5==0:
#         print(son)
#     son+=1    

# 9. 1 dan 100 gacha bo'lgan sonlar yig'indisini hisoblang.
# Natijani konsolga chiqaring.
# jami=0
# son=1
# while son<=100:
#     jami+=son
#     son+=1
# print(jami)    


# 10. 1 dan 10 gacha bo'lgan sonlarni va ularning
# 3 ga ko'paytirilgan qiymatini chiqaring.
# son=1
# while son<=10:
#     print(f"{son}ning 3 ga ko'paytmasi {son*3}")
#     son+=1

# 11. 20 dan 0 gacha 2 tadan kamayib chiqaring.
# son=20
# while son>=0:
#     if son%2==0:
#         print(son)
#     son-=2    

# 12. 1 dan 30 gacha bo'lgan 3 ga karrali sonlarni chiqaring.
# son=1
# while son<=30:
#     if son%3==0:
#         print(son)
#     son+=1    

# 13. 1 dan 10 gacha bo'lgan sonlarning
# 5 ga ko'paytirish jadvalini chiqaring.
# son=1
# while son<=10:
#     print(f"{son}x{5}={son*5}")
#     son+=1    


# 14. 1 dan 10 gacha bo'lgan sonlarning yig'indisini
# # va ko'paytmasini alohida hisoblang.
# jami=0
# kopaytma=1
# son=1
# while son<=10:
#     jami+=son
#     kopaytma*=son
#     son+=1
# print(jami,kopaytma)    
    

# 15. 100 dan 50 gacha bo'lgan sonlarni
# 5 tadan kamaytirib chiqaring.
# son=100
# while son>=50:
#     print(son)
#     son-=5



# 16. Foydalanuvchidan son kiriting.
# 1 dan shu songacha bo'lgan barcha sonlarni chiqaring.
# Masalan: 7 kiritilsa, 1 2 3 4 5 6 7 chiqsin.
# savol=int(input("Son kiriting:"))
# son=1
# while son<=savol:
#     print(son,end=' ')
#     son+=1


# 17. Foydalanuvchidan son kiriting.
# Shu sonning ko'paytirish jadvalini 1 dan 10 gacha chiqaring.
# Masalan: 6 kiritilsa, 6 x 1 dan 6 x 10 gacha.
# a="1 dan 10 ga cha raqam kiriting:"
# raqam=int(input(a))
# son=1
# while son<=10:
#     print(f"{raqam}x{son}={raqam*son}")
#     son+=1

# 18. Foydalanuvchidan 5 ta son kiriting.
# Ularning umumiy yig'indisini hisoblang.
# Eslatma: nechta son kiritilganini hisoblash uchun
# alohida sanoq o'zgaruvchisi ishlating.
# sonlar=[]
# son=1
# print("5 ta son kiriting!")
# while son<=5:
#     son1=int(input(f"{son}-sonni kiriting:"))
#     sonlar.append(son1)
#     son+=1
# print(sum(sonlar))    
    
# 19. Foydalanuvchidan son kiriting.
# Shu sonning faktorialini hisoblang.
# Masalan: 5! = 120.
# Eslatma: faktorial — 1 dan shu songacha
# bo'lgan sonlarning ko'paytmasi.
# print("Faktarial hisoblash dasturi!")
# son=1
# faktarial=1
# raqam=int(input("Son kiriting: "))
# while son<=raqam:
#     faktarial*=son
#     son+=1
# print(f"{raqam}ning faktoriali {faktarial}")

# 20. Foydalanuvchidan son kiriting.
# Shu sonning raqamlarini birma-bir ajratib,
# ularning yig'indisini hisoblang.
# Masalan: 245 kiritilsa, 2 + 4 + 5 = 11.
# son=int(input('Son kiriting:'))
# jami=0
# while son>0:
#     raqam=son%10
#     jami+=raqam
#     son=son//10
# print(jami)    

# 21. Foydalanuvchidan son kiriting.
# Shu sonning nechta raqamdan iboratligini aniqlang.
# Masalan: 4582 kiritilsa, 4 ta raqam.
# bolaklar=[]
# son=int(input('Son kiriting:'))
# while son>0:
#     raqam=son%10
#     bolaklar.append(raqam)
#     son=son//10
# print(len(bolaklar))
# print(bolaklar[::-1])    


# 22. Foydalanuvchidan son kiriting.
# Sonning raqamlarini teskari tartibda chiqaring.
# Masalan: 1234 kiritilsa, 4321 hosil bo'lsin.
# sonlar=[]
# son=input('Son kiriting:')
# sonlar.append(son)
# for i in sonlar:
#     print(i[::-1])

# 23. Foydalanuvchidan sonlar kiriting.
# 0 kiritilguncha sonlarni qabul qiling.
# Kiritilgan sonlarning yig'indisini hisoblang.
# 0 yig'indiga qo'shilmasin.
# jami=0
# # son=int(input('Son kiriting:'))
# while True:
#     son=int(input('Son kiriting:'))
#     if son!=0:
#         jami+=son
#     elif son==0:
#         break
# print(jami)    
    
# 24. Foydalanuvchidan son kiriting.
# Shu songacha bo'lgan faqat juft sonlar yig'indisini hisoblang.
# son=1
# jami_juft=0
# raqam=int(input('Son kiriting:'))
# while son<=raqam:
#     if son%2==0:
#         jami_juft+=son
#     son+=1
# print(jami_juft)    
    

# 25. Foydalanuvchidan 1 dan 10 gacha son kiritishni so'rang.
# To'g'ri son kiritilmaguncha qayta so'rang.
# To'g'ri son kiritilganda "Qabul qilindi" chiqaring.
# print("1 dan 10 gacha  bolgan son kiriting:")
# sonlar=list(range(1,11))
# while True:
#     son=int(input("Son kiriting:"))
#     if son in sonlar:
#         print("Qabul qilindi")
#         break
#     else:
#         print("1 dan 10 gacha faqat")


# 26. SON TOPISH O'YINI
# Kompyuter o'ylagan son oldindan 7 deb belgilansin.
# Foydalanuvchi son kiritadi.
# Agar son 7 bo'lsa, "Topdingiz!" chiqsin.
# Aks holda "Qayta urinib ko'ring" chiqsin.
# To'g'ri topilmaguncha so'rash davom etsin.
# sirli_son=7
# print("Son topish o'yini")
# while True:
#     son=int(input("Son kiriting:"))
#     if son==sirli_son:
#         print("Topdingiz")
#         break
#     else:
#         print("Qayta urinib ko'ring")



# 27. BANK HISOBI
# Boshlang'ich balans = 100000.
# Foydalanuvchiga quyidagi menyuni ko'rsating:
# 1 - Pul qo'shish
# 2 - Pul yechish
# 3 - Balansni ko'rish
# 0 - Dasturni tugatish
# Foydalanuvchi 0 kiritmaguncha menyu takrorlansin.
# Har bir operatsiyadan keyin balans yangilansin.
# Balansdan ko'p pul yechishga ruxsat berilmasin.
# balans=100000
# print("""1 - Pul qo'shish
# 2 - Pul yechish
# 3 - Balansni ko'rish
# 0 - Dasturni tugatish""")
# ishora=True
# while ishora:
#     son=int(input("Menu dan O'zingizga mosini tanlang:"))
#     if son==1:
#         pul=int(input("Qo'shmoqchi bolgan summani kiriting:"))
#         balans+=pul
#         print(f"Sizning hisobingizda {balans} so'm bor")
#         savol=input("Amaliyotni davom etirasizmi: Ha yoki Yoq?").lower().title()
#         if savol=="Ha":
#             continue
#         elif savol=="Yoq":
#             break   
#     elif son==2:
#         pul=int(input("Qancha summa yechmoqchisiz:"))
#         if pul>balans:
#             print("Katta summa yechish mumkinmas")
#             continue
#         else:
#             balans-=pul
#             print(f"Sizning hisobingizda {balans} so'm qoldi")
#             savol=input("Amaliyotni davom etirasizmi: Ha yoki Yoq?").lower().title()
#             if savol=="Ha":
#                 continue
#             elif savol=="Yoq":
#                 break   
#     elif son==3:
#         print(f"Sizning hisobingizda {balans} so'm bor")
#         savol=input("Amaliyotni davom etirasizmi: Ha yoki Yoq?").lower().title()
#         if savol=="Ha":
#             continue
#         elif savol=="Yoq":
#             break   
#     elif son==0:
#         ishora=False
#         print("Dastur tugadi")


# 28. BAHOLAR HISOBOTI
# Foydalanuvchidan 0 kiritilguncha baholarni so'rang.
# 0 baho sifatida hisoblanmasin.
# Kiritilgan baholar sonini hisoblang.
# Baholarning yig'indisini hisoblang.
# Oxirida o'rtacha bahoni chiqaring.
# print("BAHOLAR HISOBOTI")
# jami=0
# soni=[]
# while True:
#     baho=int(input("Bahoyingizni kiriting:"))
#     if baho!=0:
#         jami+=baho
#         soni.append(baho)
#         a=len(soni)
#     else:
#         print(f"Umimiy ball {jami},o'rtacha ball {jami/a}")
#         break


# 29. KUNLIK XARAJATLAR
# Foydalanuvchidan har kungi xarajatini so'rang.
# 0 kiritilguncha xarajatlar qabul qilinsin.
# Barcha xarajatlarni qo'shing.
# Necha marta xarajat kiritilganini hisoblang.
# Oxirida umumiy xarajatni va xarajatlar sonini chiqaring.
# print("KUNLIK XARAJATLAR")
# jami=0
# soni=0
# while True:
#     expence=int(input("Kunlik daromadingizni kiriting:"))
#     if expence!=0:
#         jami+=expence
#         soni+=1
#     else:
#         break
# print(f"Jami chiqimlar-{jami} va soni-{soni}")    

# 30. KALKULYATOR
# Foydalanuvchiga menyu ko'rsating:
# 1 - Qo'shish
# 2 - Ayirish
# 3 - Ko'paytirish
# 4 - Bo'lish
# 0 - Chiqish
# Foydalanuvchi 0 kiritmaguncha dastur ishlasin.
# Har bir amal uchun ikkita son so'rang.
# Natijani chiqaring.
# Nolga bo'lishga ruxsat bermang.
# print("""
# 1 - Qo'shish
# 2 - Ayirish
# 3 - Ko'paytirish
# 4 - Bo'lish
# 0 - Chiqish""")
# n=1
# sonlar=[]
# while n<=2:
#     menu=int(input("Menyudan bittasini tanlang:"))
#     if menu==0:
#         print("Dastur tugadi")
#         break
#     son1=int(input(f"{1}-sonni kiriting:"))
#     son2=int(input(f"{2}-sonni kiriting:"))
    
#     if menu==1:
#         a=son1+son2
#         print(a)
#     elif menu==2:
#         a=son1-son2
#         print(a)
#     elif menu==3:
#         a=son1*son2
#         print(a)
#     elif menu==4:
#         if son2==0:
#             print("0 ga bolish mumkinmas!")
#             continue
#         else:
#             a=son1/son2
#             print(a)


















