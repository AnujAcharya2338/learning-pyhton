from art import logo
from art import vs
from names import data
import random

length=len(data)

count = 0
game_end = False
index1=random.randint(0,length-1)
index2=random.randint(0,length-1)
print(logo)

choice1=data[index1]
choice2=data[index2]

def compare(a_followers,b_followers):
    if a_followers > b_followers:
        return 'A'
    else:
        return 'B'
    
print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
print(vs)
print(f"Compare B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

aorb=input("Who has more followers?? 'A' or 'B'.").strip().upper()

correct_ans=compare(choice1['follower_count'],choice2['follower_count'])

if aorb == correct_ans:
    print(f"You are right")  
    count +=1
else:
    print("You are wrong")