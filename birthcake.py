import turtle

from components import *


def draw_ellips(tt, radius, full, step): #full should be 2 or 1
    # tt.setheading(270)
    for j in range(full):
        for i in range(60):
            if i < 30:
                radius += step
            else:
                radius -= step
            tt.forward(radius)
            tt.left(3)


def candle(pos, high, widr):
    c1 = tur.Turtle()
    c1.color('grey', 'pink')
    tur.tracer(0)
    c1.penup()
    c1.goto(pos)
    c1.pendown()

    c1.begin_fill()
    c1.setheading(90)
    c1.forward(high)
    c1.setheading(270)

    draw_ellips(c1, widr, 2, 0.01)
    c1.forward(high)

    draw_ellips(c1, widr, 1, 0.01)
    c1.forward(high)

    c1.penup()
    c1.left(90)
    c1.forward(widr*50)
    c1.pendown()
    c1.setheading(90)
    c1.pensize(3)
    c1.forward(widr*60)

    c1.hideturtle()
    c1.end_fill()
    tur.tracer(1)


def main_cake():
    cake = turtle.Turtle()
    cake.hideturtle()
    cake.speed(10)
    cake.penup()
    cake.goto(-200, 0)
    cake.pendown()
    cake.setheading(270)

    cake.color('wheat')
    cake.begin_fill()
    draw_ellips(cake, 3, 2, 0.4)
    cake.end_fill()

    cake.penup()
    cake.goto(-150, 0)
    cake.pendown()
    cake.color('grey', 'orange')
    cake.setheading(270)
    cake.begin_fill()
    draw_ellips(cake, 3, 2, 0.25)
    cake.end_fill()

    cake.begin_fill()
    cake.setheading(90)
    cake.forward(100)
    cake.right(180)
    draw_ellips(cake, 3, 2, 0.25)
    draw_ellips(cake, 3, 1, 0.25)
    cake.setheading(270)
    cake.forward(100)
    cake.end_fill()


def write_font(pos):
    wt = tur.Turtle()
    wt.penup()
    wt.goto(pos)
    wt.pendown()
    wt.write('Happy Birthday', font=('bold', 50, 'normal'))
    wt.hideturtle()


if __name__ == '__main__':
    # candle((10,100), 60, 0.1)
    main_cake()

    poss = [(0, 90), (-60, 90), (60, 90), (-30, 150), (30, 150), (-30, 30), (30, 30)]
    for pos in poss:
        candle(pos, 60, 0.1)

    write_font((-200, -300))

    tur.done()