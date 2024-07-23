from bs4 import BeautifulSoup
from urllib.request import urlopen
player_url = "https://www.basketball-reference.com/players/q/quetane01.html"
page = urlopen(player_url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

table_data = soup.find(id="per_game")
table_data_career_row = table_data.find(string="Career").find_previous("tr")

print(table_data_career_row.find(attrs={"data-stat":  "pts_per_g"}).string)
