import turtle
import winsound

window = turtle.Screen()
window.title("Pong by Henrique!")
window.bgcolor("black")
window.setup(width=1920, height=1080)
window.tracer(0)

#resultado
score_a = 0
score_b = 0

#PaddleA

barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=6, stretch_len=1)
barra_a.penup()
barra_a.goto(-700,0)


#PaddleB
barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=6, stretch_len=1)
barra_b.penup()
barra_b.goto(700,0)

#Bola

Bola = turtle.Turtle()
Bola.speed(0)
Bola.shape("square")
Bola.color("white")
Bola.penup()
Bola.goto(0,0)
Bola.dx = 0.2
Bola.dy = 0.2

#Bola2

Bola2 = turtle.Turtle()
Bola2.speed(0)
Bola2.shape("square")
Bola2.color("red")
Bola2.penup()
Bola2.goto(0,0)
Bola2.dx = -0.2
Bola2.dy = 0.2

#Texto de Score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 450)
pen.write("Jogador 1: 0  Jogador 2: 0", align="center", font=("Courier", 24, "normal"))

#funções de movimento

def barra_a_cima():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barra_a_baixo():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)

def barra_b_cima():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barra_b_baixo():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)




window.listen()
window.onkeypress(barra_a_cima, "w")
window.onkeypress(barra_a_baixo, "s")
window.onkeypress(barra_b_cima, "Up")
window.onkeypress(barra_b_baixo, "Down")



#loop Main

while True:
    window.update()

    #movimento da bola 1
    Bola.setx(Bola.xcor() + Bola.dx)
    Bola.sety(Bola.ycor() + Bola.dy)

    #movimento da bola 2
    Bola2.setx(Bola2.xcor() + Bola2.dx)
    Bola2.sety(Bola2.ycor() + Bola2.dy)


    #movimento da bola 1
    if Bola.ycor() > 500:
        Bola.sety(500)
        Bola.dy *= -1
        winsound.PlaySound("BABABOOEY.wav", winsound.SND_ASYNC)

    if Bola.ycor() < -500:
        Bola.sety(-500)
        Bola.dy *= -1
        winsound.PlaySound("BABABOOEY.wav", winsound.SND_ASYNC)

    if Bola.xcor() > 920:
        Bola.goto(0,0)
        Bola.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Jogador 1: {}  Jogador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if Bola.xcor() < -920:
        Bola.goto(0,0)
        Bola.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jogador 1: {}  Jogador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #movimento da bola 2
    if Bola2.ycor() > 500:
        Bola2.sety(500)
        Bola2.dy *= -1
        winsound.PlaySound("Social credit siren.wav", winsound.SND_ASYNC)

    if Bola2.ycor() < -500:
        Bola2.sety(-500)
        Bola2.dy *= -1
        winsound.PlaySound("Social credit siren.wav", winsound.SND_ASYNC)

    if Bola2.xcor() > 920:
        Bola2.goto(0,0)
        Bola2.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Jogador 1: {}  Jogador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if Bola2.xcor() < -920:
        Bola2.goto(0,0)
        Bola2.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jogador 1: {}  Jogador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    

    #bola bate na barra
    if (Bola.xcor() > 670 and Bola.xcor() < 700) and (Bola.ycor() < barra_b.ycor() + 40 and Bola.ycor() > barra_b.ycor() - 40):
        Bola.setx(500)
        Bola.dx *=-1
        winsound.PlaySound("BABABOOEY.wav", winsound.SND_ASYNC)

    if (Bola.xcor() < -670 and Bola.xcor() > -700) and (Bola.ycor() < barra_a.ycor() + 40 and Bola.ycor() > barra_a.ycor() - 40):
        Bola.setx(-500)
        Bola.dx *=-1
        winsound.PlaySound("BABABOOEY.wav", winsound.SND_ASYNC)

    if (Bola2.xcor() > 670 and Bola2.xcor() < 700) and (Bola2.ycor() < barra_b.ycor() + 40 and Bola2.ycor() > barra_b.ycor() - 40):
        Bola2.setx(500)
        Bola2.dx *=-1
        winsound.PlaySound("BABABOOEY.wav", winsound.SND_ASYNC)

    if (Bola2.xcor() < -670 and Bola2.xcor() > -700) and (Bola2.ycor() < barra_a.ycor() + 40 and Bola2.ycor() > barra_a.ycor() - 40):
        Bola2.setx(-500)
        Bola2.dx *=-1
        winsound.PlaySound("BABABOOEY.wav", winsound.SND_ASYNC)








    #BOT

    if barra_b.ycor() < Bola.ycor() and abs(barra_b.ycor() - Bola.ycor()) > 10:
        barra_b_cima()
    elif barra_b.ycor() > Bola.ycor() and abs(barra_b.ycor() - Bola.ycor()) > 10:
        barra_b_baixo()

    if barra_b.ycor() < Bola2.ycor() and abs(barra_b.ycor() - Bola2.ycor()) > 10:
        barra_b_cima()
    elif barra_b.ycor() > Bola2.ycor() and abs(barra_b.ycor() - Bola2.ycor()) > 10:
        barra_b_baixo()
     
