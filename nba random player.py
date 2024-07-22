from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import string
import random
import re

player_a_options = []
player_b_options = []
#Pick a random letter to look up players with
player_a_letter = random.choice(string.ascii_letters).lower()
player_b_letter= random.choice(string.ascii_letters).lower()

#Open the player list for that letter
player_a_url = f'https://www.basketball-reference.com/players/{player_a_letter}/'
player_b_url = f'https://www.basketball-reference.com/players/{player_b_letter}/'
player_a_page = urlopen(player_a_url)
player_b_page = urlopen(player_b_url)
player_a_html = player_a_page.read().decode("utf-8")
player_b_html = player_b_page.read().decode("utf-8")
player_a_soup = BeautifulSoup(player_a_html, "html.parser")
player_b_soup = BeautifulSoup(player_b_html, "html.parser")

#Find all of the href links to the player pages in the resulting player list page
player_a_link = player_a_soup.find_all("a")
for link in player_a_link:
    if link.has_attr('href'):
        if re.findall(f'players.{player_a_letter}.+.html', link['href']) != []:
            #If the link found matches the regex for a player and having the letter we chose earlier, add it to the list of options
            player_a_options.append((re.findall(f'players.{player_a_letter}.+.html', link['href'])[0]))

print(player_a_options)
#Pick a random choice from that list of options. We now have the link to the chosen player's page
player_a = random.choice(player_a_options)
print(player_a)

