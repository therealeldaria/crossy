# Pygame development 1
# Start the basic game set up
# Set up the display

import pygame
from pathlib import Path

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
game_over = False
data_file_path = Path('.') / 'Datafiles'
player_image = pygame.image.load(data_file_path / 'player.png')

# enemy_image = data_file_path / 'enemy.png'
# background_image = data_file_path / 'background.png'
# treasure_image = data_file_path / 'treasure.png'


game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)



def event_handler():
    for event in pygame.event.get():
        return event.type == pygame.QUIT

while not game_over:

    game_over = event_handler()

    # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)



    pygame.display.update()
    clock.tick(TICK_RATE)

pygame.quit()
quit()
