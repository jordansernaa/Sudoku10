import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.editable = value == 0
        self.selected = False

  

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.SysFont('Arial', 40)
        small_font = pygame.font.SysFont('Arial', 20)
        x = self.col * 60
        y = self.row * 60
