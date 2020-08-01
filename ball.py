import tkinter as tk
from random import randint as rnd, choice
import time
from typing import Any, Union

points = 0


class Ball:
    def __init__(self):
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.n = 0
        self.r = rnd(30, 50)
        self.x = rnd(self.r, 800 - self.r)
        self.y = rnd(self.r, 600 - self.r)
        self.dx, self.dy = (rnd(3, 10), rnd(3, 10))  # присваивает случайную скорость для шара
        self.ball_id = canvas.create_oval(self.x - self.r,  # создает овал
                                          self.y - self.r,
                                          self.x + self.r,
                                          self.y + self.r,
                                          fill=choice(self.colors), width=0)

    def chek_inside(self, x, y):
        pass

    def show(self):  # двигает шар со скоростью дх ду
        canvas.move(self.ball_id, self.dx, self.dy)

    def move(self):  # отражает шар от стенок
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > 800 or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > 600 or self.y - self.r <= 0:
            self.dy = -self.dy


def blink():
    root.after(1500, deleteall)
    ball1.__init__()
    ball2.__init__()
    root.after(1500, blink)


def deleteall():
    canvas.delete(tk.ALL)


def movement():  # перемещает шар по полю
    ball2.show()
    ball2.move()
    ball1.show()
    ball1.move()
    root.after(30, movement)


def canvas_click_chek(event):
    global points
    if (ball1.x - event.x) ** 2 + (ball1.y - event.y) ** 2 <= ball1.r ** 2:
        ball1.n += 50  # считает очки при попадании в конкретный шар
        points += 50
    elif (ball2.x - event.x) ** 2 + (ball2.y - event.y) ** 2 <= ball2.r ** 2:
        ball2.n += 50  # считает очки при попадании в конкретный шар
        points += 50
    else:
        points = 0
    print(points)


def main():
    global canvas, root, ball1, ball2

    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.bind('<Button-1>', canvas_click_chek)
    ball1 = Ball()
    ball2 = Ball()
    movement()
    deleteall()
    blink()

    root.mainloop()


if __name__ == '__main__':
    main()
