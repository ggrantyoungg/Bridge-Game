import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, color, actions):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x = x
        self.y = y
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.actions = actions

    def move(self, dx=0):
        self.x += dx

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
