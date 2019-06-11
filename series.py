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


split1 = name_list.split("': {'name': '")
index = 0
supplier_table = PrettyTable(['SN', 'Brand'])
ind = 1
while index < len(split1)-1:
    split2 = split1[index+1].split("', 'selected'")
    index = index + 1
    supplier_table.add_row([str(ind), split2[0]])
    ind = ind + 1

print(supplier_table)

stop = time.time()

print('Took %.2f seconds to execute.' %(stop - start))

