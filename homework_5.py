import turtle
from termcolor import colored 
def q_1():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title", "1. Which of the following most closely describes your personality?\nA.Energetic and forceful\nB.Thoughtful and considerate\nC.Healthy and friendly\nD.Sociable and people person\nE.Caring and helpful\nF.Spiritual and humble\nG.Tender and sympathetic\n".lower())
def q_2():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title", "2. This statement fits you:\na) I anger easily.\nb) I like physical activities.\nc) I dislike rules.\nd) I communicate easily.\ne) I love to help others.\nf) I daydream.\ng) I enjoy learning new things.\n".lower())
def q_3():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title","3. You would describe yourself as:\na) A loner\nb) A risk-taker\nc) Spontaneous\nd) A nature lover\ne) A good listener\nf) A visionary\ng) Extremely sensitive\n".lower())
def q_4():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title","4. Overall, you are:\na) Realistic\nb) Confident\nc) Optimistic\nd) Outgoing\ne) Intuitive\nf) Curious\ng) Idealistic\n".lower())
def q_5():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title", "5. Others say you are:\na) Well-grounded\nb) Brave\nc) Creative\nd) Love-centered\ne) Highly spiritual\nf) Imaginative\ng) Independent\n".lower())
def q_6():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title","6. Which of the following is your favorite?\na) Flowers\nb) Chocolate\nc) Shoes\nd) Rings, Earrings\ne) Home Furnishings\nf) Makeup\ng) Candlelight Dinner\n".lower())
def q_7():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title","7. You think of yourself as:\na) Tenacious\nb) Strongly motivated\nc) Focused on a plan of action\nd) A person with a benevolent character\ne) A person with well-developed instincts\nf) A modest individual\ng) A person who remembers her dreams\n".lower())
def q_8():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title", "8. If you weren’t feeling well, what would be your most common ailment?\na) Nervous, anxiety\nb) Body aches from over-exertion\nc) Stomach\nd) Short of breath\ne) Sore throat\nf) Watery or dry eyes\ng) Headache\n".lower())
def q_9():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title", "9. In the workplace, you:\na) Work hard as a team player\nb) Prefer a challenge\nc) Like to work with your hands\nd) Strive to complete tasks flawlessly\ne) Feel guilty if you have to say, “no”\nf) Feel your appearance takes precedence\ng) Frequently end up in a leadership position\n".lower())
def q_10():
    sc = turtle.Screen()
    sc.setup(400, 300)
    return turtle.textinput("title","10. An overall statement about yourself:\na) I am sometimes blunt, but only because I wish to be honest.\nb) I love adventure and thrilling activities, even if they’re a little dangerous.\nc) Activities like dancing and exercise can be fun. Actually, they are my favorites.\nd) I am an organized person who loves to be intellectually stimulated.\ne) Material possessions are not my priority.\nf) I sometimes feel like a fish out of water, especially in a large group.\ng) The environment is a major concern of mine.\n".lower())
w={
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0
}
list_of_answers=[]
v1="z"
while v1!="a" and v1!="b" and v1!="c" and v1!="d" and v1!="e" and v1!="f" and v1!="g":
    v1=q_1()
    if v1!="a" and v1!="b" and v1!="c" and v1!="d" and v1!="e" and v1!="f" and v1!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v1)
v2="z"
while v2!="a" and v2!="b" and v2!="c" and v2!="d" and v2!="e" and v2!="f" and v2!="g":
    v2=q_2()
    if v2!="a" and v2!="b" and v2!="c" and v2!="d" and v2!="e" and v2!="f" and v2!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v2)
v3="z"
while v3!="a" and v3!="b" and v3!="c" and v3!="d" and v3!="e" and v3!="f" and v3!="g":
    v3=q_3()
    if v3!="a" and v3!="b" and v3!="c" and v3!="d" and v3!="e" and v3!="f" and v3!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v3)
v4="z"
while v4!="a" and v4!="b" and v4!="c" and v4!="d" and v4!="e" and v4!="f" and v4!="g":
    v4=q_4()
    if v4!="a" and v4!="b" and v4!="c" and v4!="d" and v4!="e" and v4!="f" and v4!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v4)
v5="z"
while v5!="a" and v5!="b" and v5!="c" and v5!="d" and v5!="e" and v5!="f" and v5!="g":
    v5=q_5()
    if v5!="a" and v5!="b" and v5!="c" and v5!="d" and v5!="e" and v5!="f" and v5!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v5)
v6="z"
while v6!="a" and v6!="b" and v6!="c" and v6!="d" and v6!="e" and v6!="f" and v6!="g":
    v6=q_6()
    if v6!="a" and v6!="b" and v6!="c" and v6!="d" and v6!="e" and v6!="f" and v6!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v6)
v7="z"
while v7!="a" and v7!="b" and v7!="c" and v7!="d" and v7!="e" and v7!="f" and v7!="g":
    v7=q_7().lower()
    if v7!="a" and v7!="b" and v7!="c" and v7!="d" and v7!="e" and v7!="f" and v7!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v7)
v8="z"
while v8!="a" and v8!="b" and v8!="c" and v8!="d" and v8!="e" and v8!="f" and v8!="g":
    v8=q_8()
    if v8!="a" and v8!="b" and v8!="c" and v8!="d" and v8!="e" and v8!="f" and v8!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v8)
v9="z"
while v9!="a" and v9!="b" and v9!="c" and v9!="d" and v9!="e" and v9!="f" and v9!="g":
    v9=q_9()
    if v9!="a" and v9!="b" and v9!="c" and v9!="d" and v9!="e" and v9!="f" and v9!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v9)
