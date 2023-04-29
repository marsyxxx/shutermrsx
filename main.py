from random import randint
from pygame import *

window = display.set_mode((700, 500))
background = transform.scale(image.load("4.png"), (700, 600))

mixer.init()
mixer.music.load(("space.ogg"))
mixer.music.play(-1)
kick = mixer.Sound("fire.ogg")


class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


'''class Enemy(GameSprite):
    def __init__(self, pl_image, speed, x, y, width, height):
        super().__init__(pl_image, speed, x, y, width, height)
        self.direction = 'left'
'''

lost = 0


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(0, 700 - self.width - 5)
            self.rect.y = 0
            lost = lost + 1


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if key_pressed[K_RIGHT] and self.rect.x < 700 - 65 - 5:
            self.rect.x += 5


rocket = Player("putin.png", 7, 400, 415, 60, 80)
enemy1 = Enemy("i.png", randint(1, 5), randint(0, 700 - 60 - 5), 0, randint(50, 70), 40)
enemy2 = Enemy("i.png", randint(1, 3), randint(0, 700 - 60 - 5), 0, randint(50, 70), 40)
enemy3 = Enemy("i.png", randint(1, 4), randint(0, 700 - 60 - 5), 0, randint(50, 70), 40)
enemy4 = Enemy("i.png", randint(1, 3), randint(0, 700 - 60 - 5), 0, randint(50, 70), 40)
enemy5 = Enemy("i.png", randint(1, 6), randint(0, 700 - 60 - 5), 0, randint(50, 70), 40)

enemys = sprite.Group()
enemys.add(enemy1)
enemys.add(enemy2)
enemys.add(enemy3)
enemys.add(enemy4)
enemys.add(enemy5)
font.init()
font = font.Font(None, 20)
win = font.render("YOU WIN", True, (28, 245, 24))
lose = font.render("YOU LOSE", True, (209, 15, 37))
score = font.render("СЧЕТ", True, (255, 255, 255))
FPS = 60
clock = time.Clock()

game = True
finish = False
while game:
    if finish != True:
        window.blit(background, (0, 0))
        rocket.reset()
        rocket.update()
        enemys.draw(window)
        enemys.update()
        text_lost = font.render("ПРОПУЩЕННО: "+ str(lost), True, (255, 255, 255))
        window.blit(text_lost, (5, 5))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
