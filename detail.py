import requests
import requests
import json
from bs4 import BeautifulSoup
import xlsxwriter
import re
import csv


file = open('list.txt','r')

for f in file:
    data = f.replace('\n','')

    data = data.split('===')

    url = data[3]

    print (url)

    response = requests.request("GET", url)
    html1 = BeautifulSoup(response.content, 'html.parser')

    short_desc = ''

    try:
        s_de


    except:
        print ("Erorr")

