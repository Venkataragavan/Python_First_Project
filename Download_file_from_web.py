from urllib import request
import sys

ExcelFile = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=1&b=25&c=2017&d=2&e=25&f=2017&g=d&ignore=.csv"

def download_files_from_web(url):
    response= request.urlopen(url)#connect oto the webpage
    exceldata=response.read()#read data from that webpage and store in exceldata
    stringexceldata=str(exceldata)#convert to string
    lines = stringexceldata.split("\\n")#break into lines
    fw=open('RandomExcelData.txt','w')
    for everyline in lines:
        fw.write(everyline+"\n")
    fw.close()

download_files_from_web(*sys.argv)


