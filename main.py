from replit import clear
import random
import ascii_images
import hangman_words

stages = ascii_images.stages
title = ascii_images.title
winner = ascii_images.winner
game_over_image = ascii_images.game_over

chosen_word = random.choice(hangman_words.word_list)


word = []
game_over = False
lives = 6
format_lives = '❤❤❤❤❤❤'
coincidence = False


for _ in chosen_word:
  word += '_'



print(title)


while not game_over and lives > 0:
  
  coincidence = False
  
  guessed_word = input("Quess a letter: ")
  clear()


  
  if guessed_word in word:
    print(f"You've already guessed {guessed_word}\n")
  
  for position in range(len(chosen_word)):
    
      letter = chosen_word[position]
      
      if letter == guessed_word:
        word[position] = letter
        coincidence = True
      
     
  if not '_' in word:
    game_over = True
    print(winner)

  print(f"You've guessed the letter: {guessed_word}\n")
  print(f"{' '.join(word)}\n")

  if not coincidence == True:
    
    lives = lives - 1
    
    if lives == 5: print('oh no! better luck next time!')
    if lives == 4: print('So close!')
    if lives == 3: print('Reallly??')
    if lives == 2: print('OMG..')
    if lives == 1: print("I'm gonna dieee...")

    if lives > 0: print(f"{' '.join(format_lives[:lives])}  = {lives}")
      
    print(f'{stages[lives]}')

    


    coincidence = False
    if lives == 0:

      print(f"the chosen word was: {chosen_word}")
      print(game_over_image)
  


