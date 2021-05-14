import requests
import requests
import json
from bs4 import BeautifulSoup
import xlsxwriter
import re
import csv



file = open('demo.html','r')

for f in file:


    html1 = BeautifulSoup(str(f), 'html.parser')

    categories = html1.find_all('li',{'class':'ui-menu-item level1 parent'})

    for cat in categories:
        # print (cat.text.strip())

        category= cat.find('span').text.strip()

        uls = cat.find_all('li',{'class':'ui-menu-item level2'})

        for ul in uls:
            subcategory = ul.text.strip()

            a_tag = ul.find('a')

            file = open('category.txt','a+')
            file.write(str(category) + '===' + str(subcategory) + '===' + str(a_tag.get('href')) + '\n')

        print ('\n\n')