import random
n=2
user_score=0
comp_score=0
while True:
    user=input("choose rock , paper or scissors")
    l=["rock","paper","scissor"]
    comp=random.choice(l)
    print("computer's choice is:",comp)
    if user=="rock" and comp=="paper":
        comp_score+=1
        print("computer wins")
    elif user=="rock" and comp=="scissor":
        user_score+=1
        print("user wins")
    elif user=="scissor" and comp=="rock":
        print("computer wins")
        comp_score+=1
    elif user=="scissor" and comp=="paper":
        user_score+=1
        print("user wins")
    elif user=="paper" and comp=="scissor":
        comp_score+=1
        print("computer wins")
    elif user=="paper" and comp=="rock":
        user_score+=1
        print("user wins")
    elif user==comp:
        print("it is a tie")
    else:
        print("invalid input")
    ask=input("Do you want to play another round?")
    if ask!="yes":
        break
print("user_score is: ",user_score)
print("comp_score: ",comp_score)

            
    

    
        


