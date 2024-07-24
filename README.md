As my first foray into web scraping, I decided to make a little game where the player can click a button to start playing, the script goes to basketball-reference.com and grabs two random players from the all time points per game leaderboard, and presents them to the player. You then choose which of the two players has the higher career points per game. The game informs the player if they were correct or not, and then gives them the option to play again.

This actual data gathering is done with the [urllib](https://github.com/python/cpython/tree/3.12/Lib/urllib/) python package for scraping the page and then uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to parse the data. This allowed me to search through page elements to programmatically find exactly the information I need. I used a combination of tags and regex to get player stats, names, and links to their page in order to get their image.

The web app itself is frontended with the [NiceGUI](https://nicegui.io/) framework. I like to work in Python as much as possible and this framework makes it really simple. It's nothing too spectacular, but that's not what I'm learning here :)

Hope some people get a little bit of enjoyment from my learning.
