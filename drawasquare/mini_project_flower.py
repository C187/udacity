import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(50)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #make a flower
    flower = turtle.Turtle()
    flower.shape("circle")
    flower.color("white")
    flower.speed(1000)
    for i in range(1,37):
        draw_square(flower)
        flower.right(10)
 
    #make a stem
    line = turtle.Turtle()
    line.shape("square")
    line.color("white")
    line.right(90)
    line.forward(200)

    window.exitonclick()


draw_art()

