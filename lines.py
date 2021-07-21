import time

from components import *


def line_comb():
    l_screen = tur.Screen()
    l_screen.clear()

    line_t = tur.Turtle()
    line_t.hideturtle()

    # tur.tracer(False)
    line_t.forward(100)
    # tur.tracer(1)
    line_t.left(90)
    line_t.forward(200)

    line_t.speed(11)
    line_t.goto(0, 0)
    colors = ['purple', 'green', 'red', 'blue', 'khaki', 'black', 'pink', 'indigo', 'gray', 'brown']
    # step = 3
    # for n in range(100):
    #     t1.forward(step)
    # sleep(0.1)
    line_t.pensize(3)
    for c in colors:
        # t1.goto(0, 0)
        line_t.pencolor(c)
        line_t.right(55)
        for i in range(10, 40):
            line_t.forward(2 + 2 * i)
            line_t.left(75)

    time.sleep(5)


def windmill(r): #R表示 风车半径
    w_screen = tur.Screen()
    w_screen.clear()
    # w_screen.bgcolor('light blue')

    w_tur = tur.Turtle()
    # w_tur.hideturtle()
    colors = [['orange', 'yellow'], ['red', 'pink'], ['green', 'light green'], ['indigo', 'blue']]
    angle = 0
    for i in range(300):
        w_screen.clear()
        # w_screen.bgcolor('light blue')
        w_tur.setheading(angle)
        angle -= 4
        tur.tracer(False)
        for color in colors:
            w_tur.speed(0)
            #内三角
            w_tur.color(color[0])
            w_tur.begin_fill()
            w_tur.forward(r)
            w_tur.left(90)
            w_tur.forward(r)
            w_tur.left(135)
            w_tur.goto(0, 0)
            w_tur.end_fill()

            #外三角
            side = sqrt(pow(r, 2) * 2)
            w_tur.color(color[1])
            w_tur.right(180)
            w_tur.begin_fill()
            w_tur.forward(side)
            w_tur.left(90)
            w_tur.forward(side)
            w_tur.goto(0, 0)
            w_tur.end_fill()
            w_tur.right(45)
        tur.tracer(True)
        time.sleep(0.041)


if __name__ == '__main__':
    line_comb()
    R = 100
    windmill(R)
    tur.done()