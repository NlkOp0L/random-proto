import pygame

from items.item import item, item_type
from items.ammo import ammo


class weapon(item):
    def __init__(self, name, weapon_type, damage, attack_range, ammo, clip_size, spread, parent_entity):
        super(weapon, self).__init__(name, item_type.weapon, parent_entity)

        self.weapon_type = weapon_type
        self.damage = damage
        self.attack_range = attack_range
        self.spread = spread

        self.ammo = ammo
        self.clip = 0
        self.clip_size = clip_size
        self.reload()

        self.fired = []

    def reload(self):
        if self.ammo > 0:
            delta = min(self.clip_size - self.clip, self.ammo)

            self.clip += delta
            self.ammo -= delta
            print('Reloded!  - ' + str(self.clip) + '/' + str(self.ammo))
        else:
            print('Empty!!')

    def fire(self, dest):
        if self.can_use:
            if self.clip > 0:
                self.clip -= 1
                self.fired.append(ammo('bullet', (self.parent_entity.x, self.parent_entity.y), dest, 500, self))
                print('Bang!     - ' + str(self.clip) + '/' + str(self.ammo))
            else:
                print('Reload!')
        else:
            print('Cannot use!')

    def update(self, elapsed):
        for bullet in self.fired:
            bullet.update(elapsed)

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, 0xff0000, (int(x), int(y)), int(self.attack_range), 1)

        for bullet in self.fired:
            bullet.draw(screen)

class weapon_type:
    gun = 'gun'
