from .maze_scene import MazeScene
from Maze_Generation import PrimAlgorithm

class PrimScene(MazeScene):
    def __init__(self, game_state):
        super().__init__(game_state)
        # Initialize Prim Algorithm data structure
        self.alg = PrimAlgorithm(self.game_state.maze)
