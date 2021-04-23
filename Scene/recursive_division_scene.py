from .maze_scene import MazeScene
from Maze_Generation import RecursiveDivisionAlgorithm
class RecursiveDivisionScene(MazeScene):
    def __init__(self, game_state):
        super().__init__(game_state)
        # Initialize Prim Algorithm data structure
        self.alg = RecursiveDivisionAlgorithm(self.game_state.maze)


    def update(self):
        pass