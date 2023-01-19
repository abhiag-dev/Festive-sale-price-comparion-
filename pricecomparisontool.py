from bs4 import BeautifulSoup
import requests
import html5lib
import smtplib

def tracker():
    flipkartUrl = input('Enter the flipkart product  ')
    amazonUrl = input('Enter the amazon product  ')
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    if  amazonUrl:
        flipkartResponse =requests.get(flipkartUrl,headers=headers)
        amazonResponse =requests.get(amazonUrl,headers=headers)
        flipkartSoup=BeautifulSoup(flipkartResponse.content,'html5lib')
        amazonSoup=BeautifulSoup(amazonResponse.content,'html5lib')
        flipkartProductPrice=float(flipkartSoup.find('div',attrs='_30jeq3 _16Jk6d').text.replace(',','')[1:])
        amazonProductPrice=amazonSoup.find('span',{'class':'a-price-whole'}).text 
        print("Flipkart  :  ",str(flipkartProductPrice))
        print("Amazon   :  ",str(amazonProductPrice))



tracker()