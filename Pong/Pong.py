#beginner pong using python
import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("pong by LunchBox")
wn.bgcolor("black");
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#paddle Player1
paddle_a = turtle.Turtle()
paddle_a.speed(0);
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle PLayer2
paddle_b = turtle.Turtle()
paddle_b.speed(0);
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0);
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Key state tracking
keys = {"w": False, "s": False, "Up": False, "Down": False}

def key_press(key):
    keys[key] = True
def key_release(key):
    keys[key] = False

#Keyboard Binding
wn.listen()
for k in keys:
    wn.onkeypress(lambda key=k: key_press(key), k)
    wn.onkeyrelease(lambda key=k: key_release(key), k)

#main game loop
while True:
    wn.update()
    time.sleep(0.01)

    # Move paddles
    if keys["w"] and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 20)
    if keys["s"] and paddle_a.ycor() > -250:
        paddle_a.sety(paddle_a.ycor() - 20)
    if keys["Up"] and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 20)
    if keys["Down"] and paddle_b.ycor() > -250:
        paddle_b.sety(paddle_b.ycor() - 20)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)