from library import turn_right
from library import move_x
from library import turn_around
from library import left
from library import corner
from library import right
from library import home
def takeobject():
    while object_here():
        take()
def step():
    while front_is_clear():
        takeobject()
        move()        

step()
takeobject()
left()
step()
corner()

step()
left()
step()
right()
step()
left()
step()

turn_left()
while front_is_clear():
    move()
while carries_object():
    toss()
    
home()
    





    

    
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    for r in range(0,3):
        turn_left()
        
def move_x(x):
    for x in range(0,x):
        move()
        
def turn_around():
    turn_left()
    turn_left()  

def left():
    while object_here():
        take()
    turn_left()
    move()
    turn_left()
    
def corner():
    turn_right()
    move()
    turn_left()
    move()
    turn_around()
    
def right():
    while object_here():
        take()
    turn_right()
    move()
    turn_right()
    
def home():
    while object_here():
        take()
    turn_left()
    move()
    turn_right()
    move_x(2)
    turn_right()
    move()
    
    