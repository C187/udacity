import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Create the turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(1000)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()
    #count = 0
    #while count < 4:
        #brad.forward(100)
        #brad.right(90)
        #count = count + 1

#Below hidden to make a circle out of squares.
    
#def draw_circle():
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

#def draw_triangle():
    #bob = turtle.Turtle()
    #bob.shape("triangle")
    #bob.color("red")

    #count = 0
    #while count < 3:
        #bob.forward(100)
        #bob.right(120)
        #count = count + 1
    
    

draw_art()
#draw_square()
#draw_circle()
#draw_triangle()
