from bs4 import BeautifulSoup
from urllib.request import urlopen
def getCareerStat(stat_name, url):
    player_url = f'https://www.basketball-reference.com/{url}'
    page = urlopen(player_url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    stat_name = stat_name
    table_data = soup.find(id="per_game")
    table_data_career_row = table_data.find(string="Career").find_previous("tr")

    print(table_data_career_row.find(attrs={"data-stat":  "pts_per_g"}).string)
    print(soup.find("h1").contents[1].string)

