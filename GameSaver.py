from Game import *


def save(game_state):
    with open('gameDate', 'w', encoding='utf-8') as file:
        result = ""
        for base_index in range(len(game_state.baseList)):
            for washer in game_state.baseList[base_index].washers:
                color = washer.color
                washer_x = washer.x
                washer_y = washer.y
                result += color + " " + str(washer_x) + " " + str(washer_y) + " "\
                         + str(base_index) + " " + str(washer.index) + "\n"
        result += str(game_state.count_of_white) + '\n'
        result += str(game_state.count_of_black) + '\n'
        result += str(game_state.timer.get_time())

        file.writelines(result)


def restore_game(game_state):
    with open('gameDate', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines) - 3):
            lines[i] = lines[i][:len(lines[i]) - 1:]
            color, x, y, base_ind, wash_ind = lines[i].split()
            x, y, base_ind, wash_ind = int(x), int(y), int(base_ind), int(wash_ind)
            game_state.baseList[base_ind].add_washer(Washer(color, x, y, game_state.baseList[base_ind], wash_ind))
        game_state.count_of_white = int(lines[-3][:len(lines[-2]) - 1:])
        game_state.count_of_black = int(lines[-2][:len(lines[-2]) - 1:])
        game_state.timer.set_time(float(lines[-1]))


def over_write():
    with open('firstState', 'r', encoding='utf-8') as src:
        with open('gameDate', 'w', encoding='utf-8') as dst:
            dst.write(src.read())
