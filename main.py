import requests
from bs4 import BeautifulSoup as BS
import csv

p = 1

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


# class Printer:
#     Name = ""
#     Actual = ""
#
#     def __init__(self, n, a):
#         self.Name = n
#         self.Actual = a

result_data = []
while True:
    url = "https://global.pantum.com/product-center/p-" + str(p) + "/#content"
    page = requests.get(url, headers=headers)
    save_data = page.text
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(save_data)

    with open("index.html") as file:
        data = file.read()

    soup = BS(data, 'html.parser')
    is_new_hot_device = printers = None
    have_data = True
    try:
        is_new_hot_device = soup.find("div", class_="pro_list cf").find_all("span")
        printers = soup.find("div", class_="pro_list cf").find_all("dd")
        list(is_new_hot_device)
        list(printers)
    except Exception:
        have_data = False

    # with open("pantum_result_data.csc", "w") as file:
    #     wr = csv.writer(file)
    #     wr.writerow(
    #         ("Название_модели", "Актуальность")
    #     )

    if have_data and len(printers):
        for i in range(0, len(printers)):
            if i >= len(is_new_hot_device):
                #print(printers[i].text.strip())
                result_data.append(printers[i].text.strip())
            elif len(is_new_hot_device):
                #print(printers[i].text.strip() + " " + is_new_hot_device[i].text.strip().upper())
                result_data.append(printers[i].text.strip() + " " + is_new_hot_device[i].text.strip().upper())
        p += 1
    else:
        break
print(result_data)
with open("pantum_result_data.csv", "w") as file:
    wr = csv.writer(file)
    wr.writerow(
            ("Название_модели", "Актуальность")
       )

with open("pantum_result_data.csv", "a") as file:
    wr = csv.writer(file)
    wr.writerows(
        result_data
    )