v10="z"
while v10!="a" and v10!="b" and v10!="c" and v10!="d" and v10!="e" and v10!="f" and v10!="g":
    v10=q_10()
    if v10!="a" and v10!="b" and v10!="c" and v10!="d" and v10!="e" and v10!="f" and v10!="g":
        print(colored("the answer is not avalable","red"))
list_of_answers.append(v10)     
for q1 in list_of_answers: 
    w[q1]=w[q1]+1
    #print(q1)
    #print(w)
#print(w)
turtle.shape('circle')
turtle.turtlesize(.01)
print("========================================================================================================")
if w["a"]>w["b"] and w["a"]>w["c"] and w["a"]>w["d"] and w["a"]>w["e"] and w["a"]>w["f"] and w["a"]>w["g"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly red.\nRed: Strong-willed, straightforward, energetic, forceful, well-\ngrounded, hard worker, team player, active, competitive, realistic,\n impulsive and overwhelmed by change. If a health issue arises, it\nwill be due to anxiety.")
elif w["b"]>w["a"] and w["b"]>w["c"] and w["b"]>w["d"] and w["b"]>w["e"] and w["b"]>w["f"] and w["b"]>w["g"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly orange./nOrange: Courageous, adventurous, thoughtful, considerate, self-\nassured, detail-oriented, and sometimes a lack in self-discipline.\nHealth issues usually stem from the kidney or reproductive organs.","green")
elif w["c"]>w["a"] and w["c"]>w["b"] and w["c"]>w["d"] and w["c"]>w["e"] and w["c"]>w["f"] and w["c"]>w["g"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly yellow./nYellow: Laid-back, playful, creative, friendly, optimistic, avoids\nconflict, feelings are easily hurt, timid and mental alertness. Health\nissues relate to the spleen.","green")
elif w["d"]>w["a"] and w["d"]>w["b"] and w["d"]>w["c"] and w["d"]>w["e"] and w["d"]>w["f"] and w["d"]>w["g"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly green./nGreen: Social, love people, animals and nature, good\ncommunicator, perfectionist, quick-witted, organizer, impatient,\ntrustworthy, nurturing. Lungs are the indicated health issue.","green")
elif w["e"]>w["a"] and w["e"]>w["b"] and w["e"]>w["c"] and w["e"]>w["d"] and w["e"]>w["f"] and w["e"]>w["g"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly blue./nBlue: Helpful, caring, spiritual, intuitive, generally at peace and\ncontent, understanding, peacemaker, steadfast, freethinker. Some\nbelieve that problems a person with this aura color may\nexperience relates to the throat or thyroid.","green")
elif w["f"]>w["a"] and w["f"]>w["b"] and w["f"]>w["c"] and w["f"]>w["d"] and w["f"]>w["e"] and w["f"]>w["g"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly indigo./nIndigo: Imaginative, daydreamer, curious, deep inner feelings,\nsometimes lacks self-esteem, gentle, unassuming, introvert, calm\nand modest. The eyes are the concern for indigo-aura people.","green")
elif w["g"]>w["a"] and w["g"]>w["b"] and w["g"]>w["c"] and w["g"]>w["d"] and w["g"]>w["e"] and w["g"]>w["f"]:
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.write("Your aura is predominantly violet./nViolet: Idealistic, most sensitive and wisest of the colors, a seeker\nof truth, independent, intellectual, extroverted and authoritative.\nSometimes people with a violet aura color have psychic power.\nViolet relates to the pineal gland and nervous system.","green")
else:
    all_difs={}
    all_difs["a"]=colored("Red: Strong-willed, straightforward, energetic, forceful, well-\ngrounded, hard worker, team player, active, competitive, realistic,\n impulsive and overwhelmed by change. If a health issue arises, it\nwill be due to anxiety.","green")
    all_difs["b"]=colored("Orange: Courageous, adventurous, thoughtful, considerate, self-\nassured, detail-oriented, and sometimes a lack in self-discipline.\nHealth issues usually stem from the kidney or reproductive organs.","green")
    all_difs["c"]=colored("Yellow: Laid-back, playful, creative, friendly, optimistic, avoids\nconflict, feelings are easily hurt, timid and mental alertness. Health\nissues relate to the spleen.","green")
    all_difs["d"]=colored("Green: Social, love people, animals and nature, good\ncommunicator, perfectionist, quick-witted, organizer, impatient,\ntrustworthy, nurturing. Lungs are the indicated health issue.","green")
    all_difs["e"]=colored("Blue: Helpful, caring, spiritual, intuitive, generally at peace and\ncontent, understanding, peacemaker, steadfast, freethinker. Some\nbelieve that problems a person with this aura color may\nexperience relates to the throat or thyroid.","green")
    all_difs["f"]=colored("Indigo: Imaginative, daydreamer, curious, deep inner feelings,\nsometimes lacks self-esteem, gentle, unassuming, introvert, calm\nand modest. The eyes are the concern for indigo-aura people.","green")
    all_difs["g"]=colored("Violet: Idealistic, most sensitive and wisest of the colors, a seeker\nof truth, independent, intellectual, extroverted and authoritative.\nSometimes people with a violet aura color have psychic power.\nViolet relates to the pineal gland and nervous system.","green")

    turtle.write("your answers are evenly divided between two or three colors, this means your aura color fluctuates between those particular colors, or you may always have a combination of those colors in your aura.")
    one_of_equal=(list(dict(sorted(w.items(), key=lambda item: item[1])).values())[-1])
    for k in w.keys():
        if w[k]==one_of_equal:
            print(all_difs[k])
            print("===========================================================================\n")
turtle.done()
