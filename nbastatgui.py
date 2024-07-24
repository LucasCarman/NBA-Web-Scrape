from nicegui import ui
import nbascrape
player_a_name = ""
player_b_name = ""
global player_information
player_information = []
player_stat_list = []
all_player_dict = {'Michael Jordan': ['30.12', 'players/j/jordami01.html'], 'Wilt Chamberlain': ['30.07', 'players/c/chambwi01.html'], 'Luka Dončić': ['28.68', 'players/d/doncilu01.html'], 'Joel Embiid': ['27.88', 'players/e/embiijo01.html'], 'Elgin Baylor': ['27.36', 'players/b/bayloel01.html'], 'Kevin Durant': ['27.26', 'players/d/duranke01.html'], 'LeBron James': ['27.13', 'players/j/jamesle01.html'], 'Jerry West': ['27.03', 'players/w/westje01.html'], 'Allen Iverson': ['26.66', 'players/i/iversal01.html'], 'Bob Pettit': ['26.36', 'players/p/pettibo01.html'], 'Oscar Robertson': ['25.68', 'players/r/roberos01.html'], 'Trae Young': ['25.50', 'players/y/youngtr01.html'], 'Damian Lillard': ['25.12', 'players/l/lillada01.html'], 'George Gervin': ['25.09', 'players/g/gervige01.html'], 'Karl Malone': ['25.02', 'players/m/malonka01.html'], 'Kobe Bryant': ['24.99', 'players/b/bryanko01.html'], 'Dominique Wilkins': ['24.83', 'players/w/wilkido01.html'], 'Donovan Mitchell': ['24.83', 'players/m/mitchdo01.html'], 'Rick Barry': ['24.78', 'players/b/barryri01.html'], 'Stephen Curry': ['24.76', 'players/c/curryst01.html'], 'Kareem Abdul-Jabbar': ['24.61', 'players/a/abdulka01.html'], 'Devin Booker': ['24.30', 'players/b/bookede01.html'], 'Larry Bird': ['24.29', 'players/b/birdla01.html'], 'Adrian Dantley': ['24.27', 'players/d/dantlad01.html'], 'Pete Maravich': ['24.24', 'players/m/maravpe01.html'], 'Julius Erving': ['24.16', 'players/e/ervinju01.html'], 'James Harden': ['24.15', 'players/h/hardeja01.html'], 'Anthony Davis': ['24.07', 'players/d/davisan02.html'], "Shaquille O'Neal": ['23.69', 'players/o/onealsh01.html'], 'Kyrie Irving': ['23.59', 'players/i/irvinky01.html'], 'Giannis Antetokounmpo': ['23.36', 'players/a/antetgi01.html'], 'George Mikan': ['23.13', 'players/m/mikange01.html'], 'Jayson Tatum': ['23.10', 'players/t/tatumja01.html'], 'Karl-Anthony Towns': ['22.90', 'players/t/townska01.html'], 'Paul Arizin': ['22.81', 'players/a/arizipa01.html'], 'David Thompson': ['22.67', 'players/t/thompda01.html'], 'Dan Issel': ['22.56', 'players/i/isselda01.html'], 'Bernard King': ['22.49', 'players/k/kingbe01.html'], 'Carmelo Anthony': ['22.45', 'players/a/anthoca01.html'], 'Charles Barkley': ['22.14', 'players/b/barklch01.html'], 'Bob McAdoo': ['22.05', 'players/m/mcadobo01.html'], 'Dwyane Wade': ['21.98', 'players/w/wadedw01.html'], 'Bradley Beal': ['21.86', 'players/b/bealbr01.html'], 'Geoff Petrie': ['21.82', 'players/p/petrige01.html'], 'Hakeem Olajuwon': ['21.77', 'players/o/olajuha01.html'], 'Russell Westbrook': ['21.70', 'players/w/westbru01.html'], 'Alex English': ['21.47', 'players/e/englial01.html'], 'DeMar DeRozan': ['21.25', 'players/d/derozde01.html'], "De'Aaron Fox": ['21.19', 'players/f/foxde01.html'], 'Billy Cunningham': ['21.18', 'players/c/cunnibi01.html'], 'David Robinson': ['21.06', 'players/r/robinda01.html'], 'Mitch Richmond': ['21.00', 'players/r/richmmi01.html'], 'Patrick Ewing': ['20.98', 'players/e/ewingpa01.html'], 'Elvin Hayes': ['20.96', 'players/h/hayesel01.html'], 'Nikola Jokić': ['20.95', 'players/j/jokicni01.html'], 'Paul George': ['20.80', 'players/g/georgpa01.html'], 'John Havlicek': ['20.78', 'players/h/havlijo01.html'], 'Dirk Nowitzki': ['20.74', 'players/n/nowitdi01.html'], 'Charlie Scott': ['20.69', 'players/s/scottch01.html'], 'John Drew': ['20.69', 'players/d/drewjo01.html'], 'Glenn Robinson': ['20.69', 'players/r/robingl01.html'], 'John Brisker': ['20.69', 'players/b/briskjo01.html'], 'Chris Webber': ['20.68', 'players/w/webbech01.html'], 'Gilbert Arenas': ['20.66', 'players/a/arenagi01.html'], 'Zach LaVine': ['20.46', 'players/l/lavinza01.html'], 'Clyde Drexler': ['20.44', 'players/d/drexlcl01.html'], 'Dave Bing': ['20.34', 'players/b/bingda01.html'], 'Moses Malone': ['20.33', 'players/m/malonmo01.html'], 'Spencer Haywood': ['20.27', 'players/h/haywosp01.html'], 'World B. Free': ['20.27', 'players/f/freewo01.html'], 'Bob Verga': ['20.23', 'players/v/vergabo01.html'], 'George McGinnis': ['20.20', 'players/m/mcginge01.html'], 'Lou Hudson': ['20.16', 'players/h/hudsolo01.html'], 'Marques Johnson': ['20.10', 'players/j/johnsma01.html'], 'Walt Bellamy': ['20.08', 'players/b/bellawa01.html'], 'Bob Lanier': ['20.07', 'players/l/laniebo01.html'], 'Darel Carrier': ['20.03', 'players/c/carrida01.html'], 'Kawhi Leonard': ['20.02', 'players/l/leonaka01.html'], 'Mark Aguirre': ['20.00', 'players/a/aguirma01.html'], 'Mike Mitchell': ['19.78', 'players/m/mitchmi01.html'], 'Kiki Vandeweghe': ['19.73', 'players/v/vandeki01.html'], 'Paul Pierce': ['19.66', 'players/p/piercpa01.html'], 'Kristaps Porziņģis': ['19.65', 'players/p/porzikr01.html'], 'Tracy McGrady': ['19.60', 'players/m/mcgratr01.html'], 'Klay Thompson': ['19.59', 'players/t/thompkl01.html'], 'DeMarcus Cousins': ['19.57', 'players/c/couside01.html'], 'Magic Johnson': ['19.54', 'players/j/johnsma02.html'], 'CJ McCollum': ['19.47', 'players/m/mccolcj01.html'], 'Neil Johnston': ['19.42', 'players/j/johnsne01.html'], 'Brandon Ingram': ['19.40', 'players/i/ingrabr01.html'], 'Levern Tart': ['19.40', 'players/t/tartle01.html'], 'Kemba Walker': ['19.31', 'players/w/walkeke02.html'], 'Stephon Marbury': ['19.26', 'players/m/marbust01.html'], 'Chris Bosh': ['19.25', 'players/b/boshch01.html'], 'Jack Twyman': ['19.25', 'players/t/twymaja01.html'], 'Hal Greer': ['19.24', 'players/g/greerha01.html'], 'Isiah Thomas': ['19.23', 'players/t/thomais01.html'], 'George Yardley': ['19.20', 'players/y/yardlge01.html'], 'LaMarcus Aldridge': ['19.11', 'players/a/aldrila01.html'], 'Julius Randle': ['19.08', 'players/r/randlju01.html'], 'Larry Jones': ['19.07', 'players/j/jonesla01.html'], 'Jamal Mashburn': ['19.06', 'players/m/mashbja01.html'], 'Jeff Malone': ['19.04', 'players/m/malonje01.html'], 'Tim Duncan': ['19.03', 'players/d/duncati01.html'], 'Michael Redd': ['19.03', 'players/r/reddmi01.html'], 'Yao Ming': ['19.03', 'players/m/mingya01.html'], 'Blake Griffin': ['18.97', 'players/g/griffbl01.html'], 'Brad Daugherty': ['18.96', 'players/d/daughbr01.html'], "Amar'e Stoudemire": ['18.91', 'players/s/stoudam01.html'], 'Walter Davis': ['18.90', 'players/d/daviswa03.html'], 'Walt Frazier': ['18.89', 'players/f/fraziwa01.html'], 'Donnie Freeman': ['18.88', 'players/f/freemdo01.html'], 'Ray Allen': ['18.85', 'players/a/allenra02.html'], 'Earl Monroe': ['18.85', 'players/m/monroea01.html'], 'Tiny Archibald': ['18.81', 'players/a/architi01.html'], 'Artis Gilmore': ['18.77', 'players/g/gilmoar01.html'], 'Willis Reed': ['18.74', 'players/r/reedwi01.html'], 'Connie Hawkins': ['18.71', 'players/h/hawkico01.html'], 'Bailey Howell': ['18.71', 'players/h/howelba01.html'], 'John Wall': ['18.68', 'players/w/walljo01.html'], 'Tom Heinsohn': ['18.65', 'players/h/heinsto01.html'], 'Gail Goodrich': ['18.60', 'players/g/goodrga01.html'], 'Jaylen Brown': ['18.59', 'players/b/brownja02.html'], 'George Thompson': ['18.57', 'players/t/thompge01.html'], 'Andrew Wiggins': ['18.54', 'players/w/wiggian01.html'], 'Reggie Theus': ['18.53', 'players/t/theusre01.html'], 'Dolph Schayes': ['18.51', 'players/s/schaydo01.html'], 'Bob Dandridge': ['18.51', 'players/d/dandrbo01.html'], 'Antawn Jamison': ['18.51', 'players/j/jamisan01.html'], 'Mel Daniels': ['18.43', 'players/d/danieme01.html'], 'Bob Cousy': ['18.35', 'players/c/cousybo01.html'], 'Jimmy Butler': ['18.35', 'players/b/butleji01.html'], 'Glen Rice': ['18.34', 'players/r/ricegl01.html'], 'Latrell Sprewell': ['18.30', 'players/s/sprewla01.html'], 'Chet Walker': ['18.25', 'players/w/walkech01.html'], 'Reggie Miller': ['18.20', 'players/m/millere01.html'], 'Chris Mullin': ['18.17', 'players/m/mullich01.html'], 'Steve Francis': ['18.14', 'players/f/francst01.html'], 'Lauri Markkanen': ['18.13', 'players/m/markkla01.html'], 'George Carter': ['18.13', 'players/c/cartege01.html'], 'Tom Chambers': ['18.11', 'players/c/chambto01.html'], 'Shareef Abdur-Rahim': ['18.11', 'players/a/abdursh01.html'], 'Otis Birdsong': ['18.02', 'players/b/birdsot01.html'], 'Rolando Blackman': ['17.98', 'players/b/blackro01.html'], 'Calvin Murphy': ['17.91', 'players/m/murphca01.html'], 'Doug Collins': ['17.90', 'players/c/collido01.html'], 'Kevin Johnson': ['17.86', 'players/j/johnske02.html'], 'Kevin McHale': ['17.85', 'players/m/mchalke01.html'], 'Monta Ellis': ['17.84', 'players/e/ellismo01.html'], 'Kevin Garnett': ['17.83', 'players/g/garneke01.html'], 'Bill Sharman': ['17.81', 'players/s/sharmbi01.html'], "D'Angelo Russell": ['17.75', 'players/r/russeda01.html'], 'Tim Hardaway': ['17.73', 'players/h/hardati01.html'], 'Cliff Hagan': ['17.72', 'players/h/hagancl01.html'], 'Sam Jones': ['17.69', 'players/j/jonessa01.html'], 'Pascal Siakam': ['17.69', 'players/s/siakapa01.html'], 'Jamaal Wilkes': ['17.69', 'players/w/wilkeja01.html'], 'Joe Barry Carroll': ['17.67', 'players/c/carrojo01.html'], 'Dave Cowens': ['17.64', 'players/c/cowenda01.html'], 'James Worthy': ['17.62', 'players/w/worthja01.html'], 'Willie Wise': ['17.62', 'players/w/wisewi01.html'], 'Bob Love': ['17.61', 'players/l/lovebo01.html'], 'Reggie Lewis': ['17.56', 'players/l/lewisre01.html'], 'Ed Macauley': ['17.53', 'players/m/macaued01.html'], 'Chris Paul': ['17.52', 'players/p/paulch01.html'], 'Antoine Walker': ['17.52', 'players/w/walkean02.html'], 'Isaiah Thomas': ['17.49', 'players/t/thomais02.html'], 'John Williamson': ['17.47', 'players/w/willijo01.html'], 'Jamal Murray': ['17.46', 'players/m/murraja01.html'], 'Rudy Tomjanovich': ['17.43', 'players/t/tomjaru01.html'], 'Derrick Rose': ['17.39', 'players/r/rosede01.html'], 'Bob Rule': ['17.39', 'players/r/rulebo01.html'], 'Kevin Martin': ['17.36', 'players/m/martike02.html'], 'Roger Brown': ['17.35', 'players/b/brownro01.html'], 'Purvis Short': ['17.35', 'players/s/shortpu01.html'], 'Allan Houston': ['17.34', 'players/h/houstal01.html'], 'Kyle Kuzma': ['17.32', 'players/k/kuzmaky01.html'], 'Richie Guerin': ['17.31', 'players/g/gueriri01.html'], 'Larry Kenon': ['17.23', 'players/k/kenonla01.html'], 'Cliff Robinson': ['17.21', 'players/r/robincl01.html'], 'Jo Jo White': ['17.20', 'players/w/whitejo01.html'], 'Phil Chenier': ['17.18', 'players/c/cheniph01.html'], 'Calvin Natt': ['17.18', 'players/n/nattca01.html'], 'Kelly Tripucka': ['17.17', 'players/t/tripuke01.html'], 'Warren Jabali': ['17.15', 'players/j/jabalwa01.html'], 'Zelmo Beaty': ['17.11', 'players/b/beatyze01.html'], 'Nikola Vučević': ['17.10', 'players/v/vucevni01.html'], 'Jason Richardson': ['17.09', 'players/r/richaja01.html'], 'Gus Williams': ['17.08', 'players/w/willigu01.html'], 'Alonzo Mourning': ['17.08', 'players/m/mournal01.html'], 'Richard Hamilton': ['17.06', 'players/h/hamilri01.html'], 'Larry Nance': ['17.05', 'players/n/nancela01.html'], 'Pau Gasol': ['17.04', 'players/g/gasolpa01.html'], 'Peja Stojaković': ['16.97', 'players/s/stojape01.html'], 'Clyde Lovellette': ['16.97', 'players/l/lovelcl01.html'], 'Jerry Lucas': ['16.95', 'players/l/lucasje01.html'], 'Billy Knight': ['16.93', 'players/k/knighbi01.html'], 'Jerry Stackhouse': ['16.92', 'players/s/stackje01.html'], 'Jalen Brunson': ['16.90', 'players/b/brunsja01.html'], 'Victor Oladipo': ['16.87', 'players/o/oladivi01.html'], 'Khris Middleton': ['16.86', 'players/m/middlkh01.html'], 'Sidney Wicks': ['16.85', 'players/w/wickssi01.html'], 'Danny Granger': ['16.82', 'players/g/grangda01.html'], 'Ron Boone': ['16.75', 'players/b/boonero01.html'], 'Ralph Simpson': ['16.72', 'players/s/simpsra01.html'], 'Isaiah Rider': ['16.71', 'players/r/rideris01.html'], 'Grant Hill': ['16.70', 'players/h/hillgr01.html'], 'Jimmy Walker': ['16.70', 'players/w/walkeji01.html'], 'Vince Carter': ['16.70', 'players/c/cartevi01.html'], 'Randy Smith': ['16.66', 'players/s/smithra01.html'], 'Zach Randolph': ['16.65', 'players/r/randoza01.html'], 'Jimmy Jones': ['16.57', 'players/j/jonesji01.html'], 'Lenny Wilkens': ['16.50', 'players/w/wilkele01.html'], 'Derrick Coleman': ['16.50', 'players/c/colemde01.html'], 'Glen Combs': ['16.49', 'players/c/combsgl01.html'], 'Kevin Love': ['16.47', 'players/l/loveke01.html'], 'Terry Cummings': ['16.45', 'players/c/cummite01.html'], 'Dick Van Arsdale': ['16.37', 'players/v/vanardi01.html'], 'Joe Fulks': ['16.37', 'players/f/fulksjo01.html'], 'Gary Payton': ['16.34', 'players/p/paytoga01.html'], 'Deron Williams': ['16.34', 'players/w/willide01.html'], 'Archie Clark': ['16.30', 'players/c/clarkar01.html'], 'Doug Moe': ['16.30', 'players/m/moedo01.html'], 'Stew Johnson': ['16.29', 'players/j/johnsst01.html'], 'Tobias Harris': ['16.28', 'players/h/harrito02.html'], 'Cincy Powell': ['16.27', 'players/p/powelci01.html'], 'Gus Johnson': ['16.23', 'players/j/johnsgu01.html'], 'Carlos Boozer': ['16.23', 'players/b/boozeca01.html'], 'Brian Winters': ['16.21', 'players/w/wintebr01.html'], 'Darrell Griffith': ['16.20', 'players/g/griffda01.html'], 'Larry Johnson': ['16.20', 'players/j/johnsla02.html'], 'Jeff Mullins': ['16.19', 'players/m/mullije01.html'], 'Charlie Williams': ['16.18', 'players/w/willich01.html'], 'Jrue Holiday': ['16.14', 'players/h/holidjr01.html'], 'Joe Caldwell': ['16.14', 'players/c/caldwjo01.html'], 'Mack Calvin': ['16.12', 'players/c/calvima01.html'], 'James Silas': ['16.11', 'players/s/silasja01.html'], 'Joe Dumars': ['16.11', 'players/d/dumarjo01.html'], 'Baron Davis': ['16.10', 'players/d/davisba01.html'], 'Scottie Pippen': ['16.08', 'players/p/pippesc01.html'], 'Brook Lopez': ['16.07', 'players/l/lopezbr01.html'], 'Dave DeBusschere': ['16.06', 'players/d/debusda01.html'], 'Freddie Lewis': ['16.04', 'players/l/lewisfr02.html'], 'Cuttino Mobley': ['16.02', 'players/m/moblecu01.html'], 'Eddie Johnson': ['16.02', 'players/j/johnsed03.html'], 'Keith Van Horn': ['16.01', 'players/v/vanhoke01.html'], 'Orlando Woolridge': ['16.01', 'players/w/woolror01.html'], 'Marvin Barnes': ['15.98', 'players/b/barnema01.html'], 'Bob Netolicky': ['15.98', 'players/n/netolbo01.html'], 'Joe Johnson': ['15.98', 'players/j/johnsjo02.html']}

