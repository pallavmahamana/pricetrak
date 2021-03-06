import requests
from bs4 import BeautifulSoup


HEADERS = {
'authority': 'www.flipkart.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

# this class might not work, cause tata cliq is updating dom with javascript.
class FlipkartTracker:

	def __init__(self,url):
		self.url = url
		self.soupify()


	def soupify(self):
		r = requests.get(self.url,  headers=HEADERS)
		self.soup = BeautifulSoup(r.text,"lxml")

	def get_product_name(self):
		return self.soup.find("span",{"class":"B_NuCI"}).text.replace('\n','')


	def get_price(self):
		price_tag = self.soup.find("div",{"class":"_30jeq3 _16Jk6d"})
		return float(price_tag.text[1:].replace(',',''))





