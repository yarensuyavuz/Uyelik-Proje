# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 22:05:16 2021

@author: yaren
"""
import json
from random import randint

class Uyelik:
    def __init__(self):
        self.durum=True
        self.veriler=verileriAl()
        
        
        
    def calistir(self):
       self.menuEkran()
       secim=self.menuSecimYap()
       
       if secim ==1:
           self.girisYap()
       if secim==2:
            self.kayitOl()
       if secim==3:
            self.cikis()
   
          
       
       
    def menuEkran(self):
        print("""
       1-Giriş yap
       2-Kayıt Ol
       3-Çıkış
       """)
       
    
    def menuSecimYap(self):
        while True:
          try:
            secim=int(input("Seçiminizi giriniz:"))
            while secim<1 or secim>3:
                secim=int(input("Lütfen 1 ve 3 arası bir değer giriniz"))
            break
          except ValueError:
             print("Lütfen sayı değeri giriniz")
  
    def verileriAl(self):  
      try:
       with open ("kullanicilar.json","r") as dosya:
          veriler=json.load(dosya)
          
      except FileNotFoundError:
         with open ("kullanicilar.json","w") as dosya:
           dosya.write("{}")
         with open ("kullanicilar.json","r") as dosya:
            veriler=json.load(dosya)
      
      print(veriler)
      return veriler
   
    def girisYap(self):
       # kullanıcı adı ve şifre alacağım
      kullaniciadi=input("kullanıcı adını giriniz")
      sifre=input("şifrenizi giriniz:")
      durum=self.kontrolEt(kullaniciadi,sifre)
      if durum:
          self.girisBasarili()
      else:
          self.girisBasarisiz("Yanlış bilgi girildi")
        
    def kayitOl(self):
        kullaniciadi=input("kullanıcı adını giriniz")
        sifre=input("şifrenizi giriniz:")
        aktivasyonKodu=self.aktivasyonkodugonder()
        aktivasyondurumu=self.aktivasyonkodukontrolet(aktivasyonKodu)
       
        if akdurum:
            self.kaydet(kullaniciadi,sifre)
        else:
            print("Hatalı aktivasyon kodu girdiniz")
    
    def cikis(self):
       self.durum=False
       print("Çıkış yapıldı")
       
    def kontrolEt(self):
      self.veriler=self.verileriAl()
        
      for kullanici in self.veriler["kullanicilar"]:
         if kullanici["kullaniciadi"]==kullaniciadi and kullanici[sifre]==sifre:
            self.aktivasyonkodugonder()
            return True
         
        
    def kayitVarMi(self,kullaniciadi,sifre):
       self.veriler=self.verileriAl()
       try:
         for kullanici in self.veriler["kullanicilar"]:
           if kullanici["kullaniciadi"]==kullaniciadi:
             return True
       except KeyError:
         return False
    
    
    def girisBasarisiz(self):
        print("Giriş başarısız oldu")
    
    def girisBasarili(self,giris):
       print("Giriş yapıldı")
       self.durum=False
       
    
    def aktivasyonkodugonder(self):
        with open("Aktivasyon.txt","w")as dosya:
            aktivasyon=(str(randint(100,999)))
            dosya.write(aktivasyon)
   
    
    def aktivasyonkodukontrolet(self,aktivasyon):
          aktivasyonKoduAl=input("Aktivasyon kodunu giriniz:")
        
          if aktivasyon==aktivasyonKoduAl:
             return True
          else :
            return False
   
    
   
    def kaydet(self,kullaniciadi,sifre):
       self.veriler=self.verileriAl()
       try:
         self.veriler["kullanıcılar"].append({"kullaniciadi":kullaniciadi,"sifre":sifre})
       except KeyError:
         self.veriler["kullanicilar"]={"kullaniciadi":kullaniciadi,"sifre":sifre}
         
       with open("kullanicilar.json","w")as dosya:
            json.dump(self.veriler,dosya)
            print("Oluşturuldu")