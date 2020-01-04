import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("black")
wn.tracer(1)

#score2 yi yazmak için kullandım
mypen0=turtle.Turtle()
mypen0.color("white")
mypen0.penup()
mypen0.hideturtle()


#oyun alanını çizdim
mypen=turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-250,-250)
mypen.pendown()
mypen.pensize(4)
mypen.speed(9)
for i in range(4):
    mypen.forward(500)
    mypen.left(90)
mypen.hideturtle()

#1. oyuncumuzu oluşturdum
player1 = turtle.Turtle()
player1.color("green")
player1.shape("turtle")
player1.penup()
player1.setposition(230,230)
speed1 = 1

#2. oyuncumuzu oluşturdum
player2 = turtle.Turtle()
player2.color("yellow")
player2.shape("turtle")
player2.penup()
player2.setposition(-230,-230)
speed2 = 1


#oyuncuların puan kaybedeceği şeyler oluşturdum
Maxtop=2
top=[]

for i in range(Maxtop):
    top.append(turtle.Turtle())
    top[i].color("red")
    top[i].shape("triangle")
    top[i].penup()
    top[i].speed(0)
    top[i].setposition(random.randint(-250,250),random.randint(-250,250))
    
#oyuncuların puan kazanacağı hedefler oluşturdum  
goal = turtle.Turtle()
goal.color("blue")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100,100)    

#scoreları tanımladım    
score1=0
score2=0


#hullanacağım fonksiyonları yazdım
def turnleft1():
    player1.left(30)

def turnright1():
    player1.right(30)
    
def hızart1():
    global speed1
    speed1 += 1
    
    
def hızaz1():
    global speed1
    speed1 -= 1
    
    
def turnleft2():
    player2.left(30)

def turnright2():
    player2.right(30)
    
def hızart2():
    global speed2
    speed2 += 1
    
    
def hızaz2():
    global speed2
    speed2 -= 1
    
    
    
def isCollision(t1,t2):
    d= math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False



turtle.listen()
turtle.onkey(turnleft1, "Left")
turtle.onkey(turnright1, "Right")
turtle.onkey(hızart1, "Up")
turtle.onkey(hızaz1, "Down")
turtle.onkey(turnleft2, "d")
turtle.onkey(turnright2, "a")
turtle.onkey(hızart2, "w")
turtle.onkey(hızaz2, "s")



while True:
    player1.forward(speed1)
    player2.forward(speed2)
    
    #çizdiğim alanın dışına çıkmalarını engelledim
    if player1.xcor() > 250 or player1.xcor() < -250:
        player1.left(180)
       
    if player1.ycor() > 250 or player1.ycor() < -250:
        player1.left(180)
        
    if player2.xcor() > 250 or player2.xcor() < -250:
        player2.left(180)
       
    if player2.ycor() > 250 or player2.ycor() < -250:
        player2.left(180)
        

        #-1 puan veren hedefleri haraketli yaptım
    for i in range(Maxtop):
        top[i].forward(3)
        if top[i].xcor() > 250 or top[i].xcor() < -250:
            top[i].left(180)
        if top[i].ycor() > 250 or top[i].ycor() < -250:
            top[i].left(180)
                
        
        #Collision Cheking
        if isCollision(player1,top[i]):
            top[i].setposition(random.randint(-250,250),random.randint(-250,250))
            top[i].right(random.randint(0,360))
            score1 -= 1
            
            #scoru ekrana yazdırma
            mypen.undo() #eski yazılanları silmek için
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-240,260)
            score1string= "Score1: %s" %score1
            mypen.write(score1string, False, align="Left", font=("Arial",14,"normal") ) 
          
        
        
        if isCollision(player2,top[i]):
            top[i].setposition(random.randint(-250,250),random.randint(-250,250))
            top[i].right(random.randint(0,360))
            score2 -= 1
            
            mypen0.undo() 
            mypen0.penup()
            mypen0.hideturtle()
            mypen0.setposition(150,260)
            score2string= "Score2: %s" %score2
            mypen0.write(score2string, False, align="Left", font=("Arial",14,"normal") )
            
        
        
        if isCollision(player1,goal):
            goal.setposition(random.randint(-250,250),random.randint(-250,250))
            score1 += 1
            
            mypen.undo() 
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-240,260)
            score1string= "Score1: %s" %score1
            mypen.write(score1string, False, align="Left", font=("Arial",14,"normal") )
            
            
            
        if isCollision(player2,goal):
            goal.setposition(random.randint(-250,250),random.randint(-250,250))
            score2 += 1
            
            mypen0.undo() 
            mypen0.penup()
            mypen0.hideturtle()
            mypen0.setposition(150,260)
            score2string= "Score2: %s" %score2
            mypen0.write(score2string, False, align="Left", font=("Arial",14,"normal") )
            
            
        if score1==10:
            mypen.undo() 
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-100,0)
            finstring= "1. oyuncu kazandı!" 
            mypen.write(finstring, False, align="Left", font=("Arial",14,"normal") )
            break
            
        if score2==10:
            mypen.undo() 
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-100,0)
            finstring= "2. oyuncu kazandı!" 
            mypen.write(finstring, False, align="Left", font=("Arial",14,"normal") )
            break
            
        
            
        
        
          
          
    
    
       






