import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)
chosen_list1 = chosen_list.copy()
word_length = len(chosen_word)
lives = 4

print(' Psst, correct word is', chosen_word)

user_list = ['_'] * word_length
print(user_list)

chosen_letter = ''
while chosen_list != user_list:
    chosen_letter = input('Choose a alphabet from A to Z:')
    if len(chosen_letter) != 1:
        print('Dumbass, wrong input. Try again!')
        break

    if chosen_letter not in chosen_list1:
        lives -= 1
        print('Wrong guess, You have {} lives left'.format(lives))
        if lives == 0:
            print('Sorry, But your hangman was hanged. Game Over!')
            break
    
    while chosen_letter in chosen_list1:
        index = chosen_list1.index(chosen_letter)
        user_list[index] = chosen_letter
        chosen_list1[index] = "_"
        print(user_list)

if chosen_list == user_list:
    print("Hooray!, you guessed the word","".join(user_list),'correctly')
