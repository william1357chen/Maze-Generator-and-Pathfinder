import pygame
from pygame import gfxdraw
from pygame.math import Vector2
from .color import Color
import math

# Start Button Class
class Button:
    def __init__(self, x, y, color=Color.WHITE, radius=50):
        # If mouse is over button: True, else: False
        self.mouse_over = False
        self.center = Vector2(x, y)
        self.color = color
        self.radius = radius
        self.alpha = 100

        self.polygon_lenth = 20

    def render(self, screen):
        # pygame.draw.circle(screen, (255,0,0), self.rect, 5)
        pygame.draw.circle(screen, self.color, self.center, self.radius, width=5)
        temp = self.polygon_lenth * math.sqrt(3)
        pygame.draw.polygon(
            screen,
            self.color,
            (
                (self.center.x + (2 / 3 * temp), self.center.y),
                (self.center.x - (temp / 3), self.center.y + self.polygon_lenth),
                (self.center.x - (temp / 3), self.center.y - self.polygon_lenth),
            ),
        )
        if self.mouse_over:
            self.draw_trans_button(screen)

    def draw_trans_button(self, screen):
        gfxdraw.filled_circle(
            screen,
            int(self.center.x),
            int(self.center.y),
            self.radius,
            (*(self.color), self.alpha),
        )

    def is_over(self, mouse_pos):
        # if the distance between center and mouse_pos is less than the radius of the circle
        # this means the mouse cursor is inside the circle
        distance = math.sqrt(
            (self.center.x - mouse_pos[0]) ** 2 + (self.center.y - mouse_pos[1]) ** 2
        )
        self.mouse_over = distance <= self.radius
        return self.mouse_over
