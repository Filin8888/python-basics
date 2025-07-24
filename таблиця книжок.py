import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("books.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Назва", "Ціна", "Рейтинг"])  # Заголовки стовпців

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating_class = book.p["class"]
        rating = rating_class[1]

        writer.writerow([title, price, rating])

print("Дані успішно записані у books.csv")
