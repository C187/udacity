import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(4)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()
    

draw_square()
