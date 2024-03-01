from turtle import Turtle, Screen

wn = Screen()
wn.setup(500, 500)
wn.bgcolor('black')

player = Turtle(visible=False)
player.speed('fastest')
player.shapesize(2)
player.color('white')
player.penup()
player.setposition(200, -200)
player.showturtle()

enemy = Turtle('circle', visible=False)
enemy.shapesize(5)
enemy.color('red')
enemy.penup()
enemy.setposition(-200, 200)
enemy.showturtle()

def click_handler(x, y):
    wn.onclick(None)  # disable handler while in handler
    player.setheading(player.towards(x, y))  # head towards new location
    player.setposition(x, y)

    if player.distance(enemy) < 10:
        player.hideturtle()  # teleport
        player.setposition(200, -200)
        player.showturtle()

    wn.onclick(click_handler)

wn.onclick(click_handler)

wn.mainloop()