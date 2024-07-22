from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "https://www.basketball-reference.com/players/j/jamesle01.html"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#print(soup.get_text())


table_data = soup.find(id="per_game")
table_data_career_row = table_data.find(string="Career").find_previous("tr")

print(table_data_career_row.find(attrs={"data-stat":  "pts_per_g"}).string)

