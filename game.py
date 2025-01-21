import pygame
import sys

pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white
    screen.fill((255, 255, 255))

    # Draw a red rectangle
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200, 100))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
