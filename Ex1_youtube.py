from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen (url)

raw_data = conn.read ()
html_content = raw_data.decode ("utf-8")

soup = BeautifulSoup (html_content, "html.parser")

section = soup.find ("section", "section chart-grid")
li = section.div.ul
li_list = li.find_all ("li")

for i in li_list:
    name = i.h3.string
    artist = i.h4.string
    options = {
        "default_search": "ytsearch",
        "max_downloads": 1,
        "format": "bestaudio/audio",
    }
    dl = YoutubeDL (options)
    dl.download ([name + artist])