import pygame


class Scene:
    def __init__(self, game_state):
        self.game_state = game_state

    def initialize(self):
        raise NotImplementedError

    def process_input(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError
