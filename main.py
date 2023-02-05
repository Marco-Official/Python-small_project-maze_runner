# Installed libraries
from curses import wrapper
import curses

# Built-in libraries
import queue
import time

# Local libraries
from maze import MAZE_MAP, generate_map, winner_banner
from setting import Setting


class Runner:
    def __init__(self, stdscr, player_setting: Setting):
        self.stdscr = stdscr
        self.player_setting = player_setting
        self.player_setting.update_setting(stdscr=stdscr)

    def get_to_starting_position(self):
        for row_number, row_elements in enumerate(MAZE_MAP):
            for column_number, element in enumerate(row_elements):
                if element == self.player_setting.start_position_avatar:
                    return row_number, column_number

    def _update_position(self, path):
        self.stdscr.clear()
        generate_map(stdscr=self.stdscr, player_setting=self.player_setting, path=path)
        time.sleep(0.4)
        self.stdscr.refresh()

    def _find_way_out(self, current_row, current_column):
        path_directions = []

        if current_row > 0:  # Not dead-end
            path_directions.append((current_row - 1, current_column))

        if current_row + 1 < len(MAZE_MAP):  # Go Down
            path_directions.append((current_row + 1, current_column))

        if current_column > 0:  # Go Left
            path_directions.append((current_row, current_column - 1))

        if current_column + 1 < len(MAZE_MAP[0]):  # Go Right
            path_directions.append((current_row, current_column + 1))

        return path_directions

    def _move(self, current_row, current_column, path, visited, run_queue: queue.Queue):
        if MAZE_MAP[current_row][current_column] == self.player_setting.finish_line_avatar:
            return path

        directions_to_move = self._find_way_out(
            current_row=current_row, current_column=current_column
        )

        for direction in directions_to_move:
            if direction in visited:
                continue

            direction_row, direction_column = direction
            if MAZE_MAP[direction_row][direction_column] == self.player_setting.wall_avatar:
                continue

            next_move = path + [direction]
            run_queue.put((direction, next_move))
            visited.add(direction)

    def run(self, start_position):
        run_queue = queue.Queue()
        run_queue.put((start_position, [start_position]))

        visited = set()

        while not run_queue.empty():
            current_position, path = run_queue.get()
            current_row, current_column = current_position

            self._update_position(path=path)
            self._move(
                current_row=current_row,
                current_column=current_column,
                path=path,
                visited=visited,
                run_queue=run_queue,
            )

        winner_banner(stdscr=self.stdscr, player_setting=self.player_setting)
        self.stdscr.getch()

def main(stdscr):
    # Initialize player.....
    player_setting = Setting()
    player = Runner(stdscr=stdscr, player_setting=player_setting)

    # Player getting ready....
    start_position = player.get_to_starting_position()

    # Ready 3!....2!.....1!..... GO!
    player.run(start_position=start_position)


if __name__ == '__main__':
    wrapper(main)
