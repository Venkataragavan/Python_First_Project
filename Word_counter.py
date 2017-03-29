import requests
from bs4 import BeautifulSoup
import html.parser

def WordCounter(url):
    word_list = []

    content = requests.get(url).text

    soup = BeautifulSoup(content,"html.parser")

    for each_word in soup.findAll('span', {'class':'label'}):
        every_word=each_word.string
        words = content.lower().split()
        for every_word in words:
            print(str(every_word))
            word_list.append(str(every_word))

    clean_list(word_list)

def clean_list(word_list):
    clean_word_list = []
    for word in word_list:
        crap = "!@#$%^&*()_+:\"{}?><,./'';][=-~`"
        for x in range(0,len(crap)):
            word = word.replace(crap[x],"")



WordCounter("http://codepad.org/")

