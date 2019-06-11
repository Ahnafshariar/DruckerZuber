import requests
import urllib.request
import time
import json

start = time.time()

from bs4 import BeautifulSoup
from prettytable import PrettyTable

# Set up the base URL
url = "https://www.druckerzubehoer.de/shop/subcategory/vcatid/DV-TinteToner/catid/D-Brother/lng/de_DE/site/1/lng/de_DE"

# Getting response from the base URL
response = requests.get(url)

# Parsing the response to HTML using beautiful soup
soup = BeautifulSoup(response.text, "html.parser")

font = soup.findAll('script')

category_list = (font[11]).text.split('=')

original_list = (category_list[119])

original_list = original_list.split("preselected_cat_id")[0]

original_list = original_list.strip()

original_list = original_list.split(";")[0] + original_list.split(";")[1] + original_list.split(";")[2]

json_data = json.loads(original_list)

name_list = ""

for (k, v) in json_data.items():
    #print("Key: " + k)

    value_json = str(v)

    name_list = value_json.strip('[]')
    # print(name_list)


split_brand = name_list.split("': {'name': '")
index_brand = 0
supplier_table = PrettyTable(['SN', 'Brand'])
ind = 1
while index_brand < len(split_brand)-1:
    split_brand2 = split_brand[index_brand+1].split("', 'selected'")
    index_brand = index_brand + 1
    supplier_table.add_row([str(ind), split_brand2[0]])
    ind = ind + 1

print(supplier_table)

stop = time.time()

print('Took %.2f seconds to execute.' %(stop - start))

