from art import logo
from art import vs
from names import data
import random

length=len(data)

index1=random.randint(0,length-1)
index2=random.randint(0,length-1)
print(logo)



def compare(a_followers,b_followers):
    if a_followers > b_followers:
        return 'A'
    else:
        return 'B'
    

def inpuut(c1,c2):
    
    print(f"Compare A: {c1['name']}, a {c1['description']}, from {c1['country']}")
    print(vs)
    print(f"Compare B: {c2['name']}, a {c2['description']}, from {c2['country']}")
    


def game():
    game_should_continue = True
    count = 0
    choice1=data[index1]
    choice2=data[index2]
    while choice2 == choice1:
        choice2 = random.choice(data)
    while game_should_continue:
        inpuut(choice1, choice2)
        aorb=input("Who has more followers?? 'A' or 'B'.").strip().upper()
        highest_followers=compare(choice1['follower_count'],choice2['follower_count'])
        
        
        if aorb == highest_followers:
                count +=1
                print(f"You are right! Current score:{count}")  
                choice1 = choice2
                choice2 = random.choice(data)
                while choice2 == choice1:
                    choice2 = random.choice(data)
        else:
                print(f"You are wrong! Total score:{count}")
                game_should_continue = False
game()
