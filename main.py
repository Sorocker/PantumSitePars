import requests
from bs4 import BeautifulSoup as BS
import csv

p = 1

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

with open("pantum_result_data.csv", 'w', newline='', encoding='utf-8') as file:
    wr = csv.writer(file)
    wr.writerow(("Название_модели", "Актуальность"))

    while True:
        url = f"https://global.pantum.com/product-center/p-{p}"
        page = requests.get(url, headers=headers)
        soup = BS(page.text, 'html.parser')
        cards = soup.find(class_="pro_list")
        if not cards:
            break
        for card in cards("dl"):  # cards.find_all("dl")
            is_new_hot_device = card.find("span")
            is_new_hot_device = is_new_hot_device.text if is_new_hot_device else None
            printer = card.find("dd").text.strip()

            wr.writerow((printer, is_new_hot_device))
        p += 1