def getTwoPlayersDict():
    global player_stat_list
    player_stat_list = nbascrape.pickTwoPlayers(all_player_dict)
    ui.notify(player_stat_list)
    splitter.clear()
    with splitter.before:
        ui.label("Player A")
        player_a_image = ui.image(player_stat_list[0][1][1])
        player_a_name_label = ui.label(player_stat_list[0][0])
        choose_a = ui.button('Higher', on_click=lambda: assessChoice("A"))

    with splitter.after:
        ui.label("Player B")
        player_b_image = ui.image(player_stat_list[1][1][1])
        player_b_name_label = ui.label(player_stat_list[1][0])
        choose_b = ui.button('Higher', on_click=lambda: assessChoice("B"))


def assessChoice(choice):
    player_a_stat = player_stat_list[0][1][0]
    player_a_name = player_stat_list[0][0]
    player_b_stat = player_stat_list[1][1][0]
    player_b_name = player_stat_list[1][0]
    if choice == "A":
        if player_a_stat > player_b_stat:
            ui.notify(f'Correct, {player_a_name} is higher with {player_a_stat}')
        else:
            ui.notify(f'Incorrect, {player_b_name} is higher with {player_b_stat}')
    if choice == "B":
        if player_b_stat > player_a_stat:
            ui.notify(f'Correct, {player_b_name} is higher with {player_b_stat}')
        else:
            ui.notify(f'Incorrect, {player_a_name} is higher with {player_a_stat}')
    with splitter.before:
        player_a_stat_label = ui.label(player_a_stat)
    with splitter.after:
        player_b_stat_label = ui.label(player_b_stat)
    start_button.text = "Play Again?"
    
