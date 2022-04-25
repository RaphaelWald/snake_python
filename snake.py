from collections import deque


class Snake:
    def __init__(self, game, direction="right"):
        self.deque = deque([(20, 20), (21, 20), (22, 20), (23, 20)])
        self.game = game
        self.direction = direction
        self.display_deque()
        self.moving = True

    def _contains__(self, field):
        f_x, f_y = field
        for x, y in self.deque:
            if x == f_x and y == f_y:
                return True
        return False

    def update_deque(self):

        head_x, head_y = self.deque[-1]
        head_field = self.game.fields[head_x][head_y]
        if head_field.bonus:
            head_field.bonus = False
            self.game.generate_new_bonus()
        else:
            tail_x, tail_y = self.deque.popleft()
            self.game.fields[tail_x][tail_y].update((255, 255, 255))
        head_field.update((0, 200, 0))

        if self.direction == "right" and head_x+1 < len(self.game.fields) and (head_x+1, head_y) not in self.deque:
            self.deque.append((head_x+1, head_y))
        elif self.direction == "down" and head_y+1 < len(self.game.fields) and (head_x, head_y+1) not in self.deque:
            self.deque.append((head_x, head_y+1))
        elif self.direction == "up" and head_y-1 >= 0 and (head_x, head_y-1) not in self.deque:
            self.deque.append((head_x, head_y-1))
        elif self.direction == "left" and head_x-1 >= 0 and (head_x-1, head_y) not in self.deque:
            self.deque.append((head_x-1, head_y))
        else:
            self.moving = False
            self.display_deque((255, 0, 0))

    def display_deque(self, color=(0, 200, 0)):
        for x, y in self.deque:
            self.game.fields[x][y].update(color)
