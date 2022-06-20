from cmath import pi
from itertools import count
import string
import turtle
import random
import winsound


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
    global isHidden
    randomword.clear()
    answer = ""
    isHidden = False
    hideBtn.clear()
    hideBtn.goto(-60,250)
    hideBtn.write("hide", align='center', move=True)
    hideBtn.goto(-60,240)
    randomword.goto(-140,225)
    with open(".random_words.txt") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        chosenrandomword = random.choice(words)
        randomword.write(chosenrandomword, font = ('Arial', 16, 'normal'))



# setting player
player = turtle.Turtle()
player.speed(0)
player.pensize(2)
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
# setting a button to hide word
hideBtn = turtle.Turtle()
hideBtn.speed(0)
hideBtn.penup()
hideBtn.shape("square")
hideBtn.goto(-60,250)
hideBtn.write("hide", align='center', move=True)
hideBtn.goto(-60,240)
isHidden = False


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
    colorBtn.onclick(changeColor)
    
colorShapeCreate("gray", -305,-100)
colorShapeCreate("brown", -260,-100)
colorShapeCreate("green", -215,-100)
colorShapeCreate("red", -170,-100)
colorShapeCreate("yellow", -125,-100)
colorShapeCreate("blue",-80 ,-100)
colorShapeCreate("pink",-35 ,-100)
colorShapeCreate("purple",10 ,-100)
colorShapeCreate("black",55 ,-100)




# setting pen size buttons
def psize(pSizeNum, x,y):
    pSizeBtn = turtle.Turtle()
    pSizeBtn.speed(0)
    pSizeBtn.penup()
    pSizeBtn.shape("square")
    pSizeBtn.goto(x,y)
    pSizeBtn.write(pSizeNum, align='center', move=True)
    pSizeBtn.goto(x,y - 10)
    def changePSize(x,y):
        player.pensize(pSizeNum)
    pSizeBtn.onclick(changePSize)
psize(2, -200, -150)
psize(5, -250, -150)
psize(10, -300, -150)


player.shape("circle")
player.shapesize(1)
# setting colors

def eraserWhite(x, y,):
    player.pencolor("white")


def goto(x, y):
    if x > -343 and x < 88 and y < 215 and y > -63:
        player.pendown()
        player.ondrag(None)
        player.goto(x, y)
        player.ondrag(goto)



def teleportto(x, y):
    if x > -343 and x < 88 and y < 215 and y > -63:
        player.penup()
        player.goto(x, y)
        player.pendown()


def clearpaint(x, y):
    player.clear()

counting = 0

def hideWord(x,y):
    global isHidden
    if isHidden == False:
        isHidden = True
        randomword.clear()
        hideBtn.clear()
        hideBtn.goto(-60,250)
        hideBtn.write("show", align='center', move=True)
        hideBtn.goto(-60,240)
    else:
        isHidden = False
        randomword.goto(-140,225)
        randomword.write(chosenrandomword, font = ('Arial', 16, 'normal'))
        hideBtn.clear()
        hideBtn.goto(-60,250)
        hideBtn.write("hide", align='center', move=True)
        hideBtn.goto(-60,240)
#מכין טקסט מתחדש
def chatPopUp(x,y):
    global answer
    global counting
    global isHidden
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
        winsound.PlaySound('win.wav', 1)
        wordGen()

def painter():

    # basic UI setup
    clearbtn.write("clear", align='center', move=True)
    chatBtn.write("press to chat", align='center', move=True)
    eraser.write("eraser", align='center', move=True)

    # going a bit below the text so the text can be shown
    clearbtn.goto(0, -160)
    chatBtn.goto(122,-100)
    eraser.goto(160, -160)

    # on click methods
    clearbtn.onclick(clearpaint)
    hideBtn.onclick(hideWord)
    eraser.onclick(eraserWhite)
    screen.onclick(teleportto)
    player.ondrag(goto)
    chatBtn.onclick(chatPopUp)

    wordGen()


painter()




screen.listen()
turtle.mainloop()

