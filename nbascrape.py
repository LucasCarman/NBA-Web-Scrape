from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import string
import random
import re

def getPlayerImage(player_url):
    player_page_url = f'https://www.basketball-reference.com/{player_url}'
    page = urlopen(player_page_url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    image_url = soup.find("div", class_="media-item").find("img")['src']
    #image_src = re.compile("", image_url[0])
    return(image_url)

def getPpgLeadersDict():
    player_list_dict = {}
    pts_per_game_leader_page = urlopen("https://www.basketball-reference.com/leaders/pts_per_g_career.html")
    html = pts_per_game_leader_page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    ppg_career_table = soup.find(id="all_tot")#.find_previous("table")
    player_links = ppg_career_table.find_all("a")

    for link in player_links:

        player_link = re.findall(f'players.+html', link['href'])[0]
        #player_list_dict[link.text[link.text]].append(player_link)
        player_list_dict[link.text] =  [link.parent.find_next("td").text, player_link]
        #print(player_list_dict)
    return(player_list_dict)


def pickTwoPlayers(player_list_dict):
    player_a = random.choice(list(player_list_dict.items()))
    #print(player_a)
    player_a[1][1] = getPlayerImage(player_a[1][1])
    del player_list_dict[player_a[0]]
    player_b = random.choice(list(player_list_dict.items()))
    player_b[1][1] = getPlayerImage(player_b[1][1])
    return(player_a, player_b)








def getCareerStat(stat_name, url):
    player_url = f'https://www.basketball-reference.com/{url}'
    page = urlopen(player_url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    stat_name = stat_name
    table_data = soup.find(id="per_game")
    table_data_career_row = table_data.find(string="Career").find_previous("tr")
    pts_per_g = table_data_career_row.find(attrs={"data-stat":  "pts_per_g"}).string
    player_name = soup.find("h1").contents[1].string
    return(pts_per_g, player_name)

def getRandomPlayers():
    player_a_options = []
    player_b_options = []
#Pick a random letter to look up players with
    player_a_letter = random.choice(string.ascii_letters).lower()
    player_b_letter= random.choice(string.ascii_letters).lower()

    #Open the player list for that letter
    player_a_letter_url = f'https://www.basketball-reference.com/players/{player_a_letter}/'
    player_b_letter_url = f'https://www.basketball-reference.com/players/{player_b_letter}/'
    player_a_letter_page = urlopen(player_a_letter_url)
    player_b_letter_page = urlopen(player_b_letter_url)
    player_a_letter_html = player_a_letter_page.read().decode("utf-8")
    player_b_letter_html = player_b_letter_page.read().decode("utf-8")
    player_a_letter_soup = BeautifulSoup(player_a_letter_html, "html.parser")
    player_b_letter_soup = BeautifulSoup(player_b_letter_html, "html.parser")
    
    #Find all of the href links to the player pages in the resulting player list page
    player_a_link = player_a_letter_soup.find_all("a")
    for link in player_a_link:
        if link.has_attr('href'):
            if re.findall(f'players.{player_a_letter}.+.html', link['href']) != []:
                #If the link found matches the regex for a player and having the letter we chose earlier, add it to the list of options
                player_a_options.append((re.findall(f'players.{player_a_letter}.+.html', link['href'])[0]))
    
    player_b_link = player_b_letter_soup.find_all("a")
    for link in player_b_link:
        if link.has_attr('href'):
            if re.findall(f'players.{player_b_letter}.+.html', link['href']) != []:
                #If the link found matches the regex for a player and having the letter we chose earlier, add it to the list of options
                player_b_options.append((re.findall(f'players.{player_b_letter}.+.html', link['href'])[0]))
    
    #print(player_a_options)
    #Pick a random choice from that list of options. We now have the link to the chosen player's page
    player_a = random.choice(player_a_options)
    player_b = random.choice(player_b_options)
    #print(player_a)
    #print(player_b)
    return(getCareerStat("pts_per_g", player_a), getCareerStat("pts_per_g", player_b))
    