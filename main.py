import requests
from bs4 import BeautifulSoup as BSP  # Import important libs

url = "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%92%D0%BE%D0%BB%D0%B3%D0%BE%D0%B4%D0%BE%D0%BD%D1%81%D0%BA%D0%B5"  # Here need to choose link on city whats you need on rp5 site (https://rp5.ru/)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

r = requests.get(url, headers=headers)
r.encoding = "utf-8"

html = BSP(r.text, features="html.parser")

temp_element = html.find(class_="t_0")

if temp_element:
    print(f"Температура выбранного города: {temp_element.text}")
else:
    print("Не удалось найти элемент с таким классом")
