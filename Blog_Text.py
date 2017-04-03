import urllib
import requests
import operator
from bs4 import BeautifulSoup
import html.parser
from collections import Counter
import os.path

url="http://www.thecricketmonthly.com/story/1086094/wolf-in-sheep-s-clothing"

def get_data(url):
    save_path='C:\\Users\\Venkataragavan C\\Documents\\PythTest'
    blog1 = os.path.join(save_path,"BlogCM.txt")
    blog2 = open(blog1, 'w')
    data=requests.get(url).text
    wordlist={}
    soup=BeautifulSoup(data,"html.parser")
    for item in soup.findAll('article',{'class': 'story_body'}):
        text=item.get_text()
        blog2.write(text)




get_data(url)


