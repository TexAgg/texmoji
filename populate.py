from modules.data_getter import data_getter
import json
import os

# http://unicode.org/emoji/charts/full-emoji-list.html
# https://github.com/TexAgg/TamuHack/blob/master/hackgetter.py
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

dg = data_getter('http://unicode.org/emoji/charts/full-emoji-list.html')
data = dg.scrape()

directory = "data"
if not os.path.exists(directory):
    os.makedirs(directory)
with open('data/emojis.json', 'w') as outfile:
    json.dump(data, outfile)