name= input('enter your name: ')
print( 'welcome ', name)

total_correct=0
total_incorrect=0

y=int(input("numper of works experiance in years: "))
if y>=3:
    print("correct")
    total_correct=total_correct+1
else:
    print("incorrect")
    total_incorrect=total_incorrect+1
q1=input("type of 9.5:")
if q1=="float":
    print("correct")
    total_correct=total_correct+1
else:
    print("incorrect")
    total_incorrect=total_incorrect+1
q2=input("type of \"100\":")
if q2== "string" or "str":
    print("correct")
    total_correct=total_correct+1
else:
    print("incorrect")
    total_incorrect=total_incorrect+1    
q3=input("is this command true \n print(hi):")
if q3=="no":
    print("correct")
    total_correct=total_correct+1
else:
    print("Incorrect")
    total_incorrect=total_incorrect+1    
q4=input( "do you have an certificate: ")
if q4=="yes":
    print("correct")
    total_correct=total_correct+1
else:
    print("incorrect")
    total_incorrect=total_incorrect+1    


print("total correct:", total_correct)    
print("total incorrect:", total_incorrect)    
