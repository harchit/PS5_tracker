import requests
import bs4
from bs4 import BeautifulSoup
import time
from requests_html import HTMLSession
from twilio.rest import Client
from credentials import auth_token, account_sid, my_cell, my_twilio

client = Client(account_sid, auth_token)

def getPrice():
    page= 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_10?dchild=1&keywords=ps5&qid=1620620418&sr=8-10'
    s = HTMLSession()
    #check webpage every 5 minutes
    while True:
        r = s.get(page)
        r.html.render(sleep=1)
        available = r.html.xpath('//*[@id="availability"]/span/text()', first=True)
        
        #check if its available and send a text
        if (available and not available.strip()=='Currently unavailable.'):
            msg_twilio = client.messages.create(
            body= 'ps5 in stock at '+ page,
            from_= my_twilio,
            to= my_cell)

        time.sleep(5*60)

getPrice()