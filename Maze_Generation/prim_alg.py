from os import stat_result
from sys import path
from Game_State import Color, Constants
from utils import CellCoord, Instruction
import random


class PrimAlgorithm:
    def __init__(self, maze, instructions) -> None:
        self.lst = []
        self.instructions = instructions
        self.maze = maze
        self.running = False

    def start(self):
        self.running = True
        start_node = self.maze[Constants.START_CORD.row][Constants.START_CORD.col]
        start_node.state = "path"
        start_node.status = "visited"
        self.instructions.append(
            Instruction(start_node, Color.PATH, state="path", status="visited")
        )
        self.lst.append(Constants.START_CORD)

    def finish(self):
        self.running = False
        start_node = self.maze[Constants.START_CORD.row][Constants.START_CORD.col]
        self.instructions.append(Instruction(start_node, Color.START))

    def run(self):
        self.start()
        # while there are still cells in the list
        while len(self.lst) != 0:
            # pick a random cell from the list.
            random_idx = random.randrange(0, len(self.lst))
            curr_coord = self.lst[random_idx]
            curr_node = self.maze[curr_coord.row][curr_coord.col]

            random_neighbour_coord = self.random_neighbour(curr_node)

            # print("Neighbour Cell Coords: ", random_neighbour_coord)
            # print("Current Cell Coords: ", curr_coord)

            # if there are unvisited neighbours
            # pick a random unvisited neighbour
            if random_neighbour_coord is not None:
                # Make the wall a passage and mark the unvisited cell as visited
                wall_coord = self.find_wall(curr_node, random_neighbour_coord)
                wall_node = self.maze[wall_coord.row][wall_coord.col]
                wall_node.state = "path"
                wall_node.status = "visited"
                self.instructions.append(
                    Instruction(wall_node, Color.PATH, state="path", status="visited")
                )

                # add the unvisited neighbnoring cells of the cell to the cell list
                neighbour_node = self.maze[random_neighbour_coord.row][
                    random_neighbour_coord.col
                ]
                neighbour_node.state = "path"
                neighbour_node.status = "visited"
                self.instructions.append(
                    Instruction(
                        neighbour_node, Color.PATH, state="path", status="visited"
                    )
                )
                self.lst.append(random_neighbour_coord)
                
            else:
                # else, remove the cell from the list
                self.lst[random_idx], self.lst[len(self.lst) - 1] = (
                    self.lst[len(self.lst) - 1],
                    self.lst[random_idx],
                )
                self.lst.pop()
        self.finish()

    def find_wall(self, curr_node, neighbour_coord):
        curr_coord = curr_node.coord
        if curr_node.top is not None and neighbour_coord == curr_node.top:
            return CellCoord(curr_coord.col, curr_coord.row - 1)
        elif curr_node.right is not None and neighbour_coord == curr_node.right:
            return CellCoord(curr_coord.col + 1, curr_coord.row)
        elif curr_node.left is not None and neighbour_coord == curr_node.left:
            return CellCoord(curr_coord.col - 1, curr_coord.row)
        elif curr_node.bottom is not None and neighbour_coord == curr_node.bottom:
            return CellCoord(curr_coord.col, curr_coord.row + 1)

    def unvisited_neighbours(self, curr_node):
        neighbours_coords = curr_node.neighbour_list()

        unvisited_neighbours_coords = []
        for neighbour_coord in neighbours_coords:
            neighbour_node = self.maze[neighbour_coord.row][neighbour_coord.col]
            if neighbour_node.status != "visited":
                unvisited_neighbours_coords.append(neighbour_coord)
        # print("Unvisited Neighbours Coord", unvisited_neighbours_coords)
        return unvisited_neighbours_coords

    def random_neighbour(self, curr_node):
        unvisited_neighbours_coords = self.unvisited_neighbours(curr_node)
        result = []
        for neighbour_coord in unvisited_neighbours_coords:
            neighbour_node = self.maze[neighbour_coord.row][neighbour_coord.col]
            test = self.unvisited_neighbours(neighbour_node)
            # print("Unvisited neighbour's unvisited neighbours: ", test)
            if len(neighbour_node.neighbour_list()) - len(test) >= 1:
                result.append(neighbour_coord)
        # print("result: {}".format(result))
        return random.choice(result) if len(result) > 0 else None
