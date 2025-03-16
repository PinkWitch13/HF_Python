import sys

word = " "
passed_letters = []

def hangman_logic(word):
    print("Welcome to hangman!")
    while word == True:
        hidden_word = ("_ ") * (len(word)).casefold()
        hidden_word = list(hidden_word)
        print(f"The hidden word is: {hidden_word}")
        print("Find letter: ")
        user_input = take_input_from_user()

        hangman_turn(word, user_input, hidden_word)

def take_input_from_user() -> str:
    """Function conwerting user input string."""
    user_letter = input("Please provide a letter to find: ").casefold()
    return user_letter

def hangman_turn(word, user_letter, hidden_word):
    """Function describing succesively each round of the game."""
    counter = 0
    global passed_letters
    passed_letters.append(user_letter)
    for i, user_letter in enumerate(word):
        letter_index.ap(i)
        counter +=1
        if user_letter not in word:
            print(f"No hits found for {user_letter} in round {counter}")
            print(f"The hidden word is: {hidden_word}")
        else:
            return hidden_word_switcher(user_letter, 
                                        letter_index, 
                                        hidden_word, 
                                        word)
                 
def hidden_word_switcher(user_letter, hidden_word, 
                             word) -> str:
    """Function reveal user_letter in hidden_word 
       after each match."""
    
    index = []
    for i, user_letter in enumerate(word):
        hidden_word = list(hidden_word)
        index.append(i)
        del hidden_word[i]
        hidden_word.insert(i, user_letter)
        str("".join(hidden_word))
        print(f"the hidden word is: {hidden_word=}")

 
        
    

            
        # TO-DO find i dynamically based on word and user_letter
        # TO-DO create list based on word
        # TO-DO create list based on hidden_word
        # TO-DO rep;lace char on index i in word with _
        # TO-DO replace char on index i in hidden word with user_letter

    #     print(f"2. {hidden_word=}")
    #     hidden_word.insert(i, user_letter)
    #     print(f"3. {hidden_word=}")
    #     hidden_word = "".join(hidden_word)
    #     print(f"4. {hidden_word=}")
    #     hidden_word = hidden_word.casefold()
    #     print(f"the hidden word is: {hidden_word}")
    # print(f"Congratulations - the word is {hidden_word}. VICTORY!!!")
    # TO-DO create string from hidden_word and return it


# def ____hangman_logic(word, letter):
#     word_to_find, word = list(word), str(word)
#     past_letters.append(letter)
#     print(f"{past_letters=}")
#     round = 0
#     matched_letters = []
#     matched_indexes = list()
#     w_len = len(word)
#     for each_element in past_letters:
#         round +=1
#         for w_letter in word_to_find:
#             w_len =- 1
#             print(f"{w_len=}")
#             if each_element == w_letter:
#                 matched_letters += each_element
#                 print("MATCH!")
#                 letter_index = word.find(each_element)
#                 print(f"{letter_index=}")
#                 matched_indexes.append(letter_index)
#                 letter_index = str(letter_index)
#                 print(f"{matched_indexes=}")
#                 hidden_word = hidden_word_switcher(each_element, letter_index)
#                 print(f"{hidden_word=}")
#                 return hidden_word
#             elif each_element != w_letter:
#                 return "NO MATCH!"
#             elif w_len == 0:
#                     print("VICTORY!!! Rounds played: ",round) 
#     print(f"{word=}")
#     print()
#     print(f"{round=}")
#     return "string NO MATCH!"        

# hidden_word = ("_") * len(word)
# print(hidden_word)


if __name__ == "__main__":
    # TO-DO: take input from sys.argv, validate it and pass to hangman_logic
    hangman_logic("foo")