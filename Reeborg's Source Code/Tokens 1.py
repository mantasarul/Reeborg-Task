move()
take()
move()
put()
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

def left():
    while object_here():
        take()    
    turn_left()
    if wall_in_front():
        turn_left()
        while front_is_clear():
            move()
        turn_left()
        while front_is_clear():
            move()
        dump()    
        #break
    else:
        move()
        turn_left()
        
def corner():
    turn_right()
    takeobject()
    move()
    turn_left()
    takeobject()
    move()
    turn_around()
    takeobject()
    
def dump():
    while carries_object():
        toss()
    home()
    
    
def right():
    while object_here():
        take()        
    turn_right()
    if wall_in_front():
        turn_around()
        while front_is_clear():
            move()
        dump()
        #break
    else:
        move()
        turn_right()
    
def home():
    turn_left()
    move()
    turn_right()
    move_x(2)
    turn_right()
    move()
    
    
def bypass():
    takeobject()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_right()
    takeobject()
    
    
def wall_on_left():
    turn_around()
    wall_on_right()
    
def takeobject():
    while object_here():
        take()

def step_upto_corner():
    step()
    takeobject()
    left()
    step()
    corner()

def step():
    while not wall_in_front():
        if not wall_in_front() and front_is_clear():
            takeobject()
            move()
        elif not front_is_clear() and not wall_in_front():
            bypass()
