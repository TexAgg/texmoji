import urllib
from bs4 import BeautifulSoup
import img
import os

class data_getter:

	def __init__(self, url):
		self.url = url
		r = urllib.urlopen(self.url).read()
		self.soup = BeautifulSoup(r, "html.parser")
		self.emojis = {}

	def scrape(self):
		rows = self.soup.find_all("tr")

		for row in rows:
			cols = row.find_all("td")
			if len(cols) != 0:
				# Save the raw image as a png.
				raw_img = row.find('img')['src']
				if not os.path.exists("img"):
					os.makedirs("img")
				img.save_raw_img(raw_img[22:], "img/" + cols[0].string + ".png")

				# add the emoji to the dict.
				self.emojis[cols[0].string] = {
					'id': cols[0].string,
					'name': cols[16].string,
					'unicode': cols[1].string,
					'img': "img/" + cols[0].string + ".png"
				}

		return self.emojis
