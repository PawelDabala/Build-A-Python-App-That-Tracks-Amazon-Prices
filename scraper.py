import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7iii&qid=1581288523&sr=8-3'

headers = {'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.72'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[:5])

    if (converted_price > 1.700):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pdabala@gmail.com', 'Okutel098!@#')

    subject = 'Price fell down!'
    body = 'Check the amazon link'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pdabala@gmail.com',
        'pdabala@gmail.com',
        msg
    )

    print("Hey Email Has been sent")

    server.quit()



while(True):
    check_price()
    time.sleep(60*60)


