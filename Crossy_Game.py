import pygame
from pathlib import Path

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy'
DATA_FILE_PATH = Path('.') / 'Datafiles'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
CLOCK = pygame.time.Clock()


class Game:
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    @staticmethod
    def event_handler(character):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    character.move(character, 1)
                elif event.key == pygame.K_DOWN:
                    character.move(character, -1)
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    character.move(character, 0)
            return event.type == pygame.QUIT

    def run_game_loop(self):
        game_over = False

        player_character = Player('player.png', 375, 700, 50, 50)

        while not game_over:

            game_over = self.event_handler(player_character)

            player_character.draw(self.game_screen)

            pygame.display.update()
            CLOCK.tick(self.TICK_RATE)


class GameObject:

    def __init__(self, image_name, x_pos, y_pos, width, height):
        object_image = pygame.image.load(str(DATA_FILE_PATH / image_name)).convert()
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, self.x_pos, self.y_pos)


class Player(GameObject):

    SPEED = 10

    def __init__(self, image_name, x_pos, y_pos, width, height):
        super().__init__(image_name, x_pos, y_pos, width, height)

    def move(self, direction):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED


new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()
