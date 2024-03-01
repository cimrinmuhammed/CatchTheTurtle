#Catch the turtle
import turtle
import math
import random

score = 0
print ("\n" * 40)
print("Your score is:\n0")

#Title
t=turtle.Pen()
t.pencolor("Blue")
t.hideturtle()
t.penup()
t.setposition(-70,350)
t.write("Catch the turtle", font=("Verdana", 18))

#Tip
text=turtle.Pen()
t.pencolor("Red")
t.hideturtle()
t.penup()
t.setposition(-70, -350)
t.write("DON'T TOUCH THE EDGES!", font=("Verdana", 18))



#Set up screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Catch the Turtle")

#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(10)
mypen.hideturtle()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.color("yellow")
    mypen.forward(300)
    mypen.color("black")
    mypen.forward(300)
    mypen.left(90)
mypen.hideturtle()


#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.penup()
player.speed(0)

#Create goal
goal = turtle.Turtle()
goal.color("red")
goal.shape("turtle")
goal.penup()
goal.speed(0)
goal.setposition(-100, -100)

#Set speed
speed = 1

#Define functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed +=0.5

def decreasespeed():
    global speed
    speed -= 1

#Set keyboard binding
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")



while True:
    player.forward(speed)

    #Boundary check
    if player.xcor() > 300 or player.xcor() < -300:
        print("GAME OVER")
        quit()

    if player.ycor() > 300 or player.ycor() < -300:
        print("Game OVER")
        quit()

    #Collision checking
    d= math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))
    if d < 20 :
        goal.setposition(random.randint(-300,300), random.randint(-300, 300))
        score = score + 1
        print ("\n" * 40)
        print("Your score is")
        print (score)