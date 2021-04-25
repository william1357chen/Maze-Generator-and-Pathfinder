import pygame
from .color import Color
from utils import Cell, CellCoord
from .constants import Constants


class Node:
    WIDTH = 20
    HEIGHT = 20

    def __init__(self, wall, x, y, color, coord):
        # Whether it is a wall or not (True means Wall and False means not Wall)
        self.wall = wall
        self.rect = pygame.Rect(x, y, Node.WIDTH, Node.HEIGHT)
        self.color = color
        self.coord = coord
        self.visited = False

        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    @property
    def state(self):
        return "wall" if self.wall else "path"

    @state.setter
    def state(self, value):
        self.wall = True if value == "wall" else False

    @property
    def status(self):
        return "visited" if self.visited else "unvisited"

    @status.setter
    def status(self, value):
        self.visited = True if value == "visited" else False

    def setup_neighbours(self):
        # set top
        if self.coord.row - 2 >= 1:
            self.top = CellCoord(self.coord.col, self.coord.row - 2)
        # set bottom
        if self.coord.row + 2 <= Constants.NODE_LENGTH_COUNT - 1:
            self.bottom = CellCoord(self.coord.col, self.coord.row + 2)
        # set left
        if self.coord.col - 2 >= 1:
            self.left = CellCoord(self.coord.col - 2, self.coord.row)
        # set right
        if self.coord.col + 2 <= Constants.NODE_WIDTH_COUNT - 1:
            self.right = CellCoord(self.coord.col + 2, self.coord.row)

    def neighbour_list(self):
        lst = []
        if self.top:
            lst.append(self.top)
        if self.bottom:
            lst.append(self.bottom)
        if self.left:
            lst.append(self.left)
        if self.right:
            lst.append(self.right)
        return lst

    def reset_neighbours(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        # black border
        pygame.draw.rect(screen, Color.BORDER, self.rect, width=1)

    def __repr__(self):
        return "{} {} at position: {}".format(self.status, self.state, self.coord)

