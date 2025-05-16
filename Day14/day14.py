from art import logo
from art import vs
from names import data
import random



length=len(data)

for _ in range(2):
    index1=random.randint(0,length)
    index2=random.randint(0,length)
print(logo)


choice1=data[index1]
choice2=data[index2]

def compare(a_followers,b_followers):
    if a_followers > b_followers:
        return a_followers
    else:
        return b_followers
    
print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
print(vs)
print(f"Compare B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

aorb=int(input("Who haas more followers?? 'A' or 'B'"))

correct_ans=compare(choice1['follower_count'],choice2['follower_count'])
if aorb == correct_ans == True:
    print(f"You are right")
else:
    print("You are wrong")