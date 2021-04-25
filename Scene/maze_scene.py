from .scene import Scene
from Game_State import Constants, Color
from utils import CellCoord, Instruction
import pygame
import time


class MazeScene(Scene):
    def __init__(self, game_state):
        self.game_state = game_state
        self.instructions = []
        self.counter = 0
        self.coord = CellCoord(0, 0)
        self.alg = None

    def initialize(self):
        self.game_state.next_scene = None
        self.reset()
        self.make_walls()
        self.alg.run()
        print("finished algorithm")

    def reset(self):
        self.counter = 0
        self.instructions.clear()
        self.coord = CellCoord(0, 0)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.counter < len(self.instructions) - 1:
                continue
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
        if self.counter == len(self.instructions):
            # print('instructions empty')
            return
        else:
            instruction = self.instructions[self.counter]
            instruction.run()
            self.counter += 1
            if self.counter >= Constants.NODE_LENGTH_COUNT * Constants.NODE_WIDTH_COUNT:
                time.sleep(0.05)

    def render(self):
        self.game_state.render()

    def make_walls(self):
        while self.coord.row <= Constants.NODE_LENGTH_COUNT - 1:
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
            curr_node.status = "unvisited"
            if state == "path":
                curr_node.setup_neighbours()

            self.instructions.append(
                Instruction(curr_node, Color.WALL, state=state, status="unvisited")
            )

            if self.coord.col >= Constants.NODE_WIDTH_COUNT - 1:
                self.coord.row += 1
                self.coord.col = 0
            else:
                self.coord.col += 1
        # print(len(self.instructions))

