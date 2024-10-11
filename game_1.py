import random

def Define_winner(player,computer):
   

    plydct={"rock":1,"paper":-1,"scissors":0}
    compdct={1:"rock",-1:"paper",0:"scissors"}

    if player not in plydct:
        return "invalid input"

    ply_value=plydct[player]
    comp_value=compdct[computer]
    print("coumputer choice: ", comp_value)

    if ply_value==computer:
        return "its a tie"
    elif  (ply_value==-1 and computer==0) or(ply_value==1 and computer==-1) or(ply_value==0 and computer==-1):
        return ("you lose")
    else:
        return ("you win")
      

while True:

    player=input("enter your choice(rock,paper,scissors): ")
    computer=random.choice([-1, 1, 0])

    print(Define_winner(player,computer))

    r=input("Do you want to play again (yes/no): ")
    if  r!= "yes":
         print("thanks for playing")
         break