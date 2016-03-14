import pygame


class entity:
    def __init__(self, x, y, width, height, health, speed, move_range):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.move_range = move_range
        self.move_start_x = self.x
        self.move_start_y = self.y

        self.heatlh = health

        self.travelled = 0
        self.can_move = True

        self.weapons = {}
        self.powers = {}

    def update(self, elapsed):
        pass

    def draw(self, screen):
        pass
