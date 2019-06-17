import re

import requests
import urllib.request
import time
import json

start = time.time()

from bs4 import BeautifulSoup
from prettytable import PrettyTable

import csv

# Set up the base URL
url = "https://www.druckerzubehoer.de/shop/subcategory/vcatid/DV-TinteToner/catid/D-3_M_LAS/lng/de_DE/site/1/lng/de_DE"

response = requests.get(url)

# Parsing the response to HTML using beautiful soup
soup = BeautifulSoup(response.text, "html.parser")
font = soup.findAll('script')

link = soup.findAll('href')

print('a')

for url in soup.findAll('a', {'class':'item'}):
    print(url['a'])


# # Getting response from the base URL
# response = requests.get(url)
#
# # Parsing the response to HTML using beautiful soup
# soup = BeautifulSoup(response.text, "html.parser")
#
# font = soup.findAll('script')
#
# category_list = (font[11]).text.split('=')
#
# original_list = (category_list[119])
#
# original_list = original_list.split("preselected_cat_id")[0]
#
# original_list = original_list.strip()
#
# original_list = original_list.split(";")[0] + original_list.split(";")[1] + original_list.split(";")[2]
#
# json_data = json.loads(original_list)
#
# name_list = ""
#
# for (k, v) in json_data.items():
#     # print("Key: " + k)
#
#     value_json = str(v)
#
#     name_list = value_json.strip('[]')
#     # print(name_list)
#
# split1 = name_list.split(
#     "', 'selected': False, 'topseller_groups': [], 'topseller_subcategories': [], 'groups': []}, '")
# # print(split1)
# index = 0
#
# split_brand = name_list.split("': {'name': '")
# index_brand = 0
#
# ind = 1
#
# # supplier_table2 = PrettyTable(['SN', 'Brand'])
#
# # while index_brand < len(split_brand)-1:
# # split_brand2 = split_brand[index_brand+1].split("', 'selected'")
# # index_brand = index_brand + 1
# # supplier_table2.add_row([str(ind), split_brand2[0]])
# # ind = ind + 1
#
# # supplier_table = PrettyTable(['SN', 'Brand', 'Series', 'Series Link'])
# # print(len(split1))
#
# with open('brand_data.csv', mode='w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     while index < len(split1) or index_brand < len(split_brand) - 1:
#         spp = split1[index]
#         # split_brand2 = split_brand[index_brand + 1].split("', 'selected'")
#         # print(split1)
#         # break
#
#         if index == 0:
#             split2 = spp.split("{'")[1].split(",")[0]
#             # print(split2)
#             # break
#             split_brand2 = split_brand[index_brand + 1].split("', 'selected'")
#             link_generate = "https://www.druckerzubehoer.de/shop/subcategory/vcatid/DV-TinteToner/catid/" + split2 + "/lng/de_DE/site/1/lng/de_DE"
#             # print(link_generate)
#             for link_generate in soup.findAll('a', {'class': 'item'}):
#                 print(link_generate['href'])
#
#             # supplier_table.add_row([str(index + 1), split_brand2[0], split2, link_generate])
#             # csv_writer.writerow([str(index + 1), split_brand2[0], split2, link_generate, ])
#
#         else:
#             split2 = spp.split("': {'name': '")[0].split(",")[0]
#             split_brand2 = split_brand[index_brand + 1].split("', 'selected'")
#             link_generate = "https://www.druckerzubehoer.de/shop/subcategory/vcatid/DV-TinteToner/catid/" + split2 + "/lng/de_DE/site/1/lng/de_DE"
#
#             for link in soup.findAll('a', {'class': 'item'}):
#                 print(link_generate['href'])
#             # supplier_table.add_row([str(index + 1), split_brand2[0], split2, link_generate])
#             # csv_writer.writerow([str(index+1), split_brand2[0], split2, link_generate, ])
#         # link_generate = "https://www.druckerzubehoer.de/shop/subcategory/vcatid/DV-TinteToner/catid/"+split2+"/lng/de_DE/site/1/lng/de_DE"
#         # index_brand = index_brand + 1
#
#         index = index + 1
#
# # print(supplier_table)

stop = time.time()

print('Took %.2f seconds to execute.' % (stop - start))
