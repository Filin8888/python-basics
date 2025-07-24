import requests
import csv

url = url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Запис у CSV
    with open("crypto_top10.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Назва", "символ", "Поточна ціна", "Капіталізація", "Зміна за 24 години"])

        for crypto in data:
            writer.writerow([
                crypto["name"],
                crypto["symbol"].upper(),
                crypto["current_price"],
                crypto["market_cap"],
                crypto["price_change_24h"]
            ])

    print("✅ Дані збережено у crypto_top10.csv")

else:
    print("❌ Помилка запиту:", response.status_code)
