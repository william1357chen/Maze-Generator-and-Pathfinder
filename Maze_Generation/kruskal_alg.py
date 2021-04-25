from Game_State import Color, Constants
from utils import Cell, DisjointSet, CellCoord, Instruction

import random


class KruskalAlgorithm:
    def __init__(self, maze, instructions):
        self.sets = None
        self.instructions = instructions
        self.walls = None
        self.maze = maze

    def make_disjoint_set(self):
        count = 0
        for row in range(Constants.NODE_LENGTH_COUNT):
            for col in range(Constants.NODE_WIDTH_COUNT):
                curr_node = self.maze[row][col]
                if curr_node.state == "path":
                    self.sets.parent.append(Cell(count, count, CellCoord(col, row)))
                    count += 1

    def start(self):
        # create a set for each cell
        self.sets = DisjointSet()
        self.make_disjoint_set()
        self.walls = self.wall_list()

    def finish(self):
        start_node = self.maze[Constants.START_CORD.row][Constants.START_CORD.col]
        self.instructions.append(Instruction(start_node, Color.START))

    def run(self):

        self.start()

        while len(self.walls) != 0:
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
                wall_node = self.maze[row][col]
                wall_node.state = "path"

                col = self.sets.parent[idx1].coord.col
                row = self.sets.parent[idx1].coord.row
                idx1_node = self.maze[row][col]
                idx1_node.state = "path"

                col = self.sets.parent[idx2].coord.col
                row = self.sets.parent[idx2].coord.row
                idx2_node = self.maze[row][col]
                idx2_node.state = "path"

                self.instructions.append(
                    Instruction(idx1_node, Color.PATH, state="path")
                )
                self.instructions.append(
                    Instruction(wall_node, Color.PATH, state="path")
                )
                self.instructions.append(
                    Instruction(idx2_node, Color.PATH, state="path")
                )

            # swap and pop wall
            self.walls[wall_idx], self.walls[len(self.walls) - 1] = (
                self.walls[len(self.walls) - 1],
                self.walls[wall_idx],
            )
            self.walls.pop()

        self.finish()


    def wall_list(self):
        lst = []
        for row in range(Constants.NODE_LENGTH_COUNT):
            if row != 0 and row != Constants.NODE_LENGTH_COUNT - 1:
                for col in range(Constants.NODE_WIDTH_COUNT):
                    if col != 0 and col != Constants.NODE_WIDTH_COUNT - 1:
                        if col % 2 == 0 and row % 2 == 1 or col % 2 == 1 and row % 2 == 0:
                            lst.append(CellCoord(col, row))
        return lst