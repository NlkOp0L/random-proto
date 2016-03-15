import pygame


class item:
    def __init__(self, name, item_type, parent_entity):
        self.name = name
        self.item_type = item_type
        self.parent_entity = parent_entity

        self.can_use = True


class item_type:
    weapon = 'weapon'
    ammo = 'ammo'
