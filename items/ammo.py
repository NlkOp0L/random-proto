import pygame, math

from items.item import item, item_type


class ammo(item):
    def __init__(self, name, start, end, speed, parent_weapon):
        super(ammo, self).__init__(name, item_type.ammo, parent_weapon)

        self.x = start[0]
        self.y = start[1]
        self.end_x = end[0]
        self.end_y = end[1]

        self.travelled = 0

        self.speed = speed
        self.parent_weapon = parent_weapon

    def update(self, elapsed):
        dx = self.end_x - self.x
        dy = self.end_y - self.y
        dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        travelled_x = (dx / dist) * self.speed * elapsed
        travelled_y = (dy / dist) * self.speed * elapsed
        self.travelled += math.sqrt(math.pow(travelled_x, 2) + math.pow(travelled_y, 2))

        if self.parent_weapon.attack_range < self.travelled:
            self.parent_weapon.fired.remove(self)
        else:
            self.x += travelled_x
            self.y += travelled_y

    def draw(self, screen):
        pygame.draw.circle(screen, 0xffffff, (int(self.x), int(self.y)), int(5))
