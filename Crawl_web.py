import requests
from bs4 import BeautifulSoup
import html.parser

def crawl_web(max_page):
    fw = open('Data_From_Webpage.txt', 'w')
    page=2
    while page<max_page:
        url="http://www.pythonforbeginners.com/basics/?page="+str(page) #specify the URL of the page you want to crawl
        text = requests.get(url)#gets all stuff from that url into text
        plain_data = text.text#converts text into string format with naem plain_data
        soup = BeautifulSoup(plain_data,"html.parser")#Beautiful Soup objects can be manipulated in many ways hence the creation of soup
        for headerfiles in soup.findAll('a',{'rel':'bookmark'}):#a is the anchor for links and attribute:pair is specified for selecting specific elements in the page
            classattributedata=headerfiles.get('href')#to get value in href
            title = headerfiles.string# to get string parts from 'a'
            fw.write("http://www.pythonforbeginners.com"+classattributedata+"\n")
            fw.write(title+"\n")
        fw.close()


        page+=1


crawl_web(3)
