from library import turn_right
from library import move_x
from library import turn_around

while front_is_clear():
    while object_here():
        take()
    move()
else:
    while object_here():
        take()
    turn_left()
    move()
    turn_left()
    move_x(4)
while carries_object():
    toss()
turn_left()
move()
turn_right()
move()
    


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
    
def building():
    turn_left()
    build_wall()
    turn_left()
    