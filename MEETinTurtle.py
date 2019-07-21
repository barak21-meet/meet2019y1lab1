import turtle
# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

#draw the E
turtle.penup()
turtle.goto(0,100)

turtle.pendown()

turtle.goto(0,-100)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(100,100)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(100,0)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.goto(100,-100)
#end of the E

#draw the other E
turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.goto(200,-100)

turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.goto(300,100)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.goto(300,0)

turtle.penup()
turtle.goto(200,-100)
turtle.pendown()
turtle.goto(300,-100)
#end of the other E

#draw the T
turtle.penup()
turtle.goto(400,100)
turtle.pendown()
turtle.goto(400,-100)

turtle.penup()
turtle.goto(350,100)
turtle.pendown()
turtle.goto(450,100)

# ...and end it before the next line.
turtle.mainloop() 
# turtle.mainloop() tells the turtle to do all
# the turtle commands above it and paint it on the screen.
# It always has to be the last line of code!

