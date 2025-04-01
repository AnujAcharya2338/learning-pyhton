import random
import hangman_words
from hangman_words import word_list
end_of_game = False
lives = 6
from hangman_art import logo
print(logo)
chosen_word = random.choice(word_list)
leng = len(chosen_word)
display = []
for _ in range(leng):
  display += "_"
print(display)

while not end_of_game:
  guess = input("Guess a letter  \n".lower())
  
  if guess in display:
    print(f"You have already guessed{guess}")
  for position in range(leng):
      letter = chosen_word[position]
      if guess == letter:
        display[position] = letter 
      
  if guess not in chosen_word:
    print(f"You have guessed {guess}, thats not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose")
  print(display) 
  if "_" not in display:
    end_of_game = True
    print("You have won")
 
  from hangman_art import stages
  print(stages[lives])

      
   
    

    
    
