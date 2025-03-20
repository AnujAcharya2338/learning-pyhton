# print("Hello "  + input("What is your name?"))
# name=input("What is your name?")
# print(name)
# name=input("What is your name?")
# length=len(name)
# print(length)
# print("Welcome to the Band Name Generator")
# city = input("What's the name of the city you grow up in?\n")
# pet = input("What's your pet's name?\n")
# print("Your band name could be " + city + " " + pet)
# print("Hello"[4])
# print("123"[1])

# #Interger
# # print(123_999+123)

# #Float
# print(3.14159) 

# #Boolean
# True
# False


# num_char=len(input("What is your name?"))
# new_num_char=str(num_char)
# print("Your name has " +new_num_char + " Characters")

# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
# first=int(two_digit_number[0])
# second=int(two_digit_number[1])
# print(first+second)
# print(3**3)


# height = input()
# weight = input()
# # Your code below this line 👇
# weight_as_int = int(weight)
# height_as_float = float(height)
# # Using the exponent operator **
# bmi = weight_as_int / height_as_float ** 2
# # or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)

# bmi_as_int = int(bmi)
# print(bmi_as_int)

# result = 4/2
# result /=4
# print(result)

# score=0
# height = 1.8
# isWinning = True
# score +=1

# print(f"Your score is {score} , Your height is {height}, You are winning is {isWinning}"  )


print("Welcome to the tip calculator")
total_bill=input("What was the total bill? $")
tip=input("How much tip mould you like to give? 10, 12, 15 ")
people=input("How many people to split the bill?")

tb=float(total_bill)
ti=int(tip)
pe=int(people)

tip_percent=ti/100
total_tip=tb*tip_percent
total_bill=tb+total_tip
bill_per_person=total_bill/pe

final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")




































