import pygame
from pygame import gfxdraw
from .color import Color


class CheckBox:
    def __init__(self, x, y, width, color=Color.WHITE, thickness=5):
        self.mouse_over = False
        self.checked = False
        self.rect = pygame.Rect(x, y, width, width)
        self.layer = pygame.Rect(
            x + thickness, y + thickness, width - 2 * thickness, width - 2 * thickness
        )
        self.color = color
        self.width = width
        self.thickness = thickness
        self.alpha = 100

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if not self.checked:
            pygame.draw.rect(screen, Color.BACKGROUND_COLOR, self.layer)

        if self.mouse_over:
            self.draw_trans_button(screen)

    def draw_trans_button(self, screen):
        gfxdraw.box(screen, self.rect, (*self.color, self.alpha))

    def is_over(self, mouse_pos):
        self.mouse_over = self.rect.collidepoint(mouse_pos)
        return self.mouse_over
