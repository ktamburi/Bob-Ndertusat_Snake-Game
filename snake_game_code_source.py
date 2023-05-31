import turtle
import tkinter as TK

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
