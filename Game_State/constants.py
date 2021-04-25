from pygame.math import Vector2
from utils import CellCoord
import os

base_path = os.path.dirname(__file__)


class Constants:
    NODE_LENGTH_COUNT = 25
    NODE_WIDTH_COUNT = 25
    MAZE_POSITION = Vector2(600, 100)
    START_CORD = CellCoord(1, NODE_LENGTH_COUNT - 2)

    NUM_CELL_PER_LINE = (NODE_WIDTH_COUNT - 1) // 2
    FONT = os.path.join(base_path, "..", "assets", "GemunuLibre.ttf")
