import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/dp/B00ZV9RDKK/?ref_=ods_gw_d_h1_smp_tk_blue&pf_rd_p=97c6d809-e3c7-4461-9ca5-1fac6ee68f94&pf_rd_r=T30ADK1BPBHXMYK6WWXK")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id":"priceblock_ourprice", "class":"a-size-medium a-color-price"})
string_price = (element.text.strip()) # "39.99
price_wihtout_symbol = string_price[1:]
price = float(price_wihtout_symbol)

if price < 65:
    print("Buy the firestick!")
    print("The current price is {}.".format(string_price))
else:
    print("DO NOT buy the firestick. Too expensive!")

#print(price_wihtout_symbol)