import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

#DEFINE COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#PLAYER CLASS
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50,50))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH/ 2, HEIGHT / 2)

  def update (self):
    self.rect.x += 5
    if self.rect.left > WIDTH:
      self.rect.right = 0

#INITIALIZE VARIABLES
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#SPRITE GROUPS
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#GAME LOOP:
#   Process Events
#   Update
#   Draw
running = True
while running:

    clock.tick(FPS)

    #PROCESS Events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    #UPDATE
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # FLIP AFTER DRAWING
    pygame.display.flip()

pygame.quit()
