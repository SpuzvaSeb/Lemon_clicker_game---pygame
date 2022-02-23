import pygame
import sys
import os

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Standing Lemons')

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

WINDOW_SIZE = (500, 400)

WHITE = ((255, 255, 255))

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300,300))

font = pygame.font.SysFont('verdana', 25)
button_font = pygame.font.SysFont('verdana', 15)

def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(img_folder, name)
    image = pygame.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Lemon():
    def __init__(self):

        self.lemon, self.lemon_rect = load_image("lemon.bmp", -1, 6)
        self.lemon_rect[0] = 105
        self.lemon_rect[1] = 75

        self.juicer_button, self.juicer_button_rect = load_image("lemon_button.bmp", 0)
        self.juicer_button_rect[0] = 50
        self.juicer_button_rect[1] = 350

        self.kids_button, self.kids_button_rect = load_image("lemon_button.bmp", 0)
        self.kids_button_rect[0] = 200
        self.kids_button_rect[1] = 350

        self.ape_button, self.ape_button_rect = load_image("lemon_button.bmp", 0)
        self.ape_button_rect[0] = 350
        self.ape_button_rect[1] = 350

        self.lemons = 0
        self.lpc = 1
        self.lps = 0

        self.juicers = 0
        self.kids = 0
        self.apes = 0

        self.clicked = False

    def make_lemons(self):
        self.lemons += self.lps 


    def update(self):

        screen.blit(self.lemon, (105, 75))

        screen.blit(self.juicer_button, (50, 350))

        screen.blit(self.kids_button, (200, 350))

        screen.blit(self.ape_button, (350, 350))


        screen.blit(font.render(f'Lemons: {round(self.lemons)}', True, WHITE), (180, 0))

        screen.blit(font.render(f'Lemons per Second: {round(self.lps * 30)}', True, WHITE), (130, 30))

        screen.blit(button_font.render(f'Juicers: {self.juicers}', True, WHITE), (75, 350))

        screen.blit(button_font.render('Cost: 100', True, WHITE), (75, 375))

        screen.blit(button_font.render(f'Hired kids: {self.kids}', True, WHITE), (205, 350))

        screen.blit(button_font.render('Cost: 100', True, WHITE), (225, 375))

        screen.blit(button_font.render(f'Hired apes: {self.apes}', True, WHITE), (355, 350))

        screen.blit(button_font.render('Cost: 250', True, WHITE), (373, 375))

        if pygame.mouse.get_pressed()[0] and self.lemon_rect.collidepoint(pygame.mouse.get_pos()) and not self.clicked:
            self.clicked = True
            self.lemons += self.lpc
    
        elif pygame.mouse.get_pressed()[0] and self.juicer_button_rect.collidepoint(pygame.mouse.get_pos()) and self.lemons >= 100 and not self.clicked:
            self.clicked = True

            self.lpc += 1
            self.lemons -= 100
            self.juicers += 1

        elif pygame.mouse.get_pressed()[0] and self.kids_button_rect.collidepoint(pygame.mouse.get_pos()) and self.lemons >= 100 and not self.clicked:
            self.clicked = True

            self.lps += 0.0333
            self.lemons -= 100
            self.kids += 1

        elif pygame.mouse.get_pressed()[0] and self.ape_button_rect.collidepoint(pygame.mouse.get_pos()) and self.lemons >= 250 and not self.clicked:
            self.clicked = True

            self.lps += 0.1333
            self.lemons -= 250
            self.apes += 1

        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False


lemon = Lemon()

while True:
    screen.fill((35, 179, 255))

    lemon.update()
    lemon.make_lemons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()


    pygame.display.update()
    clock.tick(30)