def getPlayerInformation():
    global player_information
    player_information = nbascrape.getRandomPlayers()
    splitter.clear()
    with splitter.before:
        ui.label("Player A")
        player_a_name_label = ui.label(player_b_name)
        choose_a = ui.button('Higher', on_click=lambda: assessChoice("A"))
        player_a_stat_label = ui.label()
    with splitter.after:
        ui.label("Player B")
        player_b_name_label = ui.label(player_a_name)
        choose_b = ui.button('Higher', on_click=lambda: assessChoice("B"))
        player_b_stat_label = ui.label()
    player_a_name_label.text = player_information[0][1]
    player_b_name_label.text = player_information[1][1]
    ui.notify(player_information)




ui.label('NBA: Career PPG')
with ui.row():
    start_button = ui.button('Play The Game!', on_click=lambda: getTwoPlayersDict()
              )

with ui.row() as player_data:
    with ui.splitter() as splitter:
        with splitter.before:
            ui.label("Player A")
            player_b_name_label = ui.label(player_b_name)
            choose_a = ui.button('Higher', on_click=lambda: assessChoice("A")).set_visibility(False)
            player_a_stat_label = ui.label()
        with splitter.after:
            ui.label("Player B")
            player_a_name_label = ui.label(player_a_name)
            choose_b = ui.button('Higher', on_click=lambda: assessChoice("B")).set_visibility(False)
            player_b_stat_label = ui.label()
ui.run()