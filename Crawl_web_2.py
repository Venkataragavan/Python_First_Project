import requests
from bs4 import BeautifulSoup
import html.parser
import pdb
from pdb import set_trace as bp

def crawl_web(max_page):
    fw = open("Data_From_Webpage_2.txt", 'w')
    fr = open('Data_From_Webpage_2.txt', 'r')
    page=2
    #bp()
    while page<max_page:
        url="https://www.snapdeal.com/products/mobiles-mobile-phones?q=Price%3A2000%2C4999%7C&sort=plrty"
        text = requests.get(url)#gets all stuff from that url into text
        plain_data = text.text#converts text into string format with naem plain_data
        soup = BeautifulSoup(plain_data,"html.parser")#Beautiful Soup objects can be manipulated in many ways hence the creation of soup
        for headerfiles in soup.findAll('a',{'target':'_blank'}):
            href=headerfiles.get('href')
            print(str(href))
            fw.write(str(href)+"\n")


        page+=1


def get_price_of_item(item_url):
    fw = open('Data_From_Webpage_1.txt', 'w')
    text = requests.get(item_url)  # gets all stuff from that url into text
    plain_data = text.text  # converts text into string format with naem plain_data
    soup = BeautifulSoup(plain_data,"html.parser")  # Beautiful Soup objects can be manipulated in many ways hence the creation of soup
    for headerfiles in soup.findAll('span', {'itemprop': 'price'}):#a is the anchor for links and attribute:pair is specified for selecting specific elements in the page
        classattributedata = headerfiles.get('href')
        print(classattributedata)
        fw.write(str(classattributedata) + "\n")



        #fw.close()





crawl_web(3)
