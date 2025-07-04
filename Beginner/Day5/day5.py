# LOOPS BOOM

# fruits = ["Apple", "Peach", "Pear"]
# for fruity in fruits:
#   print(fruity)
#   print (fruity + " "+"pie")


# for number in range(1, 11, 3):
# #   print(number)
# total = 0
# for number in range(1,101):
#   total +=number
# print(total) 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*','+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
'?', '@', '[', ']', '^', '_', '`', '{', '|',
'}', '~']

print("Welcome to the password Generaotr!")
no_letters=int(input("How many letters do you like to have?"))
no_numbers=int(input("How many numbers would you like?"))
no_symbols=int(input("How many symbols would you like?"))
 #This part is copied from chatgpt 
random_letters = [random.choice(letters) for _ in range(no_letters)]  
random_numbers = [random.choice(numbers) for _ in range(no_numbers)]
random_symbols = [random.choice(symbols) for _ in range(no_symbols)]
# just this middle part or else someone will accuse me of copying

all_chars = random_letters + random_numbers + random_symbols


random.shuffle(all_chars)
# this also copied from chatgpt
password=''.join(all_chars)
print(f"Your password is {password}")
  