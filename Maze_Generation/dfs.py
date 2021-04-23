from Game_State.node import Node
from Game_State.color import Color
from utils import CellCoord
from Game_State import Constants
import random
import time


class DepthFirstAlgorithm:
    def __init__(self, maze):
        self.stack = []
        self.maze = maze
        self.running = False

    def start(self):
        self.running = True
        self.maze[Constants.START_CORD.row][Constants.START_CORD.col].status = "visited"
        self.stack.append(Constants.START_CORD)

    def finish(self):
        self.running = False
        self.maze[Constants.START_CORD.row][Constants.START_CORD.col].color = Color.RED

    def run(self):
        # Check if stack is empty
        if len(self.stack) == 0:
            print("stack empty")
            self.finish()
            return
        # Pop a cell from stack and make it current cell
        curr_coord = self.stack.pop()
        curr_node = self.maze[curr_coord.row][curr_coord.col]
        # if current cell is wall ignore it
        if curr_node.state == "wall":
            curr_node.state = "path"
            return
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
            wall = self.maze[wall_coord.row][wall_coord.col]
            wall.status = "visited"
            self.stack.append(wall_coord)
            # mark the chosen cell as visited and push it to the stack
            neighbour = self.maze[neighbour_coord.row][neighbour_coord.col]
            neighbour.status = "visited"
            self.stack.append(neighbour_coord)

        else:
            curr_node.state = "path"

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
