#Joke Rater
liked_joke = 0
dislike_joke = 0
joke_rater = True
jokes = ['I was wondering why the ball was getting bigger and bigger. Then it hit me.', 'Whats brown and sticky? A Stick!', 'Whats the best thing about Switzerland? I dont know, but the flag is a big plus!', 'what do you call a pig that does karate? a pork chop!', 'Where do you find a dog with no legs? Right where you left them.', 'Did you hear about the guy who cut off the left side of his body? Hes all right now.', 'Why do bicycles fall over? Because the are two tired!', 'What rhymes with orange? No it doesnt.', 'How do you tell if a vampire is sick? By how much he is coffin.', 'What kind of tree fits in your hand? A palm tree!', 'What do you call a boomerang that wont come back? A stick!']
while joke_rater == True:
    from random import randint
    def pick(words):
        num_words = len(words)
        num_picked = randint(0, num_words - 1)
        word_picked = words[num_picked]
        return word_picked
    print(pick(jokes), end='\n')
    print('Was this a good joke?')
    answer = input('y,n')
    if answer == 'y':
        liked_joke = liked_joke + 1
    elif answer == 'n':
        dislike_joke = dislike_joke + 1
    else:
        print('Please enter a valid answer.')
    print('would you like to see the data?')
    data = input('y,n')
    if data == 'y':
        print('This is how many times people liked these jokes')
        print(liked_joke)
        print('this is how many times people disliked these jokes')
        print(dislike_joke)
    elif data == 'n':
        print('Okay!')
    else:
        print('please enter a valid answer.')
    print('would you like to continue?')
    redo = input('y,n')
    if redo == 'y':
        joke_rater = True
    elif redo == 'n':
        joke_rater = False
    else:
        print('please enter a valid answer.')
        joke_rater = True
print('Goodbye!')
