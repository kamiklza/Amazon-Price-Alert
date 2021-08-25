import requests
from bs4 import BeautifulSoup
import smtplib
import os


my_email = os.environ["GMAIL"]
my_password = os.environ["GMAIL_PSW"]

TARGET_PRICE = 130

product_url = "https://www.amazon.com/Medify-Air-MA-15-Purifier-filter/dp/B089CBRBVX/ref=sr_1_2_sspa?dchild=1&keywords=dyson&qid=1629874067&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKQkpFUFBTNlI0MVQmZW5jcnlwdGVkSWQ9QTAwODU4MTYzMVpSUDhTTDZFVzMwJmVuY3J5cHRlZEFkSWQ9QTA3MjI4NTMzTDhPV0E2MUtCMzUmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"

header = {
    "User-Agent": "Chrome",
    "Accept-Language": "en-US"
}
response = requests.get(url=product_url, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
price_tag = soup.find(name="span", id="price_inside_buybox").getText()
price = float(price_tag.replace("$", ""))

product_title = soup.find(name="span", id="productTitle").getText().strip()

if price <= TARGET_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="kamiklza@hotmail.com",
                        msg=f"Subject: Amazon Low Price Alert!\n\n"
                         f"The {product_title} is now at ${price}, below your target price ${TARGET_PRICE}!")

else:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="kamiklza@hotmail.com",
                        msg=f"Subject: Your amazon wish item still not reach your price target\n\n"
                            f"The {product_title} is now at ${price}, above your target price ${TARGET_PRICE}..")



