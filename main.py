import pygame
from colors import PrintColors
from viewparams import ScreenDimension
from player import Player
from enemy import Enemy

pygame.init()

#Create the screen
dimension = ScreenDimension(SIZE=1)
screen = pygame.display.set_mode( dimension.get_dimentison() )
print(screen.get_width())

#Title and icon
pygame.display.set_caption( "Space Invaders", "icon" )
icon = pygame.image.load( "./assets/outer-space.png" )
pygame.display.set_icon(icon)


player = Player( image_src="./assets/space-invaders.png", pos_x=screen.get_width()/2, pos_y=400 )
enemy = Enemy( image_src="./assets/comet.png", pos_x=500, pos_y=300 )

def render():
  screen.blit( player.Player, ( player.getPositionCenter()["x"], player.getPositionCenter()["y"] ) )
  screen.blit( enemy.Player, ( enemy.getPositionCenter()["x"], enemy.getPositionCenter()["y"]) )

# Game loop
running: bool = True
while running:
  screen.fill( ( 0, 150, 0 ) )
  player.tick()
  player.setDirection(dir="Up")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # RGB = Red, Green, Blue
  render()
  pygame.display.update()