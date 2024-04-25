import pygame, sys
from simulation import Simulation

pygame.init()

brown = (139,69,19)
cell_size = 10
width = 750
height = 750
fps = 60


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mana")

clock = pygame.time.Clock()
simulation = Simulation(width, height, cell_size)

# Simulation Loop
while True:
    # Event Handling
    for event in pygame.event.get():
        # Checks for the quit action, allows the game to be exited
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Checking for user input 
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Grabs the position of the mouse when it is clicked, and either creates a cell or deletes a cell at that location
            pos = pygame.mouse.get_pos()
            row = pos[1] // cell_size
            column = pos[0] // cell_size
            simulation.toggle_cell(row, column)
        
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is held
                pos = pygame.mouse.get_pos()
                row = pos[1] // cell_size
                column = pos[0] // cell_size
                simulation.toggle_cell(row, column)  # Place/remove cell
            # Checking for key input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Simulation is running")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Simulation has stopped")
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()


    
    # Updates state of grid
    simulation.update()

    #Displaying game
    window.fill(brown)
    simulation.draw(window)

    #Updates the display and ticks at the set frame rate or lower
    pygame.display.update()
    clock.tick(fps)