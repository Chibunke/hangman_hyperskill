__author__ = 'Victor E'
print('H A N G M A N')
while True:
    users_choice = input('Type "play" to play the game, "exit" to quit:')

    if users_choice == 'play':
        print('')
        list_ = ['python', 'java', 'javascript', 'kotlin']
        guessed_word = list()
        import random

        word = random.choice(list_)
        word_gap = "-" * len(word[0:])
        print(word_gap)
        trail = 8
        while trail > 0:
            input_ = input('Input a letter:')
            # this is to check the number of words inputted
            input_list = len(list(input_))
            if input_list != 1:
                print('You should input a single letter\n')
                print("".join(word_gap))
            else:

                for i in input_:
                   # this is to check lowercase
                    if i.islower():

                        if i in input_ not in word:
                            if i in guessed_word:
                                print('You already typed this letter\n')
                                print("".join(word_gap))
                            else:
                                guessed_word.append(i)
                                if trail == 1:
                                    trail -= 1
                                    print("No such letter in the word")
                                    break
                                else:
                                    trail -= 1
                                    print("No such letter in the word\n")
                                    print("".join(word_gap))

                        elif i in input_ in word:
                            if i in guessed_word:

                                print('You already typed this letter\n')
                                print("".join(word_gap))
                            else:
                                guessed_word.append(i)
                                word_gap = list(word_gap)
                                index_i = word.find(i)
                                word_gap[index_i] = i
                                count_i = word.count(i)
                                n = 1  # n represents the number of i to be found
                                while count_i > 1:
                                    n += 1
                                    c = word.find(i, n)
                                    word_gap[c] = i
                                    count_i -= 1
                                print("")
                                print("".join(word_gap))
                    else:
                        print('It is not an ASCII lowercase letter\n')
                        print("".join(word_gap))

        if word == ("".join(word_gap)):
            print('You guessed the word!')
            print('You survived!')
        else:
            print('You are hanged!')


    elif users_choice == 'exit':
        break
    else:
        continue

