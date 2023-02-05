from setting import Setting

MAZE_MAP = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"],
]

def generate_map(stdscr, player_setting: Setting, path=[]):
    """Generate the map elements that will be display in the terminal.

    Args:
        map (list): Maze map defined.
        stdscr (Any): stands for (Standard Output Screen)
        path (list, optional): List of path that player can run. Defaults to [].
    """
    for row_number, row_elements in enumerate(MAZE_MAP):
        for column_number, element in enumerate(row_elements):
            if (row_number, column_number) in path:
                # print(row_number, column_number*2, "X")
                stdscr.addstr(row_number, column_number*2, player_setting.player_avatar, player_setting.player_color)
            else:
                # print(row_number, column_number*2, element)
                stdscr.addstr(row_number, column_number*2, element, player_setting.wall_color)

def winner_banner(stdscr,  player_setting: Setting):
    stdscr.addstr(12, 0, "CONGRATULATION RUNNER!", player_setting.player_color)