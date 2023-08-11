from termcolor import colored
def q_1():
    return input("1. Which of the following most closely describes your personality?\nA.Energetic and forceful\nB.Thoughtful and considerate\nC.Healthy and friendly\nD.Sociable and people person\nE.Caring and helpful\nF.Spiritual and humble\nG.Tender and sympathetic\n")
def q_2():
    return input("2. This statement fits you:\na) I anger easily.\nb) I like physical activities.\nc) I dislike rules.\nd) I communicate easily.\ne) I love to help others.\nf) I daydream.\ng) I enjoy learning new things.\n")
def q_3():
    return input("3. You would describe yourself as:\na) A loner\nb) A risk-taker\nc) Spontaneous\nd) A nature lover\ne) A good listener\nf) A visionary\ng) Extremely sensitive\n")
def q_4():
    return input("4. Overall, you are:\na) Realistic\nb) Confident\nc) Optimistic\nd) Outgoing\ne) Intuitive\nf) Curious\ng) Idealistic\n")
def q_5():
    return input("5. Others say you are:\na) Well-grounded\nb) Brave\nc) Creative\nd) Love-centered\ne) Highly spiritual\nf) Imaginative\ng) Independent\n")
def q_6():
    return input("6. Which of the following is your favorite?\na) Flowers\nb) Chocolate\nc) Shoes\nd) Rings, Earrings\ne) Home Furnishings\nf) Makeup\ng) Candlelight Dinner\n")
def q_7():
    return input("7. You think of yourself as:\na) Tenacious\nb) Strongly motivated\nc) Focused on a plan of action\nd) A person with a benevolent character\ne) A person with well-developed instincts\nf) A modest individual\ng) A person who remembers her dreams\n")
def q_8():
    return input("8. If you weren’t feeling well, what would be your most common ailment?\na) Nervous, anxiety\nb) Body aches from over-exertion\nc) Stomach\nd) Short of breath\ne) Sore throat\nf) Watery or dry eyes\ng) Headache\n")
def q_9():
    return input("9. In the workplace, you:\na) Work hard as a team player\nb) Prefer a challenge\nc) Like to work with your hands\nd) Strive to complete tasks flawlessly\ne) Feel guilty if you have to say, “no”\nf) Feel your appearance takes precedence\ng) Frequently end up in a leadership position\n")
def q_10():
    return input("10. An overall statement about yourself:\na) I am sometimes blunt, but only because I wish to be honest.\nb) I love adventure and thrilling activities, even if they’re a little dangerous.\nc) Activities like dancing and exercise can be fun. Actually, they are my favorites.\nd) I am an organized person who loves to be intellectually stimulated.\ne) Material possessions are not my priority.\nf) I sometimes feel like a fish out of water, especially in a large group.\ng) The environment is a major concern of mine.\n")

a=0
b=0 
c=0 
d=0 
e=0 
f=0 
g=0

list_of_answers=[]
v1="z"
while v1!="a" or v1!="A" or v1!="b" or v1!="B" or v1!="c" or v1!="C" or v1!="d" or v1!="D" or v1!="e" or v1!="E" or v1!="f" or v1!="F" or v1!="g" or v1!="G":
    v1=q_1()
    
    print(colored("the answer is not avalable","red"))
   
list_of_answers.append(v1)
v2=q_2()
list_of_answers.append(v2)
q3=q_3()
list_of_answers.append(q3)
q4=q_4()
list_of_answers.append(q4)
q5=q_5()
list_of_answers.append(q5)
q6=q_6()
list_of_answers.append(q6)
q7=q_7()
list_of_answers.append(q7)
q8=q_8()
list_of_answers.append(q8)
q9=q_9()
list_of_answers.append(q9)
q10=q_10()
list_of_answers.append(q10)    
for q1 in list_of_answers:
        print(q1)
        if q1=="A" or q1=="a":
            a=a+1
        elif q1=="B" or q1=="b":
            b=b+1
        elif q1=="C" or q1=="c":
            c=c+1
        elif q1=="D" or q1=="d":
            d=d+1
        elif q1=="E" or q1=="e":
            e=e+1
        elif q1=="F" or q1=="f":
            f=f+1
        elif q1=="G" or q1=="g":
            g=g+1

print(a,b,c,d,e,f,g)