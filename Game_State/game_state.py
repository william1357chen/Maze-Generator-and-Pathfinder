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

    def click_checkbox(self, mouse_pos):
        flag = ""
        for method, checkbox in self.checkbox.items():
            clicked = checkbox.is_over(mouse_pos)
            if clicked:
                checkbox.checked = not checkbox.checked
                flag = method
                break
        if flag != "":
            for method in self.checkbox:
                if method != flag:
                    self.checkbox[method].checked = False

    def click_button(self, mouse_pos):
        self.next_scene = None
        self.button.is_over(mouse_pos)
        if not self.button.mouse_over:
            return
        for method, checkbox in self.checkbox.items():
            if checkbox.checked:
                self.next_scene = method
                return

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

