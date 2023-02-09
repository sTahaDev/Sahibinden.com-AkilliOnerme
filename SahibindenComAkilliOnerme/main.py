from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os

PATH = r"C:\webdriver\chromedriver.exe"


def veriCek(path,webpageadress):
    fiyatListesi = []
    driver = webdriver.Chrome(path)
    driver.get(webpageadress)

    pageHtml = driver.page_source
    soup = BeautifulSoup(pageHtml,"html.parser")

    myItems = soup.find_all("tr", {"class": "searchResultsItem"})
    os.system("cls")
    for i in myItems:
        #Verilerin Çekilmesi
        itemNames = i.find("a",{"class":"classifiedTitle"})
        itemPrices = i.find("div",{"class":"classified-price-container"})
        itemDate = i.find("td",{"class":"searchResultsDateValue"})
        itemPlace = i.find("td",{"class":"searchResultsLocationValue"})
        #Boşluk Bırakmama Sorunu
        itemPlaceNoSpace = str(itemPlace)
        itemPlaceNoSpace = itemPlaceNoSpace.replace("<br/>"," ")
        itemPlaceNoSpace = itemPlaceNoSpace.replace("</td>","")
        itemDateNoSpace = str(itemDate)
        itemDateNoSpace = itemDateNoSpace.replace("<br/>"," ")
        itemDateNoSpace = itemDateNoSpace.replace("</td>","")
        #itemPlace = itemPlace.replace("<br/>","")
        #İçerideki YAzıyı alma
        itemNames = itemNames.text
        itemPrices = itemPrices.text
        itemDate = itemDate.text
        itemPlace = itemPlace.text
        #Verilerden boşlukların çıkarılması
        itemNames = itemNames.replace("\n","")
        itemNames = itemNames.replace("   ","")
        itemPrices = itemPrices.replace("\n","")
        itemDate = itemDate.replace("\n","")
        itemPlace = itemPlace.replace("\n","")
        itemDateNoSpace = itemDateNoSpace.replace("\n","")
        itemDateNoSpace = itemDateNoSpace.replace("   ","")
        #Araba Fiyatının Int olarak Alınması
        itemPrices = itemPrices.replace("TL","")
        itemPricesNotDots = itemPrices.replace(".","")
        itemPricesInt = int(itemPricesNotDots)
        #Boşlukların Ayarlanamsı
        soup2 = BeautifulSoup(itemPlaceNoSpace,"html.parser")
        soup3 = BeautifulSoup(itemDateNoSpace,"html.parser")
        itemDateNoSpaceReal = soup3.text
        itemPlaceNoSpaceReal = soup2.text
        #place e özel ayarlama
        itemPlaceNoSpaceReal = itemPlaceNoSpaceReal.replace("\n","")
        itemPlaceNoSpaceReal = itemPlaceNoSpaceReal.replace("   ","")
        #Verilerin YAzdırılması
        print("*************************")
        print(f"İlanı Adı: {itemNames}")
        print(f"İlan Fiyatı: {itemPrices} TL")
        print(f"İlan Tarihi: {itemDateNoSpaceReal}")
        print(f"İlan Lokasyonu: {itemPlaceNoSpaceReal}")

        fiyatListesi.append(itemPricesInt)
        
    print("*********Ucuzdan Pahalıya Doğru Sıralama")
    fiyatListesi.sort()
    
    
    
    driver.quit()
print("Sahibinden.com Veri Tarayıcıya Hoş Geldiniz...")
adress = input("Adres Giriniz: ")
veriCek(PATH,adress)
os.system("Pause")