import requests
import requests
import json
from bs4 import BeautifulSoup
import xlsxwriter
import re
import csv


file = open('category.txt','r')

for f in file:
    data = f.replace('\n','')

    data = data.split('===')

    url = data[2] + '?product_list_limit=all'

    print (url)

    response = requests.request("GET", url)
    html1 = BeautifulSoup(response.content, 'html.parser')

    try:

        prd = html1.find('ol',{'class':'products list items product-items'})

        products = prd.find_all('li')

        for product in products:
            try:
                product_name = product.find('a',{'class':'product-item-link'})

                name = product_name.text.strip()
                prodcut_url = product_name.get('href')

                price = 'None'
                image = 'None'

                try:
                    prc = product.find('span',{'class':'price'})
                    price = prc.text.strip()

                    print (price)

                except:
                    print ("P error")

                try:
                    img = product.find('img',{'class':'product-image-photo default_image'})
                    image = img.get('src')

                    print (image)

                except:
                    print ("P error")

                file = open('list.txt', 'a+')
                file.write(str(data[0]) + '===' + str(data[1]) + '===' + str(name) + '===' + str(prodcut_url) + '===' + str(price) + '===' + str(image) +'\n')
                file.close()

            except:
                print ("error")

    except:
        print ("Erorr")
        erroe = open('error.txt', 'a+')
        erroe.write(str(data[0]) + '===' + str(data[1]) + '===' + str(url)  + '\n')
        erroe.close()



