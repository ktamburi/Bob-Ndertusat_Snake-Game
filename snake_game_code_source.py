import turtle
import tkinter as TK
import time
import random

#window setup
wn=turtle.Screen() 
wn.setup(width=700,height=650) 
root = wn.getcanvas().winfo_toplevel() 
root.resizable(False, False) 
wn.title("Snake Game by Bob Ndertusat") 
wn.bgcolor('#60D164') 
wn.tracer(0) 

#snake head setup
head=turtle.Turtle() 
head.speed(0)   
head.color('#030721')  
head.shape("circle") 
head.shapesize(1.1) 
head.penup()    
head.goto(0,0)  
head.direction="stop" 

#snake initial body setup
body = [] 
for index in range(1,4,+1): 
    body_part=turtle.Turtle() 
    body_part.speed(0) 
    body_part.shape("circle") 
    body_part.color('#383fff') 
    body_part.penup() 
    body_part.goto(head.xcor()-(20*index),0) 
    body.append(body_part) 
    
#snake food
apple=turtle.Turtle()
apple.speed(0)  
apple.color("red") 
apple.shape("triangle")
apple.shapesize(0.8) 
apple.penup()    
apple.goto(80,0)  

#function to grow snake each time it feeds
def newbody():
    new_body_part=turtle.Turtle()
    new_body_part.speed(0)
    new_body_part.shape("circle")
    new_body_part.color('#383fff')
    new_body_part.penup()
    body.append(new_body_part) 
    
#function to update the movement of body
def bodymove():
    if head.direction=="left" or head.direction=="right" or head.direction=="up" or head.direction=="down":
        for index in range(len(body)-1,-1,-1):
            x=body[index-1].xcor()
            y=body[index-1].ycor()
            body[index].goto(x,y)        
            if index==0:
                x=head.xcor()
                y=head.ycor()
                body[0].goto(x,y)

#functions to update the movement of the snake
game=True 
def go_up():
    global game
    if head.direction !="down" and game!=False:
        head.direction="up"
def go_down():
    global game
    if head.direction !="up" and game!=False:
        head.direction="down"
def go_right():
    global game
    if head.direction !="left" and game!=False:
        head.direction="right"
def go_left():
    global game
    if head.direction !="right" and game!=False:
        head.direction="left"

#function determining how the snake head moves
def move(): 
    if head.direction=="up": 
        head.sety(head.ycor()+20) 
    if head.direction=="down": 
        head.sety(head.ycor()-20) 
    if head.direction=="left": 
        head.setx(head.xcor()-20) 
    if head.direction=="right": 
        head.setx(head.xcor()+20) 
        
#defining function for food collision
def food_collision():
    if head.distance(apple)<18:
        x=random.randint(-335,335)
        y=random.randint(-310,310)  
        apple.goto(x,y)
        newbody()

        #function call to increase score for added body part
        


#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"W")
wn.onkeypress(go_up,"w")
wn.onkeypress(go_up,"Up") 
wn.onkeypress(go_down,"s") 
wn.onkeypress(go_down,"S") 
wn.onkeypress(go_down,"Down") 
wn.onkeypress(go_left,"a")
wn.onkeypress(go_left,"A")
wn.onkeypress(go_left,"Left") 
wn.onkeypress(go_right,"D")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_right,"Right")

while True:
    wn.update()
    
    food_collision()
    bodymove()
    move()
    
    time.sleep(0.08)
