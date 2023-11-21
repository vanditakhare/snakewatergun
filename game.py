import random

def win(a,b):
    if a==b:
        return none
    elif a=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif a=='w':
        if b=='g':
            return False
        elif b=='s':
            return True  
    elif a=='g':
        if b=='s':
            return False
        elif b=='w':
            return True        




a=input("Computer's Turn : Snake(s) Water(w) or Gun(g)??")
randno=random.randint(1,3);
if randno==1:
    a='s';
elif randno==2:
    a='w';   
else:
    a='g';
    

b=input("Your's Turn : Snake(s) Water(w) or Gun(g)??")

w=win(a,b)
if w=='none':
    print("tie")
elif w:
    print("you win")
else:
    print("you lose")
