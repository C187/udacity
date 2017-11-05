import turtle

window = turtle.Screen()
window.bgcolor("black")

def draw_square():  
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(4)

    count = 0
    while count < 4:
        brad.forward(100)
        brad.right(90)
        count = count + 1

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
    
    window.exitonclick()
    
draw_square()
#draw_circle()
#draw_triangle()
