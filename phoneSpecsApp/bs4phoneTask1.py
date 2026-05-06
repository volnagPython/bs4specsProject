#Jan. 8, 2025 - Apr.16 2026
import os
import json
import requests
from bs4 import BeautifulSoup

url = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_15_128GB_Black-p1044347.html'

############################
#Проверим подключение:
response = requests.get(url)
# print("Connection :", response.status_code)

if response.status_code != 200:
    print("--Failed to connect--")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
############### Fetching the characteristics of the phone  ###########
box_specs = soup.find("div", class_="br-pr-chr")
specs = box_specs.find_all("div", class_="br-pr-chr-item", recursive = False)

dict_specs = {};keys=[];values=[]
################################################################################
for i in range(len(specs)):
    tags = specs[i].find_all("span")
    for i in range(len(tags)):
        if i%2 == 0:
            ##print("**",i,"**",type(tags), "---->",tags[i].get_text(strip=True))
            key = tags[i].get_text(strip=True); keys.append(key)
        if i%2 == 1:
            ## print("**", i, "**", type(tags), "---->", tags[i].get_text(strip=True))
            value = tags[i].get_text(strip=True).replace("\xa0", ""); values.append(value)   # ;i=i+2
        else:
            continue
        dict_specs[key] = " ".join(value.split())
print(70*"-")
print("Dictionary:",dict_specs)

#############################################################################
########################### Cell's Photos #######################################
photos=[]
img_box = soup.find_all("img");i=0

for items in img_box:
    if items:
        image_url = (items.get("data-src") or items.get("src") or items.get("srcset"))#
        if image_url:
            if any(image_url.lower().endswith(ext) for ext in
                   [".jpg", ".jpeg", ".webp"]):  # if at least one of the conditions is True.
                #print(image_url)
                i += 1;photos.append(image_url)
            else:
                pass
        else:
            pass

    else:
        pass

print(70*"-")
# print (f"*** Found {i} images of the phone ***")
# print(40 * "-");print(photos)
############# Writing data into a json file ##################
# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, "res_bs4_specs.json")
# with open(file_path, "w", encoding="utf-8") as f:
#     json.dump(dict_specs, f, ensure_ascii = False, indent = 4)
############# In case we need it    ##################