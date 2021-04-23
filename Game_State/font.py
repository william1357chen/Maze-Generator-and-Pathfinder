import pygame
from pygame.math import Vector2
from .color import Color
from .constants import Constants


class Font:
    def __init__(self, x, y, msg, color=Color.WHITE, font=Constants.FONT, font_size=0):
        self.position = Vector2(x, y)
        self.msg = msg
        self.color = color
        self.font = pygame.font.Font(font, font_size)

    def render(self, screen):
        msg = self.font.render(self.msg, True, self.color)
        screen.blit(msg, (self.position.x, self.position.y))
