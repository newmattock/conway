from grid import Grid

class Simulation:
    """
    Represents the Conway's Game of Life simulation.
    """

    def __init__(self, width, height, cell_size):
        """
        Initializes the simulation with the given dimensions and cell size.

        Args:
            width: The width of the simulation grid.
            height: The height of the simulation grid.
            cell_size: The size of each individual cell.
        """
        self.grid = Grid(width, height, cell_size)  # Main grid holding cell states (0 = dead, 1 = alive)
        self.temp_grid = Grid(width, height, cell_size)  # Temporary grid used during updates
        self.rows = height // cell_size  # Number of rows in the grid
        self.columns = width // cell_size  # Number of columns in the grid
        self.run = False  # Flag indicating if the simulation is running

    def draw(self, window):
        """
        Draws the current state of the simulation grid onto the given window.

        Args:
            window: The Pygame window surface to draw on.
        """
        self.grid.draw(window)  # Delegate drawing to the Grid object

    def living(self, grid, row, column):
        """
        Counts the number of live neighbors for a cell at the given row and column.

        Args:
            grid: The grid to check for neighbors.
            row: The row of the cell.
            column: The column of the cell.

        Returns:
            The number of live neighbors.
        """
        live_cell = 0
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # Neighboring cell offsets
        for offset in offsets:
            updated_row = (row + offset[0]) % self.rows  # Handle grid wrapping (toroidal topology)
            updated_column = (column + offset[1]) % self.columns
            if grid.cells[updated_row][updated_column] == 1:  # Check if neighbor is alive
                live_cell += 1
        return live_cell

    def update(self):
        """
        Updates the state of the simulation grid according to Conway's Game of Life rules.
        """
        if self.running():  # Only update if the simulation is running
            for row in range(self.rows):
                for column in range(self.columns):
                    live_cell = self.living(self.grid, row, column)  # Count live neighbors
                    cell_value = self.grid.cells[row][column]  # Current state of the cell

                    # Apply Game of Life rules:
                    if cell_value == 1:  # Live cell
                        if live_cell > 3 or live_cell < 2:
                            self.temp_grid.cells[row][column] = 0  # Cell dies (overpopulation or underpopulation)
                        else:
                            self.temp_grid.cells[row][column] = 1  # Cell survives
                    else:  # Dead cell
                        if live_cell == 3:
                            self.temp_grid.cells[row][column] = 1  # Cell is born (reproduction)
                        else:
                            self.temp_grid.cells[row][column] = 0  # Cell remains dead

            # Copy updated states from temporary grid to main grid
            for row in range(self.rows):
                for column in range(self.columns):
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def running(self):
        """
        Returns True if the simulation is currently running, False otherwise.
        """
        return self.run

    def start(self):
        """
        Starts the simulation.
        """
        self.run = True

    def stop(self):
        """
        Stops the simulation.
        """
        self.run = False

    def clear(self):
        """
        Clears the simulation grid, setting all cells to the dead state.
        """
        if not self.running():  # Only clear if the simulation is not running
            self.grid.clear()

    def create_random_state(self):
        """
        Randomly initializes the simulation grid with live and dead cells.
        """
        if not self.running():  # Only randomize if the simulation is not running
            self.grid.fill_random()

    def toggle_cell(self, row, column):
        """
        Toggles the state (live/dead) of the cell at the given row and column.

        Args:
            row: The row of the cell.
            column: The column of the cell.
        """
        if not self.running():  # Only toggle cells if the simulation is not running
            self.grid.toggle_cell(row, column)