from bs4 import BeautifulSoup
import requests


cathie_html=requests.get('https://www.bucketfox.com/etf/ARKK').text
# print(cathie_html)

html_text=requests.get("https://cathiesark.com/arkk/performance").text
# print(html_text)

soup=BeautifulSoup(html_text,'lxml')

cat=soup.find_all('span',class_='numberText')
# cathie=soup.find_all

