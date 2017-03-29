import requests
from bs4 import BeautifulSoup
import html.parser
import pdb
from pdb import set_trace as bp

def crawl_web(max_page):
    fr = open('Test_for_Data_From_Webpage_2.txt', 'r')
    page=2
    while page<max_page:
        url="https://www.snapdeal.com/products/mobiles-mobile-phones?q=Price%3A2000%2C4999%7C&sort=plrty"
        text = requests.get(url)#gets all stuff from that url into text
        plain_data = text.text#converts text into string format with naem plain_data
        soup = BeautifulSoup(plain_data,"html.parser")#Beautiful Soup objects can be manipulated in many ways hence the creation of soup
        for headerfiles in soup.findAll('a',{'target':'_blank'}):
            href=fr.read()
            print(href)
            get_price_of_item(href)



def get_price_of_item(item_url):
    fw = open('Data_From_Webpage_3.txt', 'w')
    text = requests.get(item_url)  # gets all stuff from that url into text
    plain_data = text.text  # converts text into string format with naem plain_data
    soup = BeautifulSoup(plain_data,"html.parser")  # Beautiful Soup objects can be manipulated in many ways hence the creation of soup
    for price in soup.findAll('span', {'class':'payBlkBig'}):#a is the anchor for links and attribute:pair is specified for selecting specific elements in the page
        rate=price.get('itemprop')
        classattributedata = price.string
        print(classattributedata)
        #fw.write(str(classattributedata) + "\n")



        #fw.close()




#get_price_of_item("https://www.snapdeal.com/product/micromax-bolt-q381-8gb-black/671635823112")
crawl_web(3)
