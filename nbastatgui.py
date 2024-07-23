from nicegui import ui
import nbascrape
player_a_name = ""
player_b_name = ""
global player_information
player_information = []

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

def assessChoice(choice):
    player_a_stat = player_information[0][0]
    player_a_name = player_information[0][1]
    player_b_stat = player_information[1][0]
    player_b_name = player_information[1][1]
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
    player_a_stat_label.text = player_a_stat
    player_b_stat_label.text = player_b_stat
    


ui.label('NBA STAT HIGHER OR LOWER')
with ui.row():
    ui.button('Play The Game!', on_click=lambda: getPlayerInformation()
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