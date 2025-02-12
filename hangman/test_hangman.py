from hangman import hangman_logic
from hangman import hidden_word_switcher
from hangman import hangman_turn

def _test_hangman_turn_1_match_lower():
    word = "kuba"
    hidden_word = "____"
    user_letter = "b"
    assert hangman_turn(word, hidden_word, user_letter) == "__b_"

def _test_hangman_turn_1_match_upper():
    word = "kuba"
    hidden_word = "____"
    user_letter = "B"
    assert hangman_turn(word, hidden_word, user_letter) == "__b_"

def _test_hangmen_turn_no_match():
    word = "kuba"
    hidden_word = "____"
    user_letter = "z"
    assert hangman_turn(word, hidden_word, user_letter) == "No matches!"

def test_hidden_word_switcher_one_index():
    word = "hangman"
    hidden_word = "_______"
    user_letter = "g"
    assert hidden_word_switcher(user_letter, word, hidden_word) == "___g___"

def _test_hidden_word_switcher_multi_index():
    word = "hangman"
    hidden_word = "_______"
    user_letter = "n"
    assert hidden_word_switcher(user_letter, word, hidden_word) == "__n___n"

def __test_hangman_logic_output_one_mach(): 
    word = "hangman"
    letter = "g"
    assert hangman_logic(word, letter) == "___g___"
