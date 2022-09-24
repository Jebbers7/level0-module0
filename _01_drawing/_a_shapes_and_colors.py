import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Jimmy = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Jimmy.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Jimmy.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Jimmy.color('green')
    Jimmy.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        Jimmy.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        Jimmy.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Jimmy.goto(200,200)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Jimmy.pencolor('green')
    Jimmy.begin_fill()
    Jimmy.circle(25, 30)
    Jimmy.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    Jimmy.pencolor('red')
    Jimmy.fillcolor('red')
    Jimmy.goto(-100, -100)
    Jimmy.begin_fill()
    for i in range(8):
        Jimmy.forward(20)
        Jimmy.left(45)
    Jimmy.end_fill()

    Jimmy.pencolor('orange')
    Jimmy.fillcolor('orange')
    Jimmy.goto(-200,-200)
    Jimmy.begin_fill()
    for i in range(6):
        Jimmy.forward(40)
        Jimmy.left(60)
    Jimmy.end_fill()

    Jimmy.pencolor('magenta')
    Jimmy.fillcolor('magenta')
    Jimmy.goto(50, -25)
    Jimmy.begin_fill()
    for i in range(3):
        Jimmy.forward(60)
        Jimmy.left(120)
    Jimmy.end_fill()

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
