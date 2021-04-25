import pygame
from pygame import mouse
from utils import CellCoord

from .scene import Scene
from Game_State import Constants, Node, Button, Color, Font, CheckBox


class StartMenu(Scene):
    def __init__(self, game_state):
        super().__init__(game_state)

    def initialize(self):
        # Initialize Maze
        for row in range(Constants.NODE_LENGTH_COUNT):
            for col in range(Constants.NODE_WIDTH_COUNT):
                if (col, row) == Constants.START_CORD:
                    color = Color.RED
                else:
                    color = Color.WHITE
                self.game_state.maze[row][col] = Node(
                    False,
                    Constants.MAZE_POSITION.x + col * Node.WIDTH,
                    Constants.MAZE_POSITION.y + row * Node.HEIGHT,
                    color,
                    CellCoord(col, row),
                )
        # Initialize Font
        self.game_state.font = {
            "title": Font(
                50, 50, "Random Maze Generation", font_size=40, color=Color.BLACK
            ),
            "step1": Font(
                50,
                120,
                "Step 1. Check one of the options",
                font_size=30,
                color=Color.BLACK,
            ),
            "method1": Font(50, 200, "Randomized Depth-First Search", font_size=25),
            "method2": Font(50, 300, "Randomized Kruskal's algorithm", font_size=25),
            "method3": Font(50, 400, "Randomized Prim's algorithm", font_size=25),
            "step2": Font(
                50, 500, "Step 2. Press Start Button", font_size=30, color=Color.BLACK,
            ),
        }
        # Initialize Checkboxes
        self.game_state.checkbox = {
            "method1": CheckBox(470, 190, 45),
            "method2": CheckBox(470, 290, 45),
            "method3": CheckBox(470, 390, 45),
        }

        # Initialize Start Button
        self.game_state.button = Button(250, 650, color=Color.WHITE)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # click a checkbox
                mouse_pos = pygame.mouse.get_pos()
                self.game_state.click_checkbox(mouse_pos)

                # click button
                self.game_state.click_button(mouse_pos)

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                self.game_state.button.is_over(mouse_pos)
                for checkbox in self.game_state.checkbox.values():
                    checkbox.is_over(mouse_pos)

    def update(self):
        ...

    def render(self):
        self.game_state.render()
