import pygame
import random

class Grid:
    """
    Represents a grid of cells for the Game of Life simulation.
    """

    def __init__(self, width, height, cell_size):
        """
        Initializes the grid with the given dimensions and cell size.

        Args:
            width: The width of the grid.
            height: The height of the grid.
            cell_size: The size of each individual cell.
        """
        self.rows = height // cell_size  # Number of rows in the grid
        self.columns = width // cell_size  # Number of columns in the grid
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]  # 2D list representing cell states (0 = dead, 1 = alive)

    def draw(self, window):
        """
        Draws the grid onto the given window surface.

        Args:
            window: The Pygame window surface to draw on.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                color = (255, 192, 203) if self.cells[row][column] else (139, 69, 19)  # Color based on cell state
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))  # Draw cell rectangle

    def fill_random(self):
        """
        Randomly fills the grid with live and dead cells.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([1, 0, 0, 0])  # Higher chance of dead cells

    def clear(self):
        """
        Clears the grid, setting all cells to the dead state.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0

    def toggle_cell(self, row, column):
        """
        Toggles the state (live/dead) of the cell at the given row and column.

        Args:
            row: The row of the cell.
            column: The column of the cell.
        """
        if 0 <= row < self.rows and 0 <= column < self.columns:  # Check if within grid bounds
            self.cells[row][column] = not self.cells[row][column]