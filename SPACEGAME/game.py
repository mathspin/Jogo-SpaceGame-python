import turtle
import random
import os
import time
#from graphics import*



wn = turtle.Screen()
wn.title("Game")
wn.bgcolor("#5c5c5c")
wn.setup(width = 900, height = 750)
#wn.screensize(9000,9000)
wn.tracer(3)
wn.bgpic("tumblr_back copia.gif")

#-----
#score
#-----

score = 0

hidescore = 0

playerlife = 5

level = 0

difficulty = 1

pen = turtle.Turtle()
pen.hideturtle()

pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(-360,-300)
pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))

#------
#border
#------

border_pen = turtle.Turtle()
border_pen.speed(0)
#border_pen.color("#081754")
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-350)
border_pen.pendown()
border_pen.pensize(10)

border_pen.fd(600)
border_pen.lt(90)
border_pen.fd(700)
border_pen.lt(90)
border_pen.fd(600)
border_pen.lt(90)
border_pen.fd(700)
border_pen.lt(90)
border_pen.hideturtle()


#-------
#player
#-------

playerspeed = 10


player = turtle.Turtle()
player.setheading(90)
player.shapesize(2.5,2.5)
player.color("#f2dc35")
player.shape("classic")
player.penup()
player.speed(0)
player.goto(0,-300)
player.direction = "stop"

def go_left():
     player.direction = "left"

def go_right():
     player.direction = "right"

def go_stop():
     player.direction = "stop"


#-------
#badguy
#-------

bad_guysnumber = 5

bad_guys = []


for _ in range (bad_guysnumber):

     
     bad_guy = turtle.Turtle()
     bad_guy.setheading(270)
     bad_guy.shapesize(2.5,2.5, outline = 2)
     bad_guy.color("black")#A2FF00
     bad_guy.fillcolor("#A2FF00")
     bad_guy.shape("classic")
     bad_guy.penup()
     bad_guy.speed(0)
     x = random.randint(-280, 280)
     y = random.randint(380, 700)
     bad_guy.goto(x,y)
     bad_guyspeed = 1
     bad_guyspeedx = random.uniform(0.5,1)
     bad_guys.append(bad_guy)



#------
#bullet
#------

bulletspeed = 20

bullet = turtle.Turtle()
bullet.color("#f0580c")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet.goto(-900,-900)

bulletstate  ="ready"




def fire_bullet():
     global bulletstate
     if bulletstate =="ready":

          bulletstate = "fire"         
          x = player.xcor()
          y = player.ycor() + 8
          bullet.setposition(x,y)
          #bullet.showturtle()




#-----
#laser
#-----


lasers = []

lasernumber = 3


for _ in range (lasernumber):

     
     laser = turtle.Turtle()
     laser.shape("circle")
     laser.color("orange")
     laser.shapesize(0.5,0.5)
     laser.shapesize(stretch_wid = 5, stretch_len = 0.1, outline = None)
     laser.penup()
     laser.speed(0)
     x = random.randint(-280, 280)
     y = random.randint(380, 1000)
     laser.goto(x,y)
     laserspeed = 8 #random.uniform(1, 3)
     lasers.append(laser)



#--------
#upborder
#--------

upborder = turtle.Turtle()
upborder.color("#081754")
upborder.shape("square")
upborder.penup()
upborder.speed(0)
upborder.goto(0,450)
upborder.shapesize(10,31)
#upborder.hideturtle()


#--------
#downborder
#--------

downborder = turtle.Turtle()
downborder.color("#081754")
downborder.shape("square")
downborder.penup()
downborder.speed(0)
downborder.goto(0,-450)
downborder.shapesize(10,31)


#---------
#gameover
#---------

'''tryagain = turtle.Turtle()
tryagain.hideturtle()
tryagain.penup()
tryagain.color("white")
tryagain.speed(0)
tryagain.goto(-150,0)
tryagain.write(("GAME OVER \n \n Para jogar novamente digite 's' \n            para parar digite 'n'"), False, align = "left", font =("Arial", 14,"normal"))
tryagain.hideturtle()
tryagain.clear()'''


start = "s"




#--------
#tutorial
#--------


while level == 0:
     teach = wn.textinput("SPACE GAME", "TUTORIAL \n \n \n  Para se movimentar utilize as setas direita e esquerda \n \n Para atirar utilize espaço \n \n Atire nas naves verdes impedindo elas de atravessar e evite os lasers laranjas \n \n \n Digite 's' para começar. Bom jogo :)")

     if teach == 's':
          level += 1
     else:
          level = 0
 



#-----------
#keybindings
#-----------

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkey(fire_bullet, "space")
wn.onkeyrelease(go_stop,"Left")
wn.onkeyrelease(go_stop,"Right")






#---------
#game loop
#---------

while start == "s":
     
     wn.update()

     #--------
     #gameover
     #--------

     if playerlife <= 0:
          tryagain = wn.textinput("GAME OVER", "Para jogar novamente digite 's' \n            para parar digite 'n'")

          if tryagain == "s":
               playerlife = 5
               score = 0
               hidescore = 0
               level = 1
               difficulty = 1
               start = "s"
               wn.listen()
               for bad_guy in bad_guys:
                    x = random.randint(-280, 280)
                    y = random.randint(380, 700)
                    bad_guy.goto(x,y)
               pen.clear()
               pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))
               time.sleep(0.5)
               
          elif tryagain == "n":
               start = "n"
               
          else:
               start =="s"
     

     #--------
     #moviment
     #--------

     if player.direction == "left":
          x = player.xcor()
          x -= playerspeed 
          player.setx(x)          
          if x <= -280:
               x = -280
          player.setx(x)
          #player.direction = "stop"  




     if player.direction == "right":
           x = player.xcor()
           x += playerspeed 
           player.setx(x)
           if x >= 280:
               x = 280
           player.setx(x)
           #player.direction = "stop"




     for bad_guy in bad_guys:
          y = bad_guy.ycor()
          x = bad_guy.xcor()
          y -= bad_guyspeed * difficulty
          x -= bad_guyspeedx
          
                            
          if x <= -280:
               x = -275
               bad_guyspeedx *= -1
               bad_guy.setx(x)

          if x >= 280:
               x = 275
               bad_guyspeedx *= -1
               bad_guy.setx(x)
          bad_guy.sety(y)
          bad_guy.setx(x)

          if bad_guy.ycor() <= -350:
               x = random.randint(-280, 280)
               y = random.randint(380, 700)
               bad_guy.sety(y)
               playerlife -= 1
               pen.clear()
               pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))

          
          


          #---------
          #collision
          #---------


          if bad_guy.distance(player) <= 20:
               x = random.randint(-280, 280)
               y = random.randint(380, 700)
               bad_guy.goto(x, y)
               playerlife -= 1
               pen.clear()
               pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))


          if bad_guy.distance(bullet) <= 20:
               x = random.randint(-280, 280)
               y = random.randint(380, 700)
               bad_guy.goto(x, y)
               score += 100
               hidescore += 100
               pen.clear()
               pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))



     for laser in lasers:
          y = laser.ycor()
          y -= laserspeed
          laser.sety(y)

          if y < -350:
               x = random.randint(-280, 280)
               y = random.randint(380, 700)
               laser.goto(x, y)

          
          #---------
          #collision
          #---------


          if laser.distance(player) <= 20:
               x = random.randint(-280, 280)
               y = random.randint(380, 700)
               laser.goto(x, y)
               playerlife -= 1
               pen.clear()
               pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))

     #--------
     #shooting
     #--------


     if bulletstate =="fire":
          bullet.showturtle()
          y = bullet.ycor()
          y += bulletspeed
          bullet.sety(y)

     if bullet.ycor() >= 330:
          bullet.setx(-900)
          bulletstate = "ready"
          bullet.hideturtle()
          bullet.clear()
          #time.sleep(0.03)
          #bulletstate = "ready"




     #-----
     #level
     #-----


     if hidescore >= 1000:
          hidescore = 0
          level += 1
          difficulty += 1
          playerlife += 1
          if playerlife > 5:
               playerlife = 5
          pen.clear()
          pen.write(("Score: \n {} \n Lives: \n {} \n \n Level: \n {}").format(score, playerlife, level), False, align = "left", font =("Arial", 14,"normal"))


     '''#--------
     #gameover
     #--------

     while playerlife <= 0:
          start = wn.textinput("GAME OVER", "Para jogar novamente digite 's' \n            para parar digite 'n'")

          if start == "s" or start == "n":
               playerlife = 5
               score = 0
               time.sleep(1)
               break'''
          
     

