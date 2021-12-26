class ScreenDimension:
  def __init__(self, WIDTH: int = 800, HEIGHT: int = 600, SIZE: int = 1):
    self.WIDTH = WIDTH * SIZE
    self.HEIGHT = HEIGHT * SIZE
    self.SIZE = SIZE
  
  def get_dimentison(self):
    return(
      self.WIDTH,
      self.HEIGHT
    )