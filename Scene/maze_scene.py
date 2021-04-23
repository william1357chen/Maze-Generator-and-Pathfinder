from .scene import Scene
from Game_State import Constants, Color
from utils import CellCoord

import pygame
import time

class MazeScene(Scene):
    def __init__(self, game_state):
        self.game_state = game_state
        self.setup = False
        self.coord = CellCoord(0, 0)
        self.alg = None

    def initialize(self):
        self.setup = True
        self.game_state.next_scene = None

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        if self.setup:
            self.make_walls()
        else:
            if self.alg.running is True:
                self.alg.run()
                time.sleep(0.1)

    def render(self):
        self.game_state.render()

    def make_walls(self):
        curr_node = self.game_state.maze[self.coord.row][self.coord.col]
        state = ""
        # first row and last row
        if self.coord.row == 0 or self.coord.row == Constants.NODE_LENGTH_COUNT - 1:
            state = "wall"
        # if row is even
        elif self.coord.row % 2 == 0:
            state = "wall"
        # if row is odd and col is even
        elif self.coord.row % 2 == 1 and self.coord.col % 2 == 0:
            state = "wall"
        elif self.coord.row % 2 == 1 and self.coord.col % 2 == 1:
            state = "path"

        curr_node.state = state
        if state == "path":
            self.game_state.maze[self.coord.row][self.coord.col].color = Color.BLACK
            curr_node.setup_neighbours()
        if self.coord.col >= Constants.NODE_WIDTH_COUNT - 1:
            self.coord.row += 1
            self.coord.col = 0
        else:
            self.coord.col += 1

        if self.coord.row > Constants.NODE_LENGTH_COUNT - 1:
            self.setup = False
            self.alg.start()
