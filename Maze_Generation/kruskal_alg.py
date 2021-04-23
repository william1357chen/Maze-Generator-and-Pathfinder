from Game_State import Color, Constants
from utils import Cell, DisjointSet, CellCoord

import random


class KruskalAlgorithm:
    def __init__(self, maze, walls):
        self.sets = DisjointSet()
        self.walls = walls
        self.maze = maze
        self.running = False

    def make_disjoint_set(self):
        count = 0
        for row in range(Constants.NODE_LENGTH_COUNT):
            for col in range(Constants.NODE_WIDTH_COUNT):
                curr_node = self.maze[row][col]
                if curr_node.state == "path":
                    self.sets.parent.append(Cell(count, count, CellCoord(col, row)))
                    count += 1

    def start(self):
        self.running = True
        # create a set for each cell
        self.make_disjoint_set()

    def finish(self):
        self.running = False
        self.maze[Constants.START_CORD.row][Constants.START_CORD.col].color = Color.RED

    def run(self):
        if len(self.walls) == 0:
            print("wall list empty")
            self.finish()
            return
        # for each wall, in some random order
        wall_idx = random.randrange(0, len(self.walls))
        curr_wall_coord = self.walls[wall_idx]
        col = curr_wall_coord.col
        row = curr_wall_coord.row
        # pretty ugly calculations
        if col % 2 == 0 and row % 2 == 1:
            # left cell index in disjoint set
            left_coord = CellCoord(col - 1, row)
            idx1 = (left_coord.row // 2) * Constants.NUM_CELL_PER_LINE + (
                left_coord.col // 2
            )
            # right cell index in disjoint set
            idx2 = idx1 + 1
        elif col % 2 == 1 and row % 2 == 0:
            # top cell index in disjoint set
            top_coord = CellCoord(col, row - 1)
            idx1 = (top_coord.row // 2) * Constants.NUM_CELL_PER_LINE + (
                top_coord.col // 2
            )
            # bottom cell index in disjoint set
            idx2 = idx1 + Constants.NUM_CELL_PER_LINE
        # print("Keeping for Accuracy:\nWall coord: {} with top cell: {} and bottom cell: {}".format(curr_wall_coord, self.sets.parent[idx1], self.sets.parent[idx2]))

        # if the cells divided by this wall belong to distinct sets
        if not self.sets.check_rep(idx1, idx2):

            # join the sets of the formerly divided cells
            self.sets.union(idx1, idx2)
            # remove the current wall
            self.maze[row][col].state = "path"
            col = self.sets.parent[idx1].coord.col
            row = self.sets.parent[idx1].coord.row
            self.maze[row][col].state = "path"
            col = self.sets.parent[idx2].coord.col
            row = self.sets.parent[idx2].coord.row
            self.maze[row][col].state = "path"

        # swap and pop wall
        self.walls[wall_idx], self.walls[len(self.walls) - 1] = (
            self.walls[len(self.walls) - 1],
            self.walls[wall_idx],
        )
        self.walls.pop()
