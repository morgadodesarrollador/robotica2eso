import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

for i in range(15):
    for i in range(4):
        flecha.forward(50)
        flecha.left(90)
    flecha.back(50)
    flecha.left(30)
  
input('acabar...')
