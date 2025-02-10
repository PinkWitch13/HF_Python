import sys

def hangman_logic(word):
    print("Welcome to hangman!")

    while True:
        print("Find letter: ")

        user_input = take_input_from_user()

        hangman_turn(word, user_input)

def take_input_from_user() -> str:
    user_letter = input("Find letter: ")
    user_letter.casefold()
    return user_letter

def hangman_turn(word, user_letter):
    counter = 0
    passed_l = []
    passed_l.append(user_letter)
    for l in passed_l:
        counter+=1
        letter_index = word.find(user_letter)
        print(f"{letter_index=}")
        if letter_index != None:
            print("Match")
            return hidden_word_switcher(user_letter, letter_index,word)
        if letter_index == None:
            return "No matches!"

        

def hidden_word_switcher(user_letter, letter_index, word)-> str:
    hidden_word = list(("_") * len(word))
    hidden_word.pop(letter_index)
    hidden_word.insert(letter_index, user_letter)
    hidden_word = "".join(hidden_word)
    hidden_word = hidden_word.casefold()
    print(f"the hidden word is: {hidden_word}")
    return hidden_word

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