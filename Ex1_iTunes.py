from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen (url)

raw_data = conn.read ()
html_content = raw_data.decode ("utf-8")

soup = BeautifulSoup (html_content, "html.parser")

section = soup.find ("section", "section chart-grid")
li = section.div.ul
li_list = li.find_all ("li")

song_list = []
for i in li_list:
     name = i.h3.string
     artist = i.h4.string
     song_dict = {
        "Name": name,
        "Artist": artist,
    }
     song_list.append (song_dict)

pyexcel.save_as (records = song_list, dest_file_name = "top_song.xlsx")