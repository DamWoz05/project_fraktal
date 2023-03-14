from math import sqrt
from math import sqrt as pierw
from random import randint
from turtle import *

import matplotlib.pyplot as plt
import numpy as np


class triangle:
    def __init__(self):
        self.photo = "textures/Triangle.png"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(length / -2, length * sqrt(3) / -4)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def sierpinski_triangle(depth, length):
            if depth == 0:
                turtle.begin_fill()
                for i in range(3):
                    turtle.forward(length)
                    turtle.left(120)
                turtle.end_fill()
            else:
                for i in range(3):
                    sierpinski_triangle(depth - 1, length / 2)
                    turtle.forward(length)
                    turtle.left(120)

        sierpinski_triangle(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 9:
            st = 9
        elif st < 3:
            st = 3
        if length < 250:
            length = 250
        return st, length


class dywan:
    def __init__(self):
        self.photo = "textures/carpeto.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(0, length / -1)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def square(depth, length):
            if depth == 0:
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(length)
                    turtle.left(90)
                turtle.end_fill()
            else:
                for i in range(4):
                    square(depth - 1, length / 3)
                    turtle.forward(length / 3)
                    square(depth - 1, length / 3)
                    turtle.forward(2 * length / 3)
                    turtle.left(90)

        square(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 5:
            st = 5
        elif st < 2:
            st = 2
        if length < 250:
            length = 250
        elif length > 800:
            length = 800
        return st, length


class drzewko:
    def __init__(self):
        self.photo = "textures/drzewko.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.left(90)
        turtle.penup()
        turtle.goto(0, length * sqrt(3) / -3)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def tree(depth, length):
            if depth == 0:
                turtle.dot(10, "blue")
            else:
                turtle.forward(length)
                turtle.right(40)
                tree(depth - 1, length / 2)
                turtle.left(80)
                tree(depth - 1, length / 2)
                turtle.right(40)
                turtle.backward(length)

        tree(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 4:
            st = 4
        if length < 50:
            length = 50
        elif length > 400:
            length = 400
        return st, length


class plateczek:
    def __init__(self):
        self.photo = "textures/plateczek.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(length / -2, length / 3)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def kocha(depth, length):
            if depth == 1:
                turtle.forward(length)
            else:
                kocha(depth - 1, length / 3)
                turtle.left(60)
                kocha(depth - 1, length / 3)
                turtle.right(120)
                kocha(depth - 1, length / 3)
                turtle.left(60)
                kocha(depth - 1, length / 3)

        def platek(st, length):
            turtle.fillcolor("blue")
            turtle.begin_fill()
            for i in range(3):
                kocha(st, length)
                turtle.right(120)
            turtle.end_fill()

        platek(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 3:
            st = 3
        elif st > 9:
            st = 9
        if length < 150:
            length = 150
        elif length > 700:
            length = 700
        return st, length


class kantorek:
    def __init__(self):
        self.photo = "textures/kantorek.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.pencolor("blue")
        turtle.fillcolor("blue")
        turtle.pensize(2)
        x = length / -2

        def cantor(st, length, x=-500, y=200):
            if st > 0:
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.forward(length)
                y -= 50
                cantor(st - 1, length / 3, x, y)
                cantor(st - 1, length / 3, x + length / 3 * 2, y)

        cantor(st, length, x)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 3:
            st = 3
        if length < 250:
            length = 250
        return st, length


class Lewandowski:
    def __init__(self):
        self.photo = "textures/Lewy.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        if st > 10:
            turtle.goto((length / -1) - 200, -300)
        else:
            turtle.goto(length / -1, -300)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def Levy(depth, length):
            if depth == 0:
                turtle.forward(length)
            else:
                turtle.left(45)
                Levy(depth - 1, length)
                turtle.right(90)
                Levy(depth - 1, length)
                turtle.left(45)

        length = length / (st * 2)
        Levy(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st * length > 2000:
            length = 2000 / st
            if st < 8:
                length *= 2
            print(length)
        else:
            if st < 2:
                st = 2
            if length < 200:
                length = 200
        return st, length


class SSM:
    def __init__(self):
        self.photo = "textures/SSM.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def dragoncurve(l, n):
            def x(n):
                if n > 0:
                    x(n - 1)
                    turtle.right(90)
                    y(n - 1)
                    turtle.forward(l)

            def y(n):
                if n > 0:
                    turtle.forward(l)
                    x(n - 1)
                    turtle.left(90)
                    y(n - 1)

            turtle.fd(l)
            x(n)

        dragoncurve(length, st)
        done()

    def check_limit(self, st, length):
        st += 2
        if st < 10:
            st = 10
        length = 18 - st
        return st, length


class krzywy_wiktor:
    def __init__(self):
        self.photo = "textures/romb.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(length / -2, length / 2)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def draw_vicsek(length, depth):
            if depth == 0:
                turtle.forward(length)
                return
            third = length / 3
            draw_vicsek(third, depth - 1)
            turtle.left(90)
            draw_vicsek(third, depth - 1)
            turtle.right(90)
            draw_vicsek(third, depth - 1)
            turtle.right(90)
            draw_vicsek(third, depth - 1)
            turtle.left(90)
            draw_vicsek(third, depth - 1)

        for i in range(4):
            draw_vicsek(length, st)
            turtle.right(90)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 7:
            st = 7
        if length < 300:
            length = 300
        elif length > 500:
            length = 500
        return st, length


class Hilbert:
    def __init__(self):
        self.photo = "textures/hilbus.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        penup()
        turtle.goto(-length / 2.0, length / 2.0)
        pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def hilbert(level, angle, step):
            if level == 0:
                return

            turtle.right(angle)
            hilbert(level - 1, -angle, step)

            turtle.forward(step)
            turtle.left(angle)
            hilbert(level - 1, angle, step)

            turtle.forward(step)
            hilbert(level - 1, angle, step)

            turtle.left(angle)
            turtle.forward(step)
            hilbert(level - 1, -angle, step)
            turtle.right(angle)

        hilbert(st, 90, length / (2 ** st - 1))
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 9:
            st = 9
        if length < 300:
            length = 300
        return st, length


class dmuchawiec:
    def __init__(self):
        self.photo = "textures/dandy.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        penup()
        turtle.goto(0, -350)
        pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def dandelion(n, l):
            if n == 0 or l < 2:
                return
            turtle.forward(l)
            turtle.left(90)
            dandelion(n - 1, l / 2)
            turtle.right(60)
            dandelion(n - 1, l / 2)
            turtle.right(60)
            dandelion(n - 1, l / 2)
            turtle.right(60)
            dandelion(n - 1, l / 2)
            turtle.left(90)
            turtle.backward(l)

        turtle.left(90)
        dandelion(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 12:
            st = 12
        elif st < 3:
            st = 3
        if length < 100:
            length = 100
        elif length > 400:
            length = 400
        return st, length


class paprota:
    def __init__(self):
        self.photo = "textures/paprot.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        penup()
        turtle.goto(0, length * -3.9)
        pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def paprot(n, l):
            if n == 0:
                turtle.dot(5, "green")
                return
            turtle.forward(0.3 * l)
            turtle.left(55)
            paprot(n - 1, l / 2)
            turtle.right(55)
            turtle.forward(0.7 * l)
            turtle.right(40)
            paprot(n - 1, l / 2)
            turtle.left(40)
            turtle.forward(l)
            turtle.left(5)
            paprot(n - 1, 0.8 * l)
            turtle.right(5)
            turtle.right(90)
            turtle.left(90)
            turtle.backward(2 * l)

        turtle.left(90)
        paprot(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 9:
            st = 9
        elif st < 3:
            st = 3
        if length < 50:
            length = 50
        elif length > 115:
            length = 115
        return st, length


class penta:
    def __init__(self):
        self.photo = "textures/penta.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        penup()
        turtle.goto(-400, -300)
        pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def pentaplex(n, l):
            if n == 0:
                return
            for i in range(5):
                pentaplex(n - 1, (l) - (l * 0.309016699437 * 2))
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.right(144)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)
                turtle.forward((l / 2) - (l * 0.309016699437))
                turtle.left(72)

        pentaplex(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 7:
            st = 7
        elif st < 2:
            st = 2
        if length < 250:
            length = 250
        return st, length


class regress:
    def __init__(self):
        self.photo = "textures/regress.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        penup()
        turtle.goto(0, -400)
        pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def Nenio(depth, length):
            if depth > 2:
                for i in range(depth):
                    turtle.left(360 / depth)
                    turtle.forward(length)
                    Nenio(depth - 1, length / 2)

        Nenio(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 9:
            st = 9
        elif st < 4:
            st = 4
        if length > 360:
            length = 360
        elif length < 100:
            length = 100
        return st, length


class kwadrat:
    def __init__(self):
        self.photo = "textures/kwadrat.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        penup()
        turtle.goto(-length / 2, -length / 2)
        pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def square(n, l):
            if n == 0 or l < 2:
                return
            square(n - 1, l / 3)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            square(n - 1, l / 3)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            square(n - 1, l / 3)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            square(n - 1, l / 3)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(2 * (l / 3))
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.left(90)
            turtle.forward(l / 3)
            turtle.right(90)
            square(n - 1, l / 3)
            turtle.right(90)
            turtle.forward(l / 3)
            turtle.right(90)
            turtle.forward(l / 3)
            turtle.right(180)

        square(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 10:
            st = 10
        elif st < 2:
            st = 2
        if length > 800:
            length = 800
        elif length < 100:
            length = 100
        return st, length


class htree:
    def __init__(self):
        self.photo = "textures/htree.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def htree(n, l):
            if n == 0 or l < 2:
                return
            turtle.forward(l / 2)
            turtle.left(90)
            turtle.forward(l / 2)
            turtle.right(90)
            htree(n - 1, l / 2)
            turtle.left(90)
            turtle.left(180)
            turtle.forward(l)
            turtle.right(90)
            htree(n - 1, l / 2)
            turtle.left(90)
            turtle.backward(l / 2)
            turtle.right(90)
            turtle.forward(l)
            turtle.left(90)
            turtle.forward(l / 2)
            turtle.right(90)
            htree(n - 1, l / 2)
            turtle.left(90)
            turtle.left(180)
            turtle.forward(l)
            turtle.right(90)
            htree(n - 1, l / 2)
            turtle.left(90)
            turtle.backward(l / 2)
            turtle.right(90)
            turtle.forward(l / 2)

        htree(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st > 11:
            st = 11
        elif st < 2:
            st = 2
        if length > 500:
            length = 500
        elif length < 100:
            length = 100
        return st, length


class Infinity:
    def __init__(self):
        self.photo = "textures/inf.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(-length / 2, 0)
        turtle.right(90)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def halfCircle(n, l):
            if n == 0 or l < 2:
                return
            halfCircle(n - 1, l / 2)
            turtle.circle(l / 2)
            turtle.left(90)
            turtle.up()
            turtle.forward(l)
            turtle.down()
            turtle.left(90)
            turtle.circle(l / 2)
            turtle.right(90)
            turtle.up()
            turtle.backward(l / 2)
            turtle.down()
            turtle.right(90)
            halfCircle(n - 1, l / 2)
            turtle.left(90)
            turtle.up()
            turtle.backward(l / 2)
            turtle.down()
            turtle.right(90)

        halfCircle(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        if length < 100:
            length = 100
        return st, length


class cross:
    def __init__(self):
        self.photo = "textures/wavy.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        st *= 10
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def circleTunnel(n, l):
            if n == 0:
                return

            circleTunnel(n - 1, l * 0.9)
            turtle.circle(l)

        def circleCross(n, l):
            for i in range(4):
                circleTunnel(n, l)
                turtle.left(90)

        circleCross(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        if length < 100:
            length = 100
        elif length > 300:
            length = 300
        return st, length


class cTriangle:
    def __init__(self):
        self.photo = "textures/cTri.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        turtle.penup()
        turtle.goto(0, -400)
        turtle.pendown()
        bgcolor("black")
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def circleTriangle(n, l):
            if n == 0 or l < 2:
                return
            for i in range(3):
                circleTriangle(n - 1, l / 2.15470053838)
                turtle.circle(l / 2.15470053838)
                turtle.left(60)
                turtle.up()
                turtle.forward(l * 1.73205080757)
                turtle.down()
                turtle.left(60)

            turtle.circle(l)

        circleTriangle(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        elif st > 10:
            st = 10
        if length < 100:
            length = 100
        elif length > 450:
            length = 450
        return st, length


class pyth:
    def __init__(self):
        self.photo = "textures/pytha.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        turtle.penup()
        turtle.goto(0, -300)
        turtle.pendown()
        bgcolor("black")
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def bentTree(n, l):
            if n == 0 or l < 2:
                return
            for i in range(4):
                turtle.forward(l)
                turtle.left(90)
            turtle.left(90)
            turtle.forward(l)
            turtle.right(60)
            bentTree(n - 1, l * 0.86602540378)
            turtle.forward(l * 0.86602540378)
            turtle.right(90)
            bentTree(n - 1, l / 2)
            for i in range(4):
                turtle.forward(l / 2)
                turtle.left(90)
            turtle.left(180)
            for i in range(3):
                turtle.forward(l * 0.86602540378)
                turtle.left(90)
            turtle.right(120)
            turtle.forward(l)
            turtle.left(90)

        bentTree(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        if length < 50:
            length = 50
        elif length > 180:
            length = 180
        return st, length


class sTri:
    def __init__(self):
        self.photo = "textures/sTria.PNG"

    def draw(self, st, length, animation=True, gen_win=None):
        st *= 15
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        turtle.penup()
        turtle.goto(-length / 2, length / 2)
        turtle.pendown()
        bgcolor("black")
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def spiral(n, l):
            if n == 0 or l < 2:
                return
            turtle.forward(l)
            turtle.right(119)
            spiral(n - 1, l * 0.98)

        spiral(st, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        if length < 100:
            length = 100
        return st, length


class chaos:
    def __init__(self):
        self.photo = "textures/Triangle.png"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(-1500, -1500)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def sierpinski_triangle(depth, length):
            a = length
            points = [[0, 0], [a, 0], [a / 2, (a * pierw(3)) / 2]]
            x = y = -1500
            new = randint(0, 2)
            for i in range(depth):
                turtle.penup()
                turtle.goto((x + points[new][0]) / 2, (y + points[new][1]) / 2)
                x, y = (x + points[new][0]) / 2, (y + points[new][1]) / 2
                turtle.pendown()
                turtle.dot(2)
                new = randint(0, 2)

        sierpinski_triangle(st * 1000, length)
        turtle.hideturtle()
        done()

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        if length < 100:
            length = 100
        return st, length


class mandelbrott:
    def __init__(self):
        self.photo = "textures/mandelbrot.png"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()

        def countIterationsUntilDivergent(c, threshold):
            z = complex(0, 0)
            for iteration in range(threshold):
                z = (z * z) + c

                if abs(z) > 4:
                    break
                    pass
                pass
            return iteration

        def mandelbrot(threshold, d):
            realAxis = np.linspace(-0.22, -0.219, d)
            imaginaryAxis = np.linspace(-0.70, -0.699, d)
            realAxisLen = len(realAxis)
            imaginaryAxisLen = len(imaginaryAxis)
            atlas = np.empty((realAxisLen, imaginaryAxisLen))

            for ix in range(realAxisLen):
                for iy in range(imaginaryAxisLen):
                    cx = realAxis[ix]
                    cy = imaginaryAxis[iy]
                    c = complex(cx, cy)

                    atlas[ix, iy] = countIterationsUntilDivergent(c, threshold)
                    pass
                pass

            plt.imshow(atlas.T, interpolation="nearest")
            plt.show()

        mandelbrot(st * 50, length * 10)

    def check_limit(self, st, length):
        if st < 2:
            st = 2
        if st > 10:
            st = 10
        if length < 100:
            length = 100
        if length > 150:
            length = 150
        return st, length


class Nenio:
    def __init__(self):
        self.photo = "textures/Nenio.png"

    def draw(self, st, length, animation=True, gen_win=None):
        gen_win.destroy()
        colors = {
            0: "purple",
            1: "dark blue",
            2: "blue",
            3: "lime",
            4: "yellow",
            5: "orange",
            6: "red"
        }

        class mem:
            def __init__(self):
                self.c = 0
                self.step = 0

        mem = mem()
        turtle = Turtle()
        if animation == "True":
            turtle.speed(0)
        else:
            turtle._tracer(0)
        bgcolor("black")
        turtle.penup()
        turtle.goto(-1500, -1500)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")

        def Nenio(depth, length, block=4):
            if block > 0:
                for i in range(depth):
                    turtle.left(360 / depth)
                    turtle.forward(length)
                    Nenio(depth - 1, length / 2, block - 1)
                if depth > 25:
                    if mem.c > 6:
                        mem.c = 0
                    turtle.pencolor(colors[mem.c])
                    mem.c += 1
                if block == 3:
                    mem.step += 1
                    print(mem.step, "/ 30")

        turtle.penup()
        turtle.pencolor("purple")
        turtle.goto(0, -300)
        turtle.pendown()
        depth = 30
        Nenio(depth, 2500 // depth)
        done()


Fractals = {
    1: triangle(),
    2: dywan(),
    3: drzewko(),
    4: plateczek(),
    5: kantorek(),
    6: Lewandowski(),
    7: SSM(),
    8: krzywy_wiktor(),
    9: Hilbert(),
    10: dmuchawiec(),
    11: paprota(),
    12: penta(),
    13: regress(),
    14: kwadrat(),
    15: htree(),
    16: Infinity(),
    17: cross(),
    18: cTriangle(),
    19: pyth(),
    20: sTri(),
    22: chaos(),
    23: mandelbrott(),
    24: Nenio()
}
