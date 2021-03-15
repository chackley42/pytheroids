import turtle
import tkinter.messagebox
import tkinter
import random
import math 
#initialize screen for turtle
wndw = turtle.Screen()
wndw.bgcolor("light blue")
wndw.title("WTF am I doing")
speed = 1 # default speed for player
# Register new shapes in the .Screen method
# New shapes penpoint start at the first defined point
wndw.register_shape("spaceShip", ((0,0),(-10,-15),(0,-10),(10,-15),(0,0))) 

# Create border
mypen = turtle.Turtle()
mypen.color("black")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.speed(0)
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create goal
goal = turtle.Turtle()
goal.color("green")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100,100) 

#Collision of objects function
def isCollision(t1,t2):
    """
    Determines collision between two turtle objects (t1 and t2)
    """
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False



# Player turtle function
def playa():
    """
    Contains anything pertaining to the player sprite
    """
    player = turtle.Turtle() #makes the actual turtle
    player.color("Red") #player color 
    player.shape("spaceShip") #Consider creating a shape and registering it later
    player.penup() #get rid of trace. Will attempt disapearing trace later
    player.speed(0) #Animation speed. This will make turning less rigid
    
    # movement functions by angle
    def warp():
        """
        boosts player forward 100 units. 
        """
        player.forward(100)

    def turnLeft():
        """
        Turn Player left
        """
        player.left(30)
    
    def turnRight():
        """
        Turn Player right
        """
        player.right(30)

    def speedUp():
        """
        Increases player speed
        """
        global speed
        speed += 1
    
    def slowDown():
        """
        Slows down player speed
        """
        global speed 
        if speed == 1:
            speed - 0
        else:
            speed = speed - 1
        
    # key controls for player (keyboard binding)
    wndw.onkeyrelease(warp, "space")
    wndw.onkeypress(turnLeft, "Left")
    wndw.onkeypress(turnRight, "Right")
    wndw.onkeypress(speedUp, "Up")
    wndw.onkeypress(slowDown, "Down")
    wndw.listen()
    
    #Keep forward movement
    while True:
        player.forward(speed)
        # Boundaries
        if player.xcor() > 300 or player.xcor() < -300:
            player.right(180)
        if player.ycor() > 300 or player.ycor() < -300:
            player.right(180)
        
        #Collision from boolean value from isCollision function
        if isCollision(player, goal):
            goal.setposition(random.randint(-300,300), random.randint(-300, 300))

        # Move goal forward
        goal.forward(random.randint(0,10))
        goal.right(random.randint(0,360)) #randomly move 0-360 to the right.
# End playa()

#main  function
def main():
    
    

    # Call player function 
    playa()
    
    

    
    


# Call main function to show the screen
main()

wndw.mainloop()