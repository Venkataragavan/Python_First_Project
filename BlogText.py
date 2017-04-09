import urllib
import requests
import operator
from bs4 import BeautifulSoup
import html.parser
from collections import Counter
import os.path
import Obtain_URLSet




def get_data(urlstring,start):
    save_path='C:\\Users\\Venkataragavan C\\Documents\\PythTest\\Data_From_Cricket_Monthly'
    #print("Save Path created")
    blog1 = os.path.join(save_path,"CM"+str(start)+".txt")
    blog2 = open(blog1, 'w')
    data=requests.get(urlstring).text
    #print("Data obtained from URL")
    wordlist={}
    soup=BeautifulSoup(data,"html.parser")
    #print("Soup object craeatdd")
    for item in soup.findAll('article',{'class': 'story_body'}):
        #print("ID found!")
        text=item.get_text()
        blog2.write(text)
        break
    #for item in soup.findAll('section',{'class':'video_section'}):
     #   print("Husk found")
      #  husk=item.get_text()
       # print("Husk is "+husk)
        #with open('C:\\Users\\Venkataragavan C\\Documents\\PythTest\\Data_From_Cricket_Monthly\\CM'+str(start)+'.txt','r') as infile:
         #   filedata=infile.read()
          #  husklist=list
           # husklist=husk.split(" ")
            #print('HuskList is '+str(husklist))
            #for item in husklist:
             #   filedata=filedata.replace(item,'')
        #with open('C:\\Users\\Venkataragavan C\\Documents\\PythTest\\Data_From_Cricket_Monthly\\CM'+str(start)+'.txt','w') as file:
         #   file.write(filedata)
            #print("Husk replaced")





    #print("Exited from first string")
    print("File "+str(start)+" finished")







#Obtain_URLSet.get_urlset("http://thecricketmonthly.com/")
url=open("URL_SET.txt",'r')
startfile=0
for i in url.readlines():
    Url="http://thecricketmonthly.com"+str(i)
    get_data(Url,startfile)
    startfile+=1





