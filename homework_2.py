import random
while True:
    x="welcome"
    v=random.choice("q""w""e""r""t""y""u""i""o""p""a""s""d""f""g""h""j""k""l""z""x""c""v""b""n""m")
    choice=str(input("enter your choice: "))
    print(v)
    if choice==v:
        print("correct")
        break
    elif choice!=v:
        print("incorrect")
