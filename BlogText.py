import urllib
import requests
import operator
from bs4 import BeautifulSoup
import html.parser
from collections import Counter
import os.path
import Obtain_URLSet
import _codecs




def get_data(urlstring,start,savepath):
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    #print("Save Path created")
    blog1 = os.path.join(savepath,"CM"+str(start)+".txt")
    blog2 = open(blog1, 'w')
    data=requests.get(urlstring).text
    #print("Data obtained from URL")
    wordlist={}
    soup=BeautifulSoup(data,"html.parser")
    #print("Soup object craeatdd")
    for item in soup.findAll('article',{'class': 'story_body'}):
        #print("ID found!")
        try:
            text=item.get_text()
            blog2.write(text+"/n")
            #print("remove husk function done")
            break
        except:
            blog2.write("Error resulted while extracting from the link")
            pass


    print("File "+str(start)+" finished")



def get_husk(URL,start):
    URLdata=requests.get(URL).text
    soupdata=BeautifulSoup(URLdata,'html.parser')
    huskfile = open("C:\\Users\\Venkataragavan C\\PycharmProjects\\TCM\\Huskdata"+str(start)+".txt", 'w')
    for item in soupdata.findAll('section',{'class':'image_large'}):
        huskdata=item.get_text()
        huskfile.writelines(huskdata)
    print("Husk writing is done")






#Obtain_URLSet.get_urlset("http://thecricketmonthly.com/")
url=open("URL_SET.txt",'r')
startfile=0
SAVEPATH=input("Enter the path where your files are to be saved (Default is the directory created inside the Program path)"+"\n")
for i in url.readlines():
    Url="http://thecricketmonthly.com"+str(i)
    get_data(Url,startfile,SAVEPATH)
    get_husk(Url,startfile)
    startfile+=1





