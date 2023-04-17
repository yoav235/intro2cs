import turtle

#################################################################
# FILE : hello_turtle.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: A simple program that draws a flower bed
# STUDENTS I DISCUSSED THE EXERCISE WITH: yonatan levi.
# WEB PAGES I USED: https://www.google.com/search?client=firefox-b-d&q=basic+function+in+turtle+python
# NOTES: ...
#################################################################




# this function draws the petals of the flower
def draw_petal():
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


# draws a single flower
def draw_flower():
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()
