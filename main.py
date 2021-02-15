

import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

####

# Inicializando o pygame e criando a Janela
import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
import random

pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Super Jogo 01")

# Groups
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

# Background!!
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/sprits/desert.png")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)


# Music
pygame.mixer.music.load("data/musics/TremLoadingloopl.wav")
pygame.mixer.music.play(-1)

# Sounds
shoot = pygame.mixer.Sound("data/sounds/RPG Sound Pack/interface/interface2.wav")

gameLoop = True
gameOver = False
time = 0
clock = pygame.time.Clock()
if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameOver:
                    shoot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center


        # Update logic:
        if not gameOver:
            objectGroup.update()

            time += 1
            if time > 30:
                time = 0
                if random.random() < 0.5:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup)
                    print("new asteroid")

            collisions = pygame.sprite.spritecollide(player, asteroidGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print("Game over!")
                gameOver = True

            hits = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

        # Draw:
        display.fill([0, 0, 0])
        objectGroup.draw(display)
        pygame.display.update()

