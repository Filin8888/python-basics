import requests
import csv

query = "python"
url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    books = data["items"][:10]  # топ 10 книг

    # Запис у CSV
    with open("google_books_top10.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Назва", "Автор(и)", "Рейтинг", "Сторінки", "Опис", "Посилання"])

        for book in books:
            info = book["volumeInfo"]
            title = info.get("title", "—")
            authors = ", ".join(info.get("authors", ["—"]))
            rating = info.get("averageRating", "—")
            pages = info.get("pageCount", "—")
            description = info.get("description", "—").replace("\n", " ").strip()
            link = info.get("infoLink", "—")

            writer.writerow([title, authors, rating, pages, description[:200] + "...", link])
            

    print("✅ Дані збережено у google_books_top10.csv")

else:
    print("❌ Помилка запиту:", response.status_code)
