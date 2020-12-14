def turn_right():
    for r in range(0,3):
        turn_left()
def move_x(x):
    for x in range(0,x):
        move()
turn_left()
move_x(2)
turn_right()
move_x(2)
def harvest():
    for r in range(0,6):
        while object_here():
            take()
        else:
            move()        
def left():
    for r in range(0,2):
        turn_left()
        move()
def right():
    for r in range(0,2):
        turn_right()
        move()        
def harvest_all():
    harvest()
    left()
    harvest()
    right()    
for r in range(0,3):
    harvest_all()

        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
