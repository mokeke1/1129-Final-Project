#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import turtle
import turtle 

#define a function to draw a rectanly
def draw_rectangle(length, height, r,g,b, x = 0, y = 0):
    #rename turtle as "t" to simplify code
    t = turtle.Turtle()
    #specify color of rectangle
    t.fillcolor(r,g,b)
    #hide the turtle cursor when drawing
    t.hideturtle()
    #specify where to start drawing
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    #tell the cursor which direction to go in each direction, plus a 90 degree turn for each corner
    for i in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(height)
        t.rt(90)
    #fill the rectangle with the specified color
    t.end_fill()
    t.setx(length)

#define a function to call the r,g,b color parameters for a given color
def get_color(color):
    #set function for each color when called: red, white, and blue
    if color == "red":
        return 1,0,0
    if color == "white":
        return 1,1,1
    if color == "blue":
        return 0,0,1
    else:
        return 0,0,0

#define a function for drawing stars
def draw_star(size, r,g,b, x = 0, y = 0):
    #rename turtle and speed up drawing time for efficiency
    t = turtle.Turtle()
    t.speed(400)
    t.pencolor(get_color("white"))
    t.up()
    #tell the cursor to turn 144 degrees at each point
    turn = 144
    #tell the cursor where to begin
    t.goto(x,y)
    #fill with color
    t.fillcolor(r,g,b)
    #hide the turtle cursor to keep things neat
    t.hideturtle()
    t.down()
    #fill the star with the color pulled earlier
    t.begin_fill()
    #tell the cursor to turn five times to draw a five point star
    for i in range(5):
        t.fd(size)
        t.rt(turn)
    t.end_fill()
    
#define a function for drawing stripes
def draw_stripes(fly, fc, stripe, r, g, b, hc):
    #draw the first seven stripes next to the canton
    for i in range (1,7):
        #odd numbered stripes should be colored white
        if i % 2 == 1:
            r,g,b = get_color("white")
        #even numbered stripes should be colord red
        else:
            r,g,b = get_color("red")
        #actually draw the rectangular stripes
        draw_rectangle(fly - fc, stripe, r,g,b, fc, -stripe * i)

    #draw the final six stripes below the canton
    for i in range (0,6):
        #even numbered stripes should be white, unlike before
        if i % 2 == 0:
            r,g,b = get_color("white")
        #odd numbered stripes should be red
        else:
            r,g,b = get_color("red")
        #actually draw the rectangular stripes
        draw_rectangle(fly, stripe, r,g,b, 0, -hc + (-stripe * i))

#define a function to draw the entire flag, calling all earlier functions
def draw_flag(height):
    #use the height variable to define all other dimensions as specified on Wikipedia
    #fly, aka the length of the flag
    fly = 1.9 * height
    #hoist of the canon, aka its height
    hc = height * (7/13)
    #fly of the canon, aka its length
    fc = fly * (2/5)
    #height of a stripe; it's length is the same as the flag
    stripe = height / 13
    #size of the stars
    star = stripe * (4/5)
    #vertical unit of distance between stars
    e = hc / 10
    #horizontal unit of distance between stars
    h = fc / 14
    #call the color function to define the color red in r,g,b
    r,g,b = get_color("red")
    #draw a red rectangle for the whole shape of the flag
    draw_rectangle(fly, height, r,g,b)
    #call the color function to define the color blue in r,g,b
    r,g,b = get_color("blue")
    #draw a blue rectangle for the canton
    draw_rectangle(fc, hc, r,g,b)
    #draw all 13 stripes
    draw_stripes(fly, fc, stripe, r, g, b, hc)
    #call the color function to define the color white in r,g,b
    r,g,b = get_color("white")
    #draw six columns with five stars each
    for i in range(1,12,2):
        for j in range(1,10, 2):
            draw_star(star, r,g,b, e * i , -h * j )
    #draw five more columns with four stars each, set lower and to the right
    for i in range(2,12,2):
        for j in range(2,10,2):
            draw_star(star,r,g,b, e * i, -h * j)

#define a main function to call the draw_flag function, and specify a height of 100
def main():
    draw_flag(100)

#call the main function
if __name__ == "__main__":
    main()


# In[ ]:




