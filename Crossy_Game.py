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
pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 75)


class Game:
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def win_lose(self, condition):
        if condition:
            text = 'You Win! :)'
        else:
            text = 'You Lose! :('

        text = FONT.render(text, True, BLACK_COLOR)
        self.game_screen.blit(text, (275, 350))
        pygame.display.update()
        CLOCK.tick(1)
        return condition

    def run_game_loop(self):
        game_over = False
        did_win = False
        direction = 0

        background = GameObject('background.png', 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        player_character = Player('player.png', 375, 700, 50, 50)
        enemy_0 = Enemy('enemy.png', 20, 375, 30, 30)
        enemy_1 = Enemy('enemy.png', 300, 175, 100, 100)
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

            self.game_screen.fill(WHITE_COLOR)

            background.draw(self.game_screen)
            treasure.draw(self.game_screen)
            player_character.move(direction, self.game_screen)
            player_character.draw(self.game_screen)
            enemy_0.move(self.game_screen)
            enemy_0.draw(self.game_screen)
            enemy_1.move(self.game_screen)
            enemy_1.draw(self.game_screen)

            if player_character.collision_detected(enemy_0):
                did_win = self.win_lose(False)
                break
            elif player_character.collision_detected(enemy_1):
                did_win = self.win_lose(False)
                break
            elif player_character.collision_detected(treasure):
                did_win = self.win_lose(True)
                break

            pygame.display.update()
            CLOCK.tick(self.TICK_RATE)
        if did_win:
            self.run_game_loop()
        else:
            return


class GameObject:

    def __init__(self, image_name, x_pos, y_pos, width, height):
        object_image = pygame.image.load(str(DATA_FILE_PATH / image_name)).convert()
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class Player(GameObject):

    SPEED = 10

    def __init__(self, image_name, x_pos, y_pos, width, height):
        super().__init__(image_name, x_pos, y_pos, width, height)

    def move(self, direction, screen):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        if self.y_pos >= screen.get_height() - 70:
            self.y_pos = screen.get_height() - 70

    def collision_detected(self, other_object):
        if self.y_pos > other_object.y_pos + other_object.height:
            return False
        elif self.y_pos + self.height < other_object.y_pos:
            return False
        if self.x_pos + self.width < other_object.x_pos:
            return False
        elif self.x_pos > other_object.x_pos + other_object.width:
            return False
        return True


class Enemy(GameObject):

    SPEED = 10

    def __init__(self, image_name, x_pos, y_pos, width, height):
        super().__init__(image_name, x_pos, y_pos, width, height)

    def move(self, screen):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        if self.x_pos >= screen.get_width() - 70:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()
