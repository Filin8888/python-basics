import requests
import csv

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Сортуємо валюти за курсом (від більшого до меншого)
    sorted_data = sorted(data, key=lambda x: x["rate"], reverse=True)

    # Беремо топ-10
    top_currencies = sorted_data[:10]

    # Запис у CSV
    with open("nbu_top10.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Назва", "Код", "Курс (грн)", "Дата"])

        for currency in top_currencies:
            writer.writerow([
                currency["txt"],
                currency["cc"],
                currency["rate"],
                currency["exchangedate"]
            ])

    print("✅ Дані збережено у nbu_top10.csv")

else:
    print("❌ Помилка запиту:", response.status_code)
