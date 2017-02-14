import urllib
from bs4 import BeautifulSoup
import img
import os
import collections

class data_getter:

	def __init__(self, url):
		self.url = url
		r = urllib.urlopen(self.url).read()
		self.soup = BeautifulSoup(r, "html.parser")
		# Use an OrderedDict so all the best emojis are first.
		# (It says python 3 but it still works)
		# https://docs.python.org/3/library/collections.html#collections.OrderedDict
		self.emojis = collections.OrderedDict()

	def scrape(self):
		rows = self.soup.find_all("tr")

		for row in rows:
			cols = row.find_all("td")
			if len(cols) != 0:
				# Save the raw image as a png.
				# Use the index 1 to save the Apple emojis.
				# Use the index 0 to save the standard emojis.
				# Nobody cares about the other formats.
				raw_img = row.findAll('img')[1]['src']
				if not os.path.exists("img"):
					os.makedirs("img")
				img.save_raw_img(raw_img[22:], "img/" + cols[0].string + ".png")

				# add the emoji to the dict.
				self.emojis[cols[0].string] = {
					'id': cols[0].string,
					'name': cols[16].string,
					# Get only the first code.
					'unicode': cols[1].string.split(' ')[0],
					'img': "img/" + cols[0].string + ".png"
				}

		return self.emojis
