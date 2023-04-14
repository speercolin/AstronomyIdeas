# Importing necessary librarie(s)
import turtle

# Creating the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.bgpic("space_background.gif")
screen.setup(width=800, height=600)
screen.title("Our Solar System")

# Defining the Turtle pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Disclaimer notice/information
pen.goto(-700, 325)
pen.color("#EE82EE")
pen.write("Welcome to our Solar System!", font=("PLAYFAIR", 20, "bold"), align="left")
pen.goto(-700, 300)
pen.write("Be aware that these planets are not to scale.", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on our Sun
pen.goto(-700, 250)
pen.color("#FDB813")
pen.write("The Sun", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Mercury
pen.goto(-700, 225)
pen.color("#E5E5E5")
pen.write("Mercury", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Venus
pen.goto(-700, 200)
pen.color("#EED0B4")
pen.write("Venus", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Earth
pen.goto(-700, 175)
pen.color("#6B93D6")
pen.write("Earth", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Earth's Moon
pen.goto(-700, 150)
pen.color("#F6F1D5")
pen.write("Earth's Moon", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Mars
pen.goto(-700, 125)
pen.color("#BC2732")
pen.write("Mars", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Jupiter
pen.goto(-700, 100)
pen.color("#BCAFB2")
pen.write("Jupiter", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Jupiter's Great Red Spot
pen.goto(-700, 75)
pen.color("#8B3F49")
pen.write("Jupiter's Great Red Spot", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Saturn
pen.goto(-700, 50)
pen.color("#DBB57C")
pen.write("Saturn", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Saturn's Rings
pen.goto(-700, 25)
pen.color("#FFC594")
pen.write("Rings of Saturn", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Uranus
pen.goto(-700, 0)
pen.color("#E1EEEE")
pen.write("Uranus", font=("PLAYFAIR", 15, "bold"), align="left")

# Side information key on Neptune
pen.goto(-700, -25)
pen.color("#4B70DD")
pen.write("Neptune", font=("PLAYFAIR", 15, "bold"), align="left")

# About information
pen.goto(-700, -350)
pen.color("#EE82EE")
pen.write("Built by Colin Speer using Python Turtle", font=("PLAYFAIR", 10, "bold"), align="left")

# Creating our Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(stretch_len=8, stretch_wid=8)
sun.color("#FDB813")
sun.penup()
sun.goto(300, 0)

# Creating Mercury
mercury = turtle.Turtle()
mercury.shape("circle")
mercury.shapesize(stretch_wid=1.2, stretch_len=1.2)
mercury.color("#E5E5E5")
mercury.penup()
mercury.goto(300, -105)
mercury.pensize(5)
mercury.pendown()

# Creating Venus
venus = turtle.Turtle()
venus.shape("circle")
venus.shapesize(stretch_wid=1.5, stretch_len=1.5)
venus.color("#EED0B4")
venus.penup()
venus.goto(420, -95)
venus.pensize(5)
venus.pendown()

# Creating Earth
earth = turtle.Turtle()
earth.shape("circle")
earth.shapesize(stretch_wid=2, stretch_len=2)
earth.color("#6B93D6")
earth.penup()
earth.goto(500, 20)
earth.pensize(5)
earth.pendown()

# Creating our Moon
moon = turtle.Turtle()
moon.shape("circle")
moon.shapesize(stretch_wid=0.5, stretch_len=0.5)
moon.color("#F6F1D5")
moon.penup()
moon.goto(earth.xcor(), earth.ycor())
moon.fd(35)

# Creating Mars
mars = turtle.Turtle()
mars.shape("circle")
mars.shapesize(stretch_wid=1.3, stretch_len=1.3)
mars.color("#BC2732")
mars.penup()
mars.goto(480, 175)
mars.pensize(5)
mars.pendown()

# Creating Jupiter
jupiter = turtle.Turtle()
jupiter.shape("circle")
jupiter.shapesize(stretch_wid=3.5, stretch_len=3.5)
jupiter.color("#BCAFB2")
jupiter.penup()
jupiter.goto(300, 305)
jupiter.pensize(5)
jupiter.pendown()

# Creating Jupiter's Great Red Spot
red_spot = turtle.Turtle()
red_spot.shape("circle")
red_spot.shapesize(stretch_wid=0.8, stretch_len=0.8)
red_spot.color("#8B3F49")
red_spot.penup()
red_spot.goto(285, 300)

# Creating Saturn
saturn = turtle.Turtle()
saturn.shape("circle")
saturn.shapesize(stretch_wid=3, stretch_len=3)
saturn.color("#DBB57C")
saturn.penup()
saturn.goto(45, 255)
saturn.pensize(5)
saturn.pendown()

# Creating Rings of Saturn
rings = turtle.Turtle()
rings.hideturtle()
rings.color("#FFC594")
rings.penup()
rings.goto(45, 213)
rings.pensize(4)
rings.pendown()
rings.circle(42)

# Creating Uranus
uranus = turtle.Turtle()
uranus.shape("circle")
uranus.shapesize(stretch_wid=2.6, stretch_len=2.6)
uranus.color("#E1EEEE")
uranus.penup()
uranus.goto(-150, 0)
uranus.pensize(5)
uranus.pendown()

# Creating Neptune
neptune = turtle.Turtle()
neptune.shape("circle")
neptune.shapesize(stretch_wid=2.3, stretch_len=2.3)
neptune.color("#4B70DD")
neptune.penup()
neptune.goto(-50, -325)
neptune.pensize(5)
neptune.pendown()

# Defining starting direction of each planet
mercury.setheading(0)
venus.setheading(45)
earth.setheading(90)
mars.setheading(135)
jupiter.setheading(180)
red_spot.setheading(180)
saturn.setheading(225)
uranus.setheading(270)
neptune.setheading(315)

# Defining animation speed
screen.tracer(10)


# Orbits function
def orbits():
    # Mercury orbit
    mercury.fd(5)
    mercury.lt(2.4)

    # Venus orbit
    venus.fd(5)
    venus.lt(1.8)

    # Earth orbit
    earth.fd(5)
    earth.lt(1.4)

    # Moon orbit
    moon.goto(earth.xcor(), earth.ycor())
    moon.fd(35)
    moon.rt(5)

    # Mars orbit
    mars.fd(5)
    mars.lt(1.1)

    # Jupiter orbit
    jupiter.fd(5)
    jupiter.lt(0.9)

    # Great Red Spot orbit on Jupiter (stay attached)
    red_spot.fd(5)
    red_spot.lt(0.9)

    # Saturn orbit
    saturn.fd(5)
    saturn.lt(0.76)

    # Uranus orbit
    uranus.fd(5)
    uranus.lt(0.67)

    # Neptune orbit
    neptune.fd(5)
    neptune.lt(0.61)


running = True
while running:
    # Calling function(s)
    orbits()

    # Updating location of the Rings of Saturn
    rings.clear()
    rings.goto(saturn.xcor() - 1, saturn.ycor() - 45)
    rings.circle(42)
    screen.update()

# Screen to stay open
screen.mainloop()
