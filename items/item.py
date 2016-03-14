import pygame


class item:
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type

        self.can_use = True


class item_type:
    weapon = 'weapon'
