import pygame, math

from entities.entity import entity


class player(entity):
    def __init__(self, x, y, width, height, speed, move_range):
        super(player, self).__init__(x, y, width, height, speed, move_range)

        self.tx = self.x
        self.ty = self.y

    def move(self, elapsed):
        if self.can_move:
            dx = self.tx - self.x
            dy = self.ty - self.y
            dist = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

            if dist > self.width / 2:
                travelled_x = (dx / dist) * self.speed * elapsed
                travelled_y = (dy / dist) * self.speed * elapsed
                self.travelled += math.sqrt(math.pow(travelled_x, 2) + math.pow(travelled_y, 2))

                if self.move_range - self.travelled < self.width / 2:
                    self.stop_moving()

                self.x += travelled_x
                self.y += travelled_y

            self.move_start_x = self.x
            self.move_start_y = self.y

    def set_destination(self, pos):
        if self.can_move:
            self.tx = pos[0]
            self.ty = pos[1]

    def set_new_turn(self):
        self.can_move = True
        self.travelled = 0

    def stop_moving(self):
        self.set_destination((self.x, self.y))
        self.can_move = False

    def update(self, elapsed):
        self.move(elapsed)

    def draw(self, screen):
        pygame.draw.circle(screen, 0xFFFF00, (int(self.move_start_x), int(self.move_start_y)), int(self.move_range - self.travelled))
        pygame.draw.circle(screen, 0x0000ff, (int(self.x), int(self.y)), int(self.width))