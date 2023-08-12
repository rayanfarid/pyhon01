import turtle
import random
select=int(input("select your shape\n 1.circle \n2.square \n3.triangle \n4.random shape\nEnter here: "))
radius = int(input("radius: "))
color=input("Enter color shape: ")
t = turtle.Turtle()
def s1():
    t.circle(radius)
    t.color(color)
def s2():
    for f in range(4):
         t.forward(radius)
         t.left(90)
         t.color(color)
def s3():
    t.forward(radius)
    t.left(120)
    t.forward(radius+radius/2)
    t.left(120)
    t.forward(radius)
s3=s3()
s2=s2()
s1=s1()
def s4():
    randoms=random.choice(s1,s2,s3)
    print(randoms)

if select==1:
    t.circle(radius)
elif select==2:
   s2()
elif select==3:
    s3()
elif select==4:
    s4()
else:
    print("SentaxError")
turtle.done