from tkinter import W
import turtle as t

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("PongGame")
window.bgcolor("#91823A")
window.setup(width = 800, height = 600)
window.tracer(0)

#создание левого игрока
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("#D7EEF4")
leftpaddle.shapesize(stretch_wid=4.4, stretch_len=0.5)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#создание правого игрока
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("#D7EEF4")
rightpaddle.shapesize(stretch_wid=4.4, stretch_len=0.5)
rightpaddle.penup()
rightpaddle.goto(350,0)

#создание мяча
ball = t.Turtle()
ball.speed(2)
ball.shape("circle")
ball.color("#F0AD0D")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.15
ballydirection = 0.15

#создание счета
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align = "center", font = ('Arial',24,'normal'))

#движение легого игрока
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y = y-90
    leftpaddle.sety(y)    

#движение правого игрока
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y = y-90
    rightpaddle.sety(y)    

#назначение клавиш для игры
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    #движение мяча
    ball.setx(ball.xcor()+ballxdirection)    
    ball.sety(ball.ycor()+ballydirection)

    #параметры границы
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection = ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection = ballydirection*-1    

    if(ball.xcor())>390:
        ball.goto(0,0)
        ballxdirection = ballxdirection
        playerAscore = playerAscore+1
        pen.clear()
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    if(ball.xcor())<-390:
        ball.goto(0,0)
        ballxdirection = ballxdirection*-1
        playerBscore = playerBscore+1
        pen.clear()
        pen.write("player A:{}    player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    #обработка столкновений
    if (ball.xcor()>340)and(ball.xcor()<350)and(
            ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection = ballxdirection*-1

    if (ball.xcor()<-340)and(ball.xcor()>-350)and(
            ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection = ballxdirection*-1