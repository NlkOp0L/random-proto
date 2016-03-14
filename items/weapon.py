import pygame

from items.item import item, item_type


class weapon(item):
    def __init__(self, name, weapon_type, damage, attack_range, ammo, clip_size):
        super(weapon, self).__init__(name, item_type.weapon)

        self.weapon_type = weapon_type
        self.damage = damage
        self.attack_range = attack_range

        self.ammo = ammo
        self.clip = 0
        self.clip_size = clip_size
        self.reload()

    def reload(self):
        if self.ammo > 0:
            delta = min(self.clip_size - self.clip, self.ammo)

            self.clip += delta
            self.ammo -= delta
            print('Reloded!  - ' + str(self.clip) + '/' + str(self.ammo))
        else:
            print('Empty!!')

    def fire(self):
        if self.can_use:
            if self.clip > 0:
                self.clip -= 1
                print('Bang!     - ' + str(self.clip) + '/' + str(self.ammo))
            else:
                print('Reload!')
        else:
            print('Cannot use!')

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, 0xff0000, (int(x), int(y)), int(self.attack_range), 1)

class weapon_type:
    gun = 'gun'
