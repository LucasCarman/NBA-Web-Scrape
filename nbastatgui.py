from nicegui import ui
import nbascrape
player_a_name = ""
player_b_name = ""
global player_information
player_information = []
player_stat_list = []

def getTwoPlayersDict():
    global player_stat_list
    player_stat_list = nbascrape.pickTwoPlayers(nbascrape.getPpgLeadersDict())
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