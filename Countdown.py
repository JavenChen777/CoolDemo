from components import *

def countDown():
    screen = tur.Screen()
    cd = tur.Turtle()
    cd.hideturtle()
    cd.pencolor('white')
    # size = screen.screensize()
    # print(size)
    font_size = 172
    font = 3
    while font > 0:
        # screen.reset()
        screen.clear()
        screen.bgcolor('black')
        cd.penup()
        cd.goto(-70, -(font_size/2))
        cd.pendown()
        cd.write(str(font), font=('Black', font_size, 'bold'))
        font -= 1
        time.sleep(1)


if __name__ == '__main__':
    countDown()
    tur.done()