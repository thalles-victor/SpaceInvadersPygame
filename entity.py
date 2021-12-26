import pygame
from colors import PrintColors
class Entity:
  def __init__(self, image_src: str, pos_x : float, pos_y: float, speed: float = 0.1, direction : str = None):
    self.image_src = image_src
    self.Player = pygame.image.load(self.image_src)

    self.height = self.Player.get_height()
    self.width = self.Player.get_width()

    self.center_pos_x = pos_x - (self.width / 2)
    self.center_pos_y = pos_y - (self.height /2)
    
    self.speed = speed
    self.direction = direction

  def getPositionCenter(self):
    return {
      "x": self.center_pos_x,
      "y": self.center_pos_y
    }
  def tick(self):
    self.move_entity()

  def setDirection(self, dir: str):
    """ dir: "Up" | "Down" | "Left" | "Right" """
    if dir == "Up" or dir =="Down" or dir == "Left" or dir == "Right":
      self.direction = dir
    else:
      print(PrintColors.FAIL + "<" +  dir + ">"  +" is not valid valid")
      exit()

  def move_entity(self):
    if self.direction == "Up":
      self.center_pos_y -= self.speed
    if self.direction == "Down":
      self.center_pos_y += self.speed
    if self.direction == "Left":
      self.center_pos_x -= self.speed
    if self.direction == "Right":
      self.center_pos_x += self.speed
