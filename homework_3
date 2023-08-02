import time
import math

def add(n1,n2):
    print("add:",n1+n2)
    time.sleep(1.5)

def min(n1,n2):
    print("min:",n1-n2)
    time.sleep(1.5)

def multiply(n1,n2):
    print("multiply:",n1*n2)
    time.sleep(1.5)

def divide(n1,n2):
    if n2<=0:
        print("SyntaxError")
    else:
        print("divide::",n1/n2)
    time.sleep(1.5)

def Exclamation_mark(n1,n2):
        print("factorial for n1:",math.factorial(n1))
        print("factorial for n2:",math.factorial(n2))
        time.sleep(1.5)
        
def sqrt(n1,n2):
	print("sqrt for n1:",math.sqrt(n1))
	print("sqrt for n2:",math.sqrt(n2))
	time.sleep(1.5)
			
n1=int(input("enter num1: "))
operation=input("math:")
n2=int(input("enter num2: "))

if operation=="+":
    add(n1,n2)
elif operation=="-":
    min(n1,n2)
elif operation=="*":
    multiply(n1,n2)
elif operation=="/":
    divide(n1,n2)
elif operation=="!":
    Exclamation_mark(n1,n2)
elif operation=="sqrt":
    sqrt(n1,n2)
else:
    print("SyntaxError")
