from hr_count_string import substring_counter

sentence = "Kuba jest fajny"
word = "Kuba"

sentence = "ABCDCDC"
word = "CDC"

sentence = "A B C"
word = "ABC"

def test_substring_counter_include_words():
    sentence = 'Kuba jest fajny'
    word = 'Kuba'
    assert substring_counter(word,sentence) == True

def test_substring_counter_words():
    sentence = "ABCDCDC"
    word = "ABC"
    assert substring_counter(word,sentence) == True

def test_substring_counter_words_and_spaces():
    sentence = "A B C"
    word = "ABC"
    assert substring_counter(word,sentence) == False
