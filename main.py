import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


SIZE = WIDTH, HEIGHT = 300, 300
pygame.init()
screen = pygame.display.set_mode(SIZE)
screen.fill('white')
is_draw = False
running = True
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("creature.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.x = 10
sprite.rect.y = 10
all_sprites.draw(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite.rect.x -= 10
            if event.key == pygame.K_RIGHT:
                sprite.rect.x += 10
            if event.key == pygame.K_UP:
                sprite.rect.y -= 10
            if event.key == pygame.K_DOWN:
                sprite.rect.y += 10
            screen.fill('white')
            all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
