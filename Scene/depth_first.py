from .maze_scene import MazeScene
from Maze_Generation import DepthFirstAlgorithm

class DepthFirstScene(MazeScene):
    def __init__(self, game_state):
        super().__init__(game_state)
        # Initialize DFS data structure
        self.alg = DepthFirstAlgorithm(self.game_state.maze)


