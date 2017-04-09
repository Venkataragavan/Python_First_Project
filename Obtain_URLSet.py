import urllib
import requests
import operator
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from html.parser import HTMLParser
from collections import Counter
import os.path
import re


def get_urlset(url):
    #print("Starting up")
    #urls = open("url.txt", 'w')
    save_path = 'C:\\Users\\Venkataragavan C\\PycharmProjects\\TCM'
    urlset = os.path.join(save_path, "URL_SET.txt")
    URLSET = open(urlset, 'w')

    data=requests.get(url).text
    #print("Data obtained from site")
    urlset=set()
    finalHREF=set()
    soup=BeautifulSoup(data,"html.parser")
    #print("Soup object created")
    for item in soup.findAll('aside',{'class':'story_details'}):
        a_tag = item.a
        hrefLIST1=set()
        hrefLIST1.add(a_tag)
        #print(hrefLIST1)
        for line in hrefLIST1:
            start=str(line).find('<href="')+9
            end=str(line).find('>')
            halfURL=str(line)[start:end]
            URLlist=list()
            URLlist.append(halfURL)
        #print(URLlist)
        for lineitem in URLlist:
            stripped=lineitem[1:-1]
            URLSET.write(stripped+"\n")







get_urlset('http://thecricketmonthly.com/')