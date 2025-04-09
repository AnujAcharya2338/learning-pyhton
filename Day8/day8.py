# def great():
#     print("Hello")
#     print("World")
#     print("Office")
    
# great()

# def greet(name):
#     print(f"Hello {name}" )
#     print(f"How you doing {name}")
    
# greet("Anuj")
    
# def great_With(name , address):
#     print(f"Hello {name} \n  What is it like in {address}")
# great_With(name="Anuj",address="Taudaha")    
# great_With(address="Rato-Pul",name="Alisha Baini")  # Write your code below this line 👇
# def prime_checker(number):
#   count =0
#   for prime in range(1,number+1):
#     if number % prime == 0:
#       count +=1
#   if count == 2:
#      print(f"It's a prime number.")
#   else:
#      print(f"It's not a prime number")
# # Write your code above this line 👆
# #Do NOT change any of the code below👇
# n = 13 # Check this number
# prime_checker(number=n)

# ****************************************************

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_a, shift_a):
    encrypted_text =""
    for loop in text_a:
        position = alphabet.index(loop)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encrypted_text += new_letter
    print(f"The encoded text is {encrypted_text}")
encrypt(text_a=text, shift_a=shift)
