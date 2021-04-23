from .maze_scene import MazeScene
from Game_State import Constants, Color
from Maze_Generation import KruskalAlgorithm

import time
import pygame



class KruskalScene(MazeScene):
    def __init__(self, game_state):
        super().__init__(game_state)
        # Initialize Kruskal Algorithm data structure
        self.alg = KruskalAlgorithm(self.game_state.maze, self.game_state.wall_list())

