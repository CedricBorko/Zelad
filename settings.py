WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64



# Level surrounded with x's and dots in the middle
__LEVEL = [['x' if (i in (0, 19) or j in (0,29)) else '.' for i in range(20)] for j in range(30)]

# 46 x 30
LEVEL = (
    [
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "x...........................w..............x",
        "x...........................ww.............x",
        "x............................w.............x",
        "x...........................ww.............x",
        "x...........................b..............x",
        "x...........................ww.............x",
        "x..w.........................www...........x",
        "x.ww...........................w...........x",
        "x.www..........................w...........x",
        "x.www..........................w...........x",
        "x.www..........................www.........x",
        "x.wwww...........................ww........x",
        "x.wwww............................w........x",
        "x...ww.........................wwww........x",
        "x...w..........................w...........x",
        "x.............................www..........x",
        "x...........................wwwww..........x",
        "x...........................wwwww..........x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "x..........................................x",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ],
    (5, 5)
)

# for x in __LEVEL:
#     print(x)