from hr_count_string import count_substring

def test_count_substring_include_words():
    main_str = 'Kuba jest fajny'
    sub_str = 'Kuba'
    assert count_substring(main_str, sub_str) == 1

def test_count_substring_words():
    main_str = 'ABCDCDC'
    sub_str = 'CDC'
    assert count_substring(main_str, sub_str) == 2

def test_count_substring_words_and_spaces():
    main_str = 'A B C'
    sub_str = 'ABC'
    assert count_substring(main_str, sub_str) == 0
