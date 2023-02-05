# Installed libraries
import curses

class Setting:

    def __init__(self):
        self.player_avatar = "X"
        self.start_position_avatar = "O"
        self.finish_line_avatar = "W"
        self.wall_avatar = "#"
        self.player_color = None
        self.wall_color = None

    def update_setting(self, stdscr):
        # Setting up the player color
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

        # Setting up the wall color
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        self.player_color = curses.color_pair(1)
        self.wall_color = curses.color_pair(2)
