from Cell import Cell
import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None

    def draw(self):
        # Draw grid lines
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (self.width, i * 60), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, self.height), thickness)

        # Draw cell values
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    
