import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/sprits/spaceships01.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed_X = 0.5
        self.speed_Y = 0.5
        self.acceleration = 0.1

    def update(self, *args):

        # LOGICA!
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed_Y -= self.acceleration

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed_Y += self.acceleration

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.speed_X -= self.acceleration

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.speed_X += self.acceleration

        else:
            self.speed_Y *= 0.95
            self.speed_X *= 0.95

        self.rect.y += self.speed_Y
        self.rect.x += self.speed_X

        # Delimitando o espaçoa à ser jogado. Para que o player não saia da tela!
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed_Y = 0

        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed_Y = 0

        elif self.rect.right > 840:
            self.rect.right = 840
            self.speed_X = 0

        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed_X = 0