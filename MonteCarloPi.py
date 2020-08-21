#! /usr/bin/python

import turtle
import random
import math


def monteCarloPi(numdarts: int):
    """
    Runs a Monte Carlos simulation to visualize the estimation of pi.

    :param numdarts = number of darts to throw.
    """

    def drawCircle(t, radius):
        """Make turtle t draw a circle of radius."""

        def drawPolygon(t, sideLength, numSides):
            """Make turtle t draw a polygon of numSides."""
            turn = 360 / numSides
            for i in range(numSides):
                t.forward(sideLength)
                t.right(turn)

        circumference = 2 * 3.1415 * radius
        side_length = circumference / 360
        drawPolygon(t, side_length, 360)

    # Initialize the window
    wn = turtle.Screen()
    wn.title('Monte Carlo Simulation for Pi')
    wn.bgcolor('black')
    wn.setup(800, 800, 0, 0)
    wn.tracer(100)
    wn.setworldcoordinates(-1, -1, 1, 1)

    # Create turtle named Fred
    fred = turtle.Turtle()
    fred.pencolor('white')
    fred.fillcolor('white')
    fred.ht()

    # Draw grid for visualization
    points = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i, j in points:
        fred.goto(i, j)
        fred.home()

    # Draw a circle for visualization
    fred.goto(0, 1)
    drawCircle(fred, 1)

    # Lift pen up so just dots will show
    fred.up()

    insideCount = 0
    for i in range(numdarts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        fred.home()
        fred.goto(x, y)
        xySquare = (x ** 2) + (y ** 2)
        if xySquare <= 1:
            insideCount += 1
            fred.dot(5, 'red')
        else:
            fred.dot(5, 'blue')

    montePi = 4 * (insideCount / numdarts)
    print('Estimated pi value: ' + str('%.15f' % montePi))
    print('Actual value of pi: ' + str(math.pi))
    wn.exitonclick()


monteCarloPi(15000)
