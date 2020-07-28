import tkinter as tk
from random import randint as rnd, choice
import time

n = 0

class Ball:
    def __init__(self):
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = rnd(30, 50)
        self.x = rnd(self.r, 800 - self.r)
        self.y = rnd(self.r, 600 - self.r)
        self.dx, self.dy = (rnd(3, 10), rnd(3, 10))
        self.ball_id = canvas.create_oval(self.x - self.r,
                                   self.y - self.r,
                                   self.x + self.r,
                                   self.y + self.r,
                                   fill=choice(self.colors), width=0)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > 800 or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > 600 or self.y - self.r <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def canvas_click(event):
        global n
        ball.ball_click()
        if (posx-event.x)**2 + (posy-event.y)**2<=R**2:
            n += 50
            print('У вас', n, 'очков!')
        else:
            n = 0
            print('Мимо!')

    def ball_click(self):
        global posx, posy, R

        posx = self.x
        posy = self.y
        R = self.r


def dvig():
    ball.move()
    ball.show()
    root.after(30, dvig)


def main():
    global root, canvas, ball, event

    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.bind('<Button-1>', Ball.canvas_click)
    ball = Ball()
    dvig()
    root.mainloop()

if __name__ == '__main__':
    main()
