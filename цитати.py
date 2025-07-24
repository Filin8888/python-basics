import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"


 # створюємо csv файл
with open("quotes.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Цитата", "Автор", "Теги"])  # Заголовки стовпців

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")           

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = quote.find("div", class_="tags").find_all("a", class_="tag")
            tag = ", ".join(tag.text for tag in tags)

        

            writer.writerow([text, author, tag])


        # кнопкa Next
        next_button = soup.find("li", class_="next")
        if next_button:
            next = next_button.a["href"]
            url = "https://quotes.toscrape.com/" + next
        else:
            break



print("Дані успішно записані у quotes.csv")