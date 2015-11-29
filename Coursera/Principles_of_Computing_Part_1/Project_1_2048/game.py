"""
Clone of 2048 game.
"""

import os
import sys

tmp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(tmp)
print(__file__)
sys.path.append(tmp)

#import poc_2048_gui
import random
from Project_1_merge_2048.merge import merge


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


'''
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    tight_line = tight(line[:])

    iter_i = 0
    while iter_i <= len(tight_line) - 2:
      if tight_line[iter_i] != 0 and tight_line[iter_i] == tight_line[iter_i + 1]:
        tight_line[iter_i] *= 2
        tight_line[iter_i + 1] = 0
        iter_i += 2
      else:
        iter_i += 1

    return tight(tight_line)

def tight(line):
  """
  Function that move all zeroes to the end of the list.
  """
  for iter_j in xrange(len(line)):
    iter_i = iter_j - 1
    while iter_i >= 0:
      if line[iter_i] == 0:
        line[iter_i] = line[iter_i + 1]
        line[iter_i + 1] = 0
      iter_i -= 1
  return line
'''


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        self.reset()

        self._tiles_indices_up = []
        self._tiles_indices_down = []
        self._tiles_indices_left = []
        self._tiles_indices_right = []

        for width in xrange(self._width):
            self._tiles_indices_up.append((0, width))
            self._tiles_indices_down.append((self._height - 1, width))

        for height in xrange(self._height):
            self._tiles_indices_left.append((height, 0))
            self._tiles_indices_right.append((height, self._width - 1))


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [ [0] * self._width for _ in xrange(self._height)]
        for _ in xrange(2):
            self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = ''
        for line in xrange(self._height):
            for row in xrange(self._width):
                result += str(self._grid[line][row]) + ' '
            result += '\n'
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        movements = 0

        for row in xrange(self._width):
            if direction == UP:
                start_point = (0, row)
                steps = self._height
            elif direction == DOWN:
                start_point = (self._height - 1, row)
                steps = self._height
            else:
                break

            get_line = self.get_line_or_row(start_point, OFFSETS[direction], steps)
            set_line = merge(get_line)
            if get_line != set_line:
                self.set_line_or_row(start_point, OFFSETS[direction], steps, set_line)
                movements += 1

        for line in xrange(self._height):
            if direction == LEFT:
                start_point = (line, 0)
                steps = self._width
            elif direction == RIGHT:
                start_point = (line, self._width - 1)
                steps = self._width
            else:
                break

            get_line = self.get_line_or_row(start_point, OFFSETS[direction], steps)
            set_line = merge(get_line)
            if get_line != set_line:
                self.set_line_or_row(start_point, OFFSETS[direction], steps, set_line)
                movements += 1

        if movements != 0:
            self.new_tile()
        else:
            print "the game is over"


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        value = -1
        height = -1
        width = -1
        while value != 0:
            height = random.randint(0, self._height - 1)
            width = random.randint(0, self._width - 1)
            value = self._grid[height][width]

        probability = random.random()
        if probability < 0.9:
            self._grid[height][width] = 2
        else:
            self._grid[height][width] = 4

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    def get_line_or_row(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction

        Both start_cell is a tuple(row, col) denoting the
        starting cell

        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        line = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            line.append(self._grid[row][col])
        return line

    def set_line_or_row(self, start_cell, direction, num_steps, new_line):
        """
        Function that iterates through the cells in a grid
        in a linear direction and change that line to new_line.
        """
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self._grid[row][col] = new_line[step]



#board = TwentyFortyEight(4, 4)
#board.set_tile(0, 0, 2)
#board.set_tile(0, 1, 0)
#board.set_tile(0, 2, 0)
#board.set_tile(0, 3, 0)
#board.set_tile(1, 0, 0)
#board.set_tile(1, 1, 2)
#board.set_tile(1, 2, 0)
#board.set_tile(1, 3, 0)
#board.set_tile(2, 0, 0)
#board.set_tile(2, 1, 0)
#board.set_tile(2, 2, 2)
#board.set_tile(2, 3, 0)
#board.set_tile(3, 0, 0)
#board.set_tile(3, 1, 0)
#board.set_tile(3, 2, 0)
#board.set_tile(3, 3, 2)
#board.move(UP)
#print(board)

# 2 0 0 0
# 0 2 0 0
# 0 0 2 0
# 0 0 0 2
#
# =>
#
# 2 2 2 2
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
