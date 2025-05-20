import turtle as t
import random
import time

def right():
    if player.xcor() < 200:
         player.forward(10)

def left():
    if player.xcor() > -200:
        player.backward(10)
        
#화면
t.bgcolor("sky blue")
t.setup(500, 700)

t.bgpic("./화질/sea.png")  # 경로 수정

#변수
player_speed = 5
score = 0
game_over = False

#플레이어 패들
player = t.Turtle()
player.shape("square")
player.shapesize(1,6)
player.up()
player.speed(0)
player.goto(0,-270)

#공
ball = t.Turtle()
ball.shape("turtle")
ball.left(90)
ball.shapesize(1.5)
ball.up()
ball.speed(1)
ball.color("greenyellow")

#키패드 작동
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")
t.listen()

game_on = True
life = 5
t.up()
t.ht()
t.goto(0,300)

#레벨 표시
t.up()
t.ht()
t.goto(0,300)
count = 0
lv = 13

draw = t.Turtle()
draw.up()
draw.speed(0)
draw.ht()
draw.goto(0,250)

#생명&점수표시
t.up()
t.ht()
t.goto(0,300)
t.write(f"Life : {life} ", False, "center", ("",20))
t.up()
t.ht()
t.goto(0,200)
t.write(f" score : {score} ", False, "center", ("",20))

ball_xspeed = 5
ball_yspeed = 5

#공 움직이기
while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        ball_yspeed *= -1

    if ball.ycor() < -340:
        life -= 1
        t.clear()
        t.write(f"Life : {life}", False, "center", ("",20))
        time.sleep(0.5)
        ball.goto(0,100)
        ball_yspeed *= -1
        ball_xspeed *= -1

        if life == 0:
            game_on = False
            t.goto(0,0)
            t.write("Game Over", False, "center", ("",20))

    if count > 50 and lv == 1:
        lv = 2
        if ball_xspeed == -2:
            ball_xspeed = -3
        elif ball_xspeed == 2:
            ball_xspeed = 3
        if ball_yspeed == -2:
            ball_yspeed = -3
        elif ball_yspeed == 2:
            ball_yspeed = 3

    if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1
        score += 1
        t.clear()
        t.write(f" Score : {score} ", False, "center", ("",20))

        if score == 1:
            ball_xspeed += 0.5
            ball_yspeed += 0.5
            t.write(f"                           Lv 1   ", False, "center", ("", 20))
            player_speed += 0.5
            t.bgpic("./화질/sea.png")

        if score == 3:
            ball_xspeed += 0.5
            ball_yspeed += 0.5
            t.write(f"                           Lv 2  ", False, "center", ("", 20))
            player_speed += 0.5
            t.bgpic("./화질/ground.png")
            ball.color("teal")
            player.shapesize(1,5)

        if score == 5:
            ball_xspeed += 0.5
            ball_yspeed += 0.5
            t.write(f"                           Lv 3  ", False, "center", ("", 20))
            player_speed += 0.5
            t.bgpic("./화질/mountain.png")
            player.color("lightgrey")
            ball.color("limegreen")
            player.shapesize(1,4)

        if score == 7:
            ball_xspeed += 0.5
            ball_yspeed += 0.5
            t.write(f"                           Lv 4 ", False, "center", ("", 20))
            player_speed += 0.5
            t.bgpic("./화질/sky.png")
            player.color("dimgray")
            ball.color("darkgreen")
            player.shapesize(1,3)

        if score == 9:
            ball_xspeed += 0.5
            ball_yspeed += 0.5
            t.color("white")
            t.write(f"                           Lv 5  ", False, "center", ("", 20))
            player_speed += 0.5
            t.bgpic("./화질/space.png")
            player.color("lightgrey")
            ball.color("limegreen")
            player.shapesize(1,2)
