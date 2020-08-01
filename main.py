import tkinter as tk
from random import randint as rnd, choice
import time


class Ball:
    def __init__(self):
        canvas.delete(tk.ALL)  # удаляет все фигуры с холста
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

    def score(self):  # считает очки при попадании в конкретный шар
        self.n += 50

    def show(self):  # двигает шар со скоростью дх ду
        canvas.move(self.ball_id, self.dx, self.dy)

    def move(self):  # отражает шар от стенок
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > 800 or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > 600 or self.y - self.r <= 0:
            self.dy = -self.dy


def blink():  # вводит новый шар в игру
    ball.__init__()
    root.after(2000, blink)


def movement():  # перемещает шар по полю
    ball.show()
    ball.move()
    root.after(30, movement)


def canvas_click_chek(event):
    if (ball.x - event.x) ** 2 + (ball.y - event.y) ** 2 <= ball.r ** 2:
        ball.score()  # считает очки при попадании в конкретный шар
        print('У вас', ball.n, 'очков!')
    else:
        print('Мимо!')


def main():
    global canvas, root, ball

    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.bind('<Button-1>', canvas_click_chek)
    ball = Ball()
    blink()
    movement()

    root.mainloop()


if __name__ == '__main__':
    main()
