import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""
	
	def __init__(self, ai_settings, screen, ship):
		"""Create abullet rect at (0, 0) and then set correct position."""
		super(Bullet, self).__init__()
		self.screen = screensize
		
