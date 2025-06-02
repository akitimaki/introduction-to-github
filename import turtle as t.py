import turtle as t
import colorsys

t.bgcolor('black')
t.speed("fasttest")
t.tracer(100)
t.pencolor("darkviolet")
hue = 0.7
t.hideturtle()

def func():
    global hue
    for a in range(4):
        global hue
        for a in range(4):
            color =colorsys.hsv_to_rgb(hue,1,1)
            hue =+ 0.01
            t.fillcolor(color)
            t.begin_fill()
            t.fd(100)
            t.rigth(18)
            t.fd(100)
            t.end_fill()


for a in range(100):
    func()
    t.goto(8,8)
    t.rt(188)

    t.exitonclick()
            