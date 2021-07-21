import math

from components import *


def move_to(deftur, pos):
    deftur.penup()
    deftur.goto(pos)
    deftur.pendown()


def headTo(pos1, pos2):
    width = pos2[0] -pos1[0]
    heith = pos2[1] -pos1[1]
    if width != 0 or heith != 0:
        ctan = math.atan(abs(heith)/abs(width))
        angle = math.degrees(ctan)

        if pos2[0] > 0 and pos2[1] >0:
            angle = angle

        elif pos2[0] <0 and pos2[1] >0:
            angle = 180 - angle

        elif pos2[0] <0 and pos2[1] < 0:
            angle = 180 + angle

        elif pos2[0] > 0 and pos2[1] < 0:
            angle = 360 - angle

        return angle


def draw_leaves(petiole_lenth, ppensize, petpoistion):
    main_petiole = tur.Turtle()
    main_petiole.hideturtle()
    main_petiole.pensize(ppensize)
    petheading = random.randint(0, 360)
    move_to(main_petiole, petpoistion)
    main_petiole.setheading(petheading)

    main_petiole.forward(-petiole_lenth)
    side_pos = main_petiole.pos()

    sizes = [(142, 0.3), (180, 1), (172, 0.8), (158, 0.45)] #index0 表示偏转角度，index1表示开始走的距离
    size = random.choice(sizes)

    # deltaAngle = random.randint(-20, 20)
    startangle = random.randint(0, 360)
    t1 = tur.Turtle()
    t1.hideturtle()
    tur.tracer(0)
    move_to(t1, side_pos)
    t1.color(0, 205, 0) #需要修改为RGB的
    t1.setheading(startangle)
    t1.speed(0)
    t2 = t1.clone()
    t2.right(size[0])

    t1.begin_fill()
    t2.begin_fill()
    stepl = size[1]
    for i in range(50):
        if i > 30:
            stepl += 0.1
        t1.forward(stepl)
        t2.forward(stepl)
        t1.left(3)
        t2.right(3)
    t1.end_fill()
    t2.end_fill()
    tailpos = t1.pos()
    tur.tracer(1)

    # main_petiole.setheading(deltaAngle)
    # main_petiole.pencolor('black')
    # sub1_main = main_petiole.clone()
    # sub2_main = main_petiole.clone()

    # for line in range(4):     #画叶子里的纹理
    #     main_pos = main_petiole.pos()
    #     # m_heading = main_petiole.heading()
    #     m_heading = headTo(tailpos, main_pos)
    #     main_petiole.setheading(m_heading)  # 设置纹理角度
    #     main_petiole.forward(-size[1]*5)
    #     ppensize -= 2
    #     if ppensize > 0:
    #         sub1_main.pensize(ppensize)
    #         sub2_main.pensize(ppensize)
    #         sub1_main.setheading(m_heading-135)
    #         sub2_main.setheading(m_heading+135)
    #         move_to(sub1_main, main_pos)
    #         move_to(sub2_main, main_pos)
    #         sub2_main.forward(size[1]*5)
    #         sub1_main.forward(size[1]*5)
    #
    #         main_petiole.pensize(ppensize)
    #         main_petiole.forward(-size[1]*10)


def rattan():
    rat_left = tur.Turtle()
    rat_left.color('Green')
    rat_left.hideturtle()
    rat_left.speed(0)

    screen = rat_left.getscreen()
    screen.clear()
    screen.colormode(255) #设置为RGB 255模式
    mainx, mainy = screen.window_width(), screen.window_height()
    screen.bgcolor(135, 206, 235)

    move_to(rat_left, (-mainx/2+30, -mainy/2+20))
    rat_left.setheading(90)
    rat_left.pensize(7) #藤粗细
    rat_left.forward(10)

    rat_right = rat_left.clone()
    rat_left.setheading(0)
    move_to(rat_right, (mainx/2-40, -mainy/2+20))
    rat_right.forward(10)
    rat_right.setheading(180)

    turn = False
    while not turn:
        rat_x = rat_left.xcor()
        rat_y = rat_left.ycor()
        # print(rat_x, rat_y)
        rat_r = random.randint(30, 60)

        if rat_y + rat_r*2 < mainy/2-30:
            rat_left.circle(rat_r, 80)
            draw_leaves(10, 3, rat_left.pos())
            rat_left.circle(rat_r, 100)
            draw_leaves(10, 3, rat_left.pos())
            rat_left.circle(-rat_r, 180)
            draw_leaves(10, 3, rat_left.pos())

        elif rat_x + rat_r*2 < mainx/2:
            rat_left.setheading(270)
            rat_left.circle(rat_r, 90)
            draw_leaves(10, 3, rat_left.pos())
            rat_left.circle(rat_r, 90)
            draw_leaves(10, 3, rat_left.pos())
            rat_left.circle(-rat_r, 90)
            draw_leaves(10, 3, rat_left.pos())
            rat_left.circle(-rat_r, 90)
            draw_leaves(10, 3, rat_left.pos())

        else:
            turn = True

    turnr = False
    while not turnr:
        rat_rx = rat_right.xcor()
        rat_ry = rat_right.ycor()
        # print(rat_x, rat_y)
        rat_r = random.randint(30, 60)

        if rat_ry + rat_r*2 < mainy/2:
            rat_right.circle(-rat_r, 90)
            draw_leaves(10, 3, rat_right.pos())
            rat_right.circle(-rat_r, 90)
            draw_leaves(10, 3, rat_right.pos())
            rat_right.circle(rat_r, 180)
            draw_leaves(10, 3, rat_right.pos())

        elif rat_rx -rat_r*2 > -mainx/2:
            rat_right.setheading(270)
            rat_right.circle(-rat_r, 90)
            draw_leaves(10, 3, rat_right.pos())
            rat_right.circle(-rat_r, 90)
            draw_leaves(10, 3, rat_right.pos())
            rat_right.circle(rat_r, 80)
            draw_leaves(10, 3, rat_right.pos())
            rat_right.circle(rat_r, 100)
            draw_leaves(10, 3, rat_right.pos())

        else:
            turnr = True


if __name__ == '__main__':
    # draw_leaves(10, 3)
    rattan()

    tur.done()
