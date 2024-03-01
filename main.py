from turtle import Screen, Turtle
from random import randint



def change_position():
    catch_turtle.hideturtle()
    x = randint(-300, 300)
    y = randint(-300, 300)
    catch_turtle.goto(x, y)
    catch_turtle.showturtle()

score = 0

def update_score():
    global score

    score += 1
    score_keeper.clear()
    score_keeper.write(score, align='center')

def update_time():
    time_keeper.undo()
    time_keeper.write(seconds, align='center')

def target_clicked(x, y):
    if seconds > 0:
        update_score()
        change_position()

def action():
    global seconds

    seconds -= 1

    if seconds <= 0:
        catch_turtle.hideturtle()

        time_keeper.clear()
        time_keeper.sety(320)
        time_keeper.write("Time Over", align='center')
    else:
        update_time()
        turtle_screen.ontimer(action, 1000)

turtle_screen = Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")


catch_turtle = Turtle()
catch_turtle.penup()
catch_turtle.setposition(randint(-300, 300), randint(-300, 300))
catch_turtle.shape('turtle')


score_keeper = Turtle()
score_keeper.hideturtle()
score_keeper.penup()

seconds = int(turtle_screen.numinput("Timer", "Enter the seconds", minval=0, maxval=59))

time_keeper = score_keeper.clone()

time_keeper.sety(370)
time_keeper.write("Time Left:", align='center')
time_keeper.sety(300)
time_keeper.write(seconds, align='center')

catch_turtle.onclick(target_clicked)

action()

turtle_screen.mainloop()