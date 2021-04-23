from Maze_Generation.prim_alg import PrimAlgorithm
import pygame

from Scene import StartMenu, DepthFirstScene, KruskalScene, PrimScene
from Game_State import GameState, Color

WIDTH = 1200
HEIGHT = 800
FPS = 60
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Maze Generator and Pathfinder")
clock = pygame.time.Clock()
game_state = GameState(screen)
scene_list = {
    "start_menu": StartMenu(game_state),
    "method1": DepthFirstScene(game_state),
    "method2": KruskalScene(game_state),
    "method3": PrimScene(game_state),
}

current_scene = None


def switch_scene(method):
    global current_scene
    current_scene = scene_list[method]
    current_scene.initialize()


def initialize():
    switch_scene("start_menu")


def process_input():
    current_scene.process_input()


def update():
    current_scene.update()


def render():
    screen.fill(Color.DARK_GREY)
    current_scene.render()
    pygame.display.update()


def main():
    initialize()

    while True:
        process_input()
        update()
        if game_state.next_scene is not None:
            switch_scene(game_state.next_scene)
        render()
        # clock.tick(FPS)


if __name__ == "__main__":
    main()
