#Norma
#http4_6.py

import turtle as t


def draw_full(Alex, l, n, c2):
    for count in range(n):
        Alex.forward(l)
        Alex.left(360/n)
    Alex.fillcolor(c2)


def main():
    scr = t.Screen()
    Alex = t.Turtle()
    Alex.pensize(3)
    Alex.speed(0)

    n = int(input("Number of sides: "))
    l = int(input("Length of side: "))
    c = str(input("Enter global_max color: "))
    c2 = str(input("Another color: "))
    Alex.color(c)
    Alex.begin_fill()
    Alex.pendown()
    draw_full(Alex, l, n, c2)
    Alex.end_fill()
    scr.exitonclick()


main()