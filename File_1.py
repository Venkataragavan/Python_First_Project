from urllib import request
import urllib
from bs4 import BeautifulSoup
import requests
import html.parser

#Get links from URL
def get_phone_links(url):
    data=requests.get(url).text
    soup=BeautifulSoup(data,'html.parser')
    for item in soup.findAll('h2',{'class':'a-size-base a-color-null s-inline scx-truncate s-access-title a-text-normal'}):
        nameproduct=item["data-attribute"]
        print(nameproduct)
    for link in soup.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
        price=link.get_text()
        print(price)

get_phone_links('http://www.amazon.in/s/ref=lp_1389401031_nr_p_36_2?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_36%3A1318505031&bbn=1389401031&ie=UTF8&qid=1491809056&rnid=1318502031')

