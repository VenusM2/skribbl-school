import turtle

# setting players and screen
screen = turtle.Screen()
player = turtle.Turtle()
player.speed(0)
# setting clear button
clearbtn = turtle.Turtle()
clearbtn.speed(0)
clearbtn.penup()
clearbtn.shape("square")
clearbtn.goto(0,-300)


#הגדרת 4 ריבועים TURTLE ל4 צבעים
G = turtle.Turtle()
G.speed(0)
G.shape("turtle")
G.color("green")
G.shapesize(2)
G.penup()
G.goto(-240,-240)


R = turtle.Turtle()
R.speed(0)
R.shape("turtle")
R.color("red")
R.shapesize(2)
R.penup()
R.goto(-80,-240)


Y = turtle.Turtle()
Y.speed(0)
Y.shape("turtle")
Y.color("yellow")
Y.shapesize(2)
Y.penup()
Y.goto(80,-240)

B = turtle.Turtle()
B.speed(0)
B.shape("turtle")
B.color("blue")
B.shapesize(2)
B.penup()
B.goto(240,-240 )

psize2 = turtle.Turtle()
psize5 = turtle.Turtle()
psize10 = turtle.Turtle()
psize2.speed(0)
psize5.speed(0)
psize2.speed(0)


# setting shape for color buttons
psize2.shape("square")
psize5.shape("square")
psize10.shape("square")
player.shape("circle")
player.shapesize(1)

# setting pen up for buttons
psize2.penup()
psize5.penup()
psize10.penup()


# setting colors


# methods for color buttons
def TAL(x,y):
    if -252 < x < -222  and -224 > y > -252:
        player.pencolor('green')
        print("1")
    elif -91 < x < -63 and -224 > y > -252:
        player.pencolor('red')
        print("2")
    elif 71 < x < 96 and -224 > y > -252:
        player.pencolor('yellow')
        print("3")
    elif 229 < x < 258 and -224 > y > -252:
        player.pencolor('blue')
        print("4")

def goto(x, y):
    player.ondrag(None)
    player.goto(x, y)
    player.ondrag(goto)
def pensize2(x,y):
    player.pensize(2)
def pensize5(x,y):
    player.pensize(5)
def pensize10(x,y):
    player.pensize(10)
def teleportto(x,y):
    player.penup()
    player.goto(x,y)
    player.pendown()
def clearpaint(x,y):
    player.clear()
def painter():
    # buttons location
    psize2.goto(-200, -300)
    psize5.goto(-250, -300)
    psize10.goto(-300, -300)

    # basic UI setup
    clearbtn.write("clear" , align='center', move=True)
    psize2.write("2" , align='center', move=True)
    psize5.write("5" , align='center', move=True)
    psize10.write("10" , align='center', move=True)

    # going a bit below the text so the text can be shown
    clearbtn.goto(0,-310)
    psize2.goto(-200, -315)
    psize5.goto(-250, -315)
    psize10.goto(-300, -315)


    # on click methods
    clearbtn.onclick(clearpaint, btn=3)
    screen.onclick(TAL, btn=3)
    psize2.onclick(pensize2, btn=3)
    psize5.onclick(pensize5, btn=3)
    psize10.onclick(pensize10, btn=3)
    screen.onclick(teleportto)
    player.ondrag(goto)


painter()

turtle.mainloop()
