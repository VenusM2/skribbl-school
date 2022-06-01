from cmath import pi
from itertools import count
import turtle
import random

answer = ""
randomword = turtle.Turtle()
text = turtle.Turtle()
chatBtn = turtle.Turtle()
screen = turtle.Screen()
x = 0
chatBtn.shape("square")
text.penup()
randomword.penup()
chatBtn.penup()
chatBtn.goto(122,-90)
text.goto(100, 60)
text.right(90)
turtle.speed(0)
turtle.penup()
turtle.goto(98, 75)
turtle.pendown()
turtle.hideturtle()
text.hideturtle()
randomword.hideturtle()



#מצייר לוח
for c in range(2):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
turtle.pendown()
turtle.goto(98, -75)
turtle.right(90)
for c in range(2):
    turtle.right(90)
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(300)
turtle.penup()
turtle.goto(-150, 225)
turtle.right(180)
turtle.pendown()
for c in range(2):
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)

#בוחר מילה רנדומלית
def wordGen():
    global chosenrandomword
    randomword.goto(-140,225)
    with open(".random_words.txt") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        chosenrandomword = random.choice(words)
        randomword.write(chosenrandomword, font = ('Arial', 16, 'normal'))
wordGen()


# setting players and screen
player = turtle.Turtle()
player.speed(0)
# setting clear button
clearbtn = turtle.Turtle()
clearbtn.speed(0)
clearbtn.penup()
clearbtn.shape("square")
clearbtn.goto(0, -150)
# setting eraser button
eraser = turtle.Turtle()
eraser.speed(0)
eraser.penup()
eraser.shape("square")
eraser.goto(160, -150)

#הגדרת 4 ריבועים TURTLE ל4 צבעים
def colorShapeCreate(nameColor, x,y):
    colorBtn = turtle.Turtle()
    colorBtn.speed(0)
    colorBtn.shape("circle")
    colorBtn.color(nameColor)
    colorBtn.shapesize(2)
    colorBtn.penup()
    colorBtn.goto(x, y)
    def changeColor(x,y):
        player.color(nameColor)
    colorBtn.onclick(changeColor, btn=3)
    

Gra = turtle.Turtle()
Gra.speed(0)
Gra.shape("circle")
Gra.color("gray")
Gra.shapesize(2)
Gra.penup()
Gra.goto(-305, -100)

Br = turtle.Turtle()
Br.speed(0)
Br.shape("circle")
Br.color("brown")
Br.shapesize(2)
Br.penup()
Br.goto(-260, -100)

G = turtle.Turtle()
G.speed(0)
G.shape("circle")
G.color("green")
G.shapesize(2)
G.penup()
G.goto(-215, -100)


R = turtle.Turtle()
R.speed(0)
R.shape("circle")
R.color("red")
R.shapesize(2)
R.penup()
R.goto(-170, -100)


Y = turtle.Turtle()
Y.speed(0)
Y.shape("circle")
Y.color("yellow")
Y.shapesize(2)
Y.penup()
Y.goto(-125, -100)

Bl = turtle.Turtle()
Bl.speed(0)
Bl.shape("circle")
Bl.color("blue")
Bl.shapesize(2)
Bl.penup()
Bl.goto(-80, -100)

Pi = turtle.Turtle()
Pi.speed(0)
Pi.shape("circle")
Pi.color("pink")
Pi.shapesize(2)
Pi.penup()
Pi.goto(-35, -100)

Pu = turtle.Turtle()
Pu.speed(0)
Pu.shape("circle")
Pu.color("purple")
Pu.shapesize(2)
Pu.penup()
Pu.goto(10, -100)

Bla = turtle.Turtle()
Bla.speed(0)
Bla.shape("circle")
Bla.color("black")
Bla.shapesize(2)
Bla.penup()
Bla.goto(55, -100)

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

# fill color


def fill(x, y):
    player.fillcolor()

# setting colors
# methods for color buttons


def ColorGreen(x, y):
    player.color("green")


def ColorRed(x, y):
    player.color("red")


def ColorYellow(x, y):
    player.color("yellow")


def ColorBlue(x, y):
    player.color("blue")


def ColorPink(x, y):
    player.color("pink")


def ColorPurple(x, y):
    player.color("purple")


def ColorBrown(x, y):
    player.color("brown")


def ColorGray(x, y):
    player.color("gray")


def ColorBlack(x, y):
    player.color("black")


def eraserWhite(x, y,):
    player.pencolor("white")


def goto(x, y):
    if x > -343 and x < 88 and y < 215 and y > -63:
        player.pendown()
        player.ondrag(None)
        player.goto(x, y)
        player.ondrag(goto)


def pensize2(x, y):
    player.pensize(2)


def pensize5(x, y):
    player.pensize(5)


def pensize10(x, y):
    player.pensize(10)


def teleportto(x, y):
    if x > -343 and x < 88 and y < 215 and y > -63:
        player.penup()
        player.goto(x, y)
        player.pendown()


def clearpaint(x, y):
    player.clear()

counting = 0
#מכין טקסט מתחדש
def chatPopUp(x,y):
    global answer
    global counting
    value = screen.textinput("what is your guess?", "enter here")
    text.write(value)
    answer = value
    text.forward(10)
    counting += 1
    if counting == 14:
        text.goto(100, 60)
        text.clear()
        counting = 0
    if answer == chosenrandomword:
        randomword.clear()
        answer = ""
        wordGen()


def painter():
    # buttons location
    psize2.goto(-200, -150)
    psize5.goto(-250, -150)
    psize10.goto(-300, -150)

    # basic UI setup
    clearbtn.write("clear", align='center', move=True)
    chatBtn.write("press to chat", align='center', move=True)
    eraser.write("eraser", align='center', move=True)
    psize2.write("2", align='center', move=True)
    psize5.write("5", align='center', move=True)
    psize10.write("10", align='center', move=True)

    # going a bit below the text so the text can be shown
    clearbtn.goto(0, -160)
    chatBtn.goto(122,-100)
    eraser.goto(160, -160)
    psize2.goto(-200, -160)
    psize5.goto(-250, -160)
    psize10.goto(-300, -160)

    # on click methods
    clearbtn.onclick(clearpaint)
    Br.onclick(ColorBrown)
    Bl.onclick(ColorBlue)
    Bla.onclick(ColorBlack)
    Pi.onclick(ColorPink)
    Gra.onclick(ColorGray)
    G.onclick(ColorGreen)
    Y.onclick(ColorYellow)
    R.onclick(ColorRed)
    Pu.onclick(ColorPurple)
    eraser.onclick(eraserWhite)
    psize2.onclick(pensize2)
    psize5.onclick(pensize5)
    psize10.onclick(pensize10)
    screen.onclick(teleportto)
    player.onclick(fill, btn=3)
    player.ondrag(goto)
    chatBtn.onclick(chatPopUp)


painter()




screen.listen()
turtle.mainloop()

