from Game import *


def init_bases(game_state):
    Base(game_state, 550, 0, 0, "Down")

    for i in range(6):
        Base(game_state, 505 - 37 * i, 510, i + 1, "Up")
    for i in range(6):
        Base(game_state, 247 - 37 * i, 510, 7 + i, "Up")
    for i in range(6):
        Base(game_state, 60 + 37 * i, 60, 13 + i, "Down")
    for i in range(6):
        Base(game_state, 320 + 37 * i, 60, 19 + i, "Down")
    Base(game_state, 0, 50, 25, "Down")