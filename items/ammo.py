import pygame, math

from items.item import item, item_type


class ammo(item):
    def __init__(self, name, start, end, speed, parent_weapon):
        super(ammo, self).__init__(name, item_type.ammo, parent_weapon)

        self.travelled = 0
        self.speed = speed
        self.parent_weapon = parent_weapon

        # currentposition
        self.x = start[0]
        self.y = start[1]

        # Direction vector
        x1 = end[0] - self.x
        y1 = end[1] - self.y
        n1 = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2))

        # X Absissa vector
        x2 = 1
        y2 = 0
        n2 = 1

        # Direction vector angle
        angle = math.acos((x1*x2 + y1*y2) / (n1 * n2))
        if y1 < 0:
            angle = -angle

        # End point coordinates
        self.end_x = self.x + self.parent_weapon.attack_range * math.cos(angle)
        self.end_y = self.y + self.parent_weapon.attack_range * math.sin(angle)

    def update(self, elapsed):
        # Distance to travel
        dx = self.end_x - self.x
        dy = self.end_y - self.y
        dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

        # Distance to travel this tick ( d = (u / |u|) * v * t )
        travelled_x = (dx / dist) * self.speed * elapsed
        travelled_y = (dy / dist) * self.speed * elapsed
        self.travelled += math.sqrt(math.pow(travelled_x, 2) + math.pow(travelled_y, 2))

        # Move the ammo or destroy it
        if self.parent_weapon.attack_range < self.travelled:
            self.parent_weapon.fired.remove(self)
        else:
            self.x += travelled_x
            self.y += travelled_y

    def draw(self, screen):
        pygame.draw.circle(screen, 0xffffff, (int(self.x), int(self.y)), int(5))
