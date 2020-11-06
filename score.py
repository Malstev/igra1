import tkinter as tk

def points(event):
    return print(event.x, event.y)

def canvas_click_chek(event):
    canv = tk.Canvas(canvas, bg='green')
    canv.place(x=(event.x-50), y=(event.y-50), width=100, height=30)


def main():
    global canvas
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.bind('<Button-1>', canvas_click_chek)

    root.mainloop()


if __name__ == '__main__':
    main()
