# Day 47 Project - Automated Amazon Price Tracker

from bs4 import BeautifulSoup
import requests
import smtplib

header = {
    "User-Agent": "User-Agent",
    "Accept-Language": "Accept-Language"
}

url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=lp_16225009011_1_2"

response = requests.get(url, headers=header)
amazon_webpage = response.content

soup = BeautifulSoup(amazon_webpage, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 250

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
