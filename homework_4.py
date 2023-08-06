import turtle
select=int(input("select your shape\n 1=circle 2= square: "))
radius = int(input("radius: "))
t = turtle.Turtle()
if select==1:
    t.circle(radius)
elif select==2:
    t.forward(radius)
    t.left(90)
else:
    print("SentaxeRror")
