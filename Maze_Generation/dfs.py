from Game_State import color
from Game_State.node import Node
from Game_State.color import Color
from utils import CellCoord, Instruction
from Game_State import Constants
import random
import time


class DepthFirstAlgorithm:
    def __init__(self, maze, instructions):
        self.stack = []
        self.maze = maze
        self.instructions = instructions

    def start(self):
        print("Stack length",len(self.stack))
        start_node = self.maze[Constants.START_CORD.row][Constants.START_CORD.col]
        start_node.status = "visited"
        self.instructions.append(
            Instruction(start_node, Color.VISITED, status="visited")
        )
        self.stack.append(Constants.START_CORD)

    def finish(self):
        print("Stack length",len(self.stack))
        start_node = self.maze[Constants.START_CORD.row][Constants.START_CORD.col]
        self.instructions.append(Instruction(start_node, Color.START))

    def run(self):
        # Add starting cell to stack first
        self.start()
        # Check if stack is empty
        while len(self.stack) != 0:
            # Pop a cell from stack and make it current cell
            curr_coord = self.stack.pop()
            curr_node = self.maze[curr_coord.row][curr_coord.col]
            # if current cell is wall ignore it
            if curr_node.state == "wall":
                curr_node.state = "path"
                self.instructions.append(
                    Instruction(curr_node, Color.PATH, state="path")
                )
                continue
            # if the current cell has unvisited neighbours
            # randomly choose one of the unvisited neighbours
            neighbour_coord = self.random_neighbour(curr_node)

            # print("Neighbour Cell Coords: ", neighbour_coord)
            # print("Current Cell Coords: ", curr_coord)

            if neighbour_coord is not None:
                # push the current cell back to the stack
                self.stack.append(curr_coord)

                # remove the wall between the current cell and the chosen cell
                wall_coord = self.find_wall(curr_node, neighbour_coord)
                wall_node = self.maze[wall_coord.row][wall_coord.col]
                # add instruction
                wall_node.status = "visited"
                self.instructions.append(
                    Instruction(wall_node, Color.LAVENDER, status="visited")
                )
                self.stack.append(wall_coord)

                # mark the chosen cell as visited and push it to the stack
                neighbour_node = self.maze[neighbour_coord.row][neighbour_coord.col]
                neighbour_node.status = "visited"
                self.instructions.append(
                    Instruction(neighbour_node, color=Color.VISITED, status="visited")
                )
                self.stack.append(neighbour_coord)

            else:
                curr_node.state = "path"
                self.instructions.append(
                    Instruction(curr_node, Color.PATH, state="path")
                )
        self.finish()

    def random_neighbour(self, curr_node):
        neighbours_coords = curr_node.neighbour_list()
        unvisited_neighbour_coords = []
        for neighbour_coord in neighbours_coords:
            neighbour_node = self.maze[neighbour_coord.row][neighbour_coord.col]
            if neighbour_node.status != "visited":
                unvisited_neighbour_coords.append(neighbour_coord)
        return (
            random.choice(unvisited_neighbour_coords)
            if len(unvisited_neighbour_coords) > 0
            else None
        )

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
