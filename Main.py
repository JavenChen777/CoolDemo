import time

from Countdown import *
from sakura import *
from vine import *
from lines import *
from birthcake import *


if __name__ == '__main__':
    countDown()
    time.sleep(1)
    sakura()
    print("sakura end")
    time.sleep(3)
    line_comb()
    R = 100
    windmill(R)
    time.sleep(1)
    rattan()

    main_cake() #画蛋糕
    poss = [(0, 90), (-60, 90), (60, 90), (-30, 150), (30, 150), (-30, 30), (30, 30)]
    for pos in poss:
        candle(pos, 60, 0.1)

    time.sleep(2)
    write_font((-200, -300))

    tur.done()