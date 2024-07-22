from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "https://www.basketball-reference.com/players/j/jamesle01.html"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#print(soup.get_text())


chosen_year = "2004"
chosen_stat = "pts_per_g"
table_data = (soup.find(id=f'per_game.{chosen_year}'))
#print(table_data.contents)
#data_point = table_data.find(data-stat=f'{chosen_stat}')
data_point = table_data.find(attrs={"data-stat": f'{chosen_stat}'})
print(data_point.string)
