import tkinter as tk
from random import *
import time
import math


class Snake:
    def __init__(self, pos_x, pos_y, vx, vy):
        '''
        initializing the snake, main controlable target in the game
        '''
        self.size = 40
        self.vx = vx
        self.vy = vy
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.shape = canvas.create_rectangle(self.pos_x,
                                             self.pos_y,
                                             self.pos_x + self.size,
                                             self.pos_y + self.size,
                                             fill='green')

    def set_coords(self):
        canvas.coords(self.shape,
                      self.pos_x,
                      self.pos_y,
                      self.pos_x + self.size,
                      self.pos_y + self.size)

    def check_boarders(self):
        '''
        replaces the snake to the opposite boarder if the field is over
        '''
        if self.pos_x > 480:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = 480
        if self.pos_y > 480:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = 480

    def move(self):
        '''
        reproduce the movement of the snake on the field
        '''
        self.pos_x += self.vx
        self.pos_y += self.vy
        self.check_boarders()
        self.set_coords()

    def check_collision(self):
        '''
        will must recognize the touch of the apple by the snake
        '''
        global speed_multiplier, body
        if self.pos_x == apple.pos_x and self.pos_y == apple.pos_y:
            speed_multiplier += 1
            canvas.delete(apple.shape)
            body.append(Body(snake.pos_x, snake.pos_y))
            apple.__init__()

    def up(self, event=None):
        if -40 < self.vy < 40:
            self.vx = 0
            self.vy -= 40

    def down(self, event=None):
        if -40 < self.vy < 40:
            self.vx = 0
            self.vy += 40

    def left(self, event=None):
        if -40 < self.vx < 40:
            self.vy = 0
            self.vx -= 40

    def right(self, event=None):
        if -40 < self.vx < 40:
            self.vy = 0
            self.vx += 40


class Body(Snake):
    def __init__(self, pos_x, pos_y, vx=None, vy=None):
        super().__init__(pos_x, pos_y, vx, vy)

    def set_body_coords(self):
        canvas.coords(self.shape,
                      self.pos_x,
                      self.pos_y,
                      self.pos_x + self.size,
                      self.pos_y + self.size)


class Apple:
    def __init__(self):
        '''initialize the apples - the main target in the game'''
        self.size = 40
        self.pos_x = choice(positions)
        self.pos_y = choice(positions)
        self.shape = canvas.create_rectangle(self.pos_x,
                                             self.pos_y,
                                             self.pos_x + self.size,
                                             self.pos_y + self.size,
                                             fill='red')


def refresh():
    for i in range(len(body)-1, -1, -1):
        if not i:
            body[i].pos_x = snake.pos_x
            body[i].pos_y = snake.pos_y
        else:
            body[i].pos_x = body[i - 1].pos_x
            body[i].pos_y = body[i - 1].pos_y
    root.after(snake_speed, snake.move)
    root.after(snake_speed, snake.check_collision)
    if body:
        for i in body:
            root.after(snake_speed, i.set_body_coords)
    root.after(snake_speed, refresh)


def main():
    global canvas, root, snake, positions, apple, speed_multiplier, snake_speed, body
    root = tk.Tk()
    speed_multiplier = 1
    snake_speed = 500
    positions = [40 * i for i in range(1, 12)]
    pos_x, pos_y = choice(positions), choice(positions)
    canvas = tk.Canvas(root, width=480, height=480)
    canvas.pack()
    apple = Apple()
    body = []
    snake = Snake(pos_x, pos_y, 0, 0)
    root.bind('<Down>', snake.down)
    root.bind('<Up>', snake.up)
    root.bind('<Left>', snake.left)
    root.bind('<Right>', snake.right)
    refresh()
    root.mainloop()


if __name__ == '__main__':
    main()
