import turtle

shapes = {
        "triangle": [3,180],
        "square": [4,360],
        "pentagon": [5,540],
        "hexagon": [6,720],
        "octagon": [8,1080],
        "nonagon": [9, 1260],
}
turtle.setup(1500,1500)
abdul_turtle = turtle.Turtle()
abdul_turtle.penup()
abdul_turtle.goto(0,0)
abdul_turtle.pendown()
abdul_turtle.speed(1)

def DrawShape( length , shape_drawn , angles_drawn , numberOfShapes, anglesPerShape ):
    for j in range(numberOfShapes):
        for x in range(shapes[shape_drawn][0]):
            abdul_turtle.forward(length)
            #x doesn't need to turn at the end because it got to its final stop
            if x == (shapes[shape_drawn][0])-1:
                break
            else:
                abdul_turtle.left(angles_drawn)
                print("AA2")
                #added it with the old angle because it doesn't start from zero
        abdul_turtle.left(anglesPerShape+angles4shapeBF)
        print("AA1")


user_shape = input("Tell me the name of the shape you want to draw?\n 1)triangle\n 2)square\n 3)pentagon\n 4)hexagon\n 5)octagon\n 6)nonagon\n")
user_shape_length = float(input("Tell me the length of each size?\n"))
user_shapes_in_circle = int(input("Give me the number of shapes you want me to draw in the circle?"))

#to workout the angle depending on the number of shapes
anglesPerShape = 360/user_shapes_in_circle
print(anglesPerShape)
#this line finds the shape angles by checking with the map
#uses the shape input from the user
angles4shapeBF = (shapes[user_shape][1]/shapes[user_shape][0])

#gets the angle takes away from 180 because it starts from a stright line
angles4shape = 180 - angles4shapeBF
print(angles4shape)
DrawShape( user_shape_length , user_shape, angles4shape ,user_shapes_in_circle , anglesPerShape  )
