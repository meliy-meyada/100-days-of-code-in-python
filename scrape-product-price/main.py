import requests
from bs4 import BeautifulSoup
import smtplib
import lxml


URL = "https://www.amazon.com/dp/B07PQXHP1J/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B07PQXHP1J&pd_rd_w=ZCWeo&pf_rd_p=9fd3ea7c-b77c-42ac-b43b-c872d3f37c38&pd_rd_wg=BCa1V&pf_rd_r=2FJKJ9XM3CP2XYXERHE9&pd_rd_r=a33854a4-ee25-4c30-a9ff-d88b5bc23b36&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExU1lIREszT1ZZN1c4JmVuY3J5cHRlZElkPUEwNTU3Nzg3SjlDS0lUSlBSN1lIJmVuY3J5cHRlZEFkSWQ9QTAxOTM3NjdLUzIyMFZRSDFYNDEmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=header)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "lxml")

price = soup.find(name="span", class_="a-size-medium a-color-price").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
EMAIL_SMTP = "Your smtp Email"
MY_EMAIL = "Your Email"
MY_PASSWORD = "Your Password"


if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(EMAIL_SMTP, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )