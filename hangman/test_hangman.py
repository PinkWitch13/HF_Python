from hangman import hangman_logic
from hangman import hidden_word_switcher
from hangman import hangman_turn

def test_hangman_turn_1_match_lower():
    word = "kuba"
    user_letter = "b"
    assert hangman_turn(word, user_letter) == "__b_"

def test_hangman_turn_1_match_upper():
    word = "kuba"
    user_letter = "B"
    assert hangman_turn(word, user_letter) == "__b_"

def test_hangmen_turn_no_match():
    word = 'kuba'
    user_letter = "c"
    assert hangman_turn(word, user_letter) == "No matches!"

def test_hidden_word_switcher_one_index():
    word = "hangman"
    each_letter = "g"
    letter_index = 3
    assert hidden_word_switcher(each_letter, letter_index, word) == "___g___"

def __test_hangman_logic_output_one_mach(): 
    word = "hangman"
    letter = "g"
    assert hangman_logic(word, letter) == "___g___"
