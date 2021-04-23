from pygame.constants import SCRAP_SELECTION
from .constants import Constants
from utils import CellCoord

class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.font: dict = None
        self.checkbox: dict = None
        self.button = None
        self.maze: list = [
            [None] * Constants.NODE_WIDTH_COUNT
            for _ in range(Constants.NODE_LENGTH_COUNT)
        ]
        self.next_scene: int = None

    def reset(self):
        self.font = None
        self.checkbox = None
        self.button = None
        self.maze = [
            [None] * Constants.NODE_WIDTH_COUNT
            for _ in range(Constants.NODE_LENGTH_COUNT)
        ]
        self.next_scene = None

    def wall_list(self):
        lst = []
        for row in range(Constants.NODE_LENGTH_COUNT):
            if row != 0 and row != Constants.NODE_LENGTH_COUNT - 1:
                for col in range(Constants.NODE_WIDTH_COUNT):
                    if col != 0 and col != Constants.NODE_WIDTH_COUNT - 1:
                        if col % 2 == 0 and row % 2 == 1 or col % 2 == 1 and row % 2 == 0:
                            lst.append(CellCoord(col, row))
        return lst

    def render(self):
        if self.font != None:
            for word in self.font.values():
                word.render(self.screen)
        if self.button != None:
            self.button.render(self.screen)
        if self.checkbox != None:
            for checkbox in self.checkbox.values():
                checkbox.render(self.screen)
        for row in range(Constants.NODE_LENGTH_COUNT):
            for col in range(Constants.NODE_WIDTH_COUNT):
                self.maze[row][col].draw(self.screen)

