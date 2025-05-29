import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get ("https://www.zigwheels.com/tata-cars")
soup = BeautifulSoup (response.content,"html.parser")
names = soup.find_all ('div', class_ = "_col-md-6.col-sm-6.col-xs-12")
name =[]
for i in names[0:12]:
     d=i.get_text()
     name.append(d)
print(names)
prices = soup.find_all('div', class_="_clr_bl.fnt-16.b.i-b")
prices = []
for i in prices [0:12]:
    d = i.get_text()
    prices.append(d)
print(prices)
ratings = soup.find_all ('span', class_="_r-n.g")
rate = []
for i in ratings[0:12]:
    d=i.get_text()
    rate.append(float(d))
    print(rate)
reviews = soup.find_all('span', class_="_mr-10.pull-left.fnt-14.lnk-c")
review = []
for i in reviews[0:12]:
    d=i.get_text()
    review.append(d)
    print(review)
features = soup.find_all('a', class_="_clr.lnk-c.fnt-16")
feature = []
for i in features[0:12]:
    d = i.get_text()
    feature.append(d)
    print(feature)
links = soup.find_all('div', class_="_p-15 pt-10 mke-ryt rel")
link = []
for i in links[0:12]:
    d = "https://www.fliplart.com"+i['href']
    link.append(d)
    print(link)
images = soup.find_all('img', class_="_text-center.img-responsive.zw-cmn-cursorPointer")
image = []
for i in image[0:12]:
    d-i['src']
    image.append(d)
    print(image)

df=pd.DataFrame()
df["Names"]=name
df["Prices"]=prices
df["RatingS"]=rate
df["Images"]=image
df["Links"]=link

df.to_csv("Mobiles.csv")

