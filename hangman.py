import random 


Hangman = [
    '''
    ____
    |   
    |   
    |  
    |  
    _______   
    ''',
    '''
     _____
    |   |
    |   
    |  
    |  
    _______
    ''',
    '''
     _____
    |   |
    |   O
    |  
    |  
    _______
    ''',
    '''
      ____
    |   |
    |   O
    |   |
    |  
    _______
    ''',
    '''
      ____
    |   |
    |   O
    |  /|\
    |  
    _______
    ''',
    '''
      ____
    |   |
    |   O
    |  /|\
    |  / \
    _______
    ''',
    '''
    You Died
    '''
    
]

max_wrong = len(Hangman)
Words = ["armenia","russia","usa","georgia","spain","portugal","france","germany","bulgary","canada","mexico","sweden","italia","ukraine"]
word = random.choice(Words)
so_far_from_word = "-" * len(word)
wrong = 0
used_letters = []

while wrong < max_wrong and so_far_from_word != word:
    print(Hangman[wrong])
    print('You used these letters:', used_letters)
    print("Your word like this:", so_far_from_word)
    
    guess = input("Please enter your letter: ")


    while guess in used_letters:
        print("You already guess this letter:", used_letters)
        guess = input("Please, enter another letter:")
    used_letters.append(guess)


    if guess in word:
        print("Yeah you guess this letter:")
    
        new_far = ""
        for i in range(len(word)):
            if guess == word[i]:
                new_far += guess
            else:
                new_far += so_far_from_word[i]
        so_far_from_word = new_far
        
    else:
        print("It's wrong letter")
        wrong += 1
if wrong == max_wrong:
    
    print("You're looser")
else:
    print("You guess this word")

print("this word is " + word)
