
def _substring_counter(word, sentence):
    counter = len(sentence)
    for word_letter in word:
        print(f"{word_letter=}")
        for s_letter in sentence:
            print(f"{s_letter=}")
            if word_letter == s_letter:
                counter -= 1
                print("Match",f"{counter=}")
                if counter == (len(sentence) - len(word)):
                    return True
            else:
                continue
    return False

def substring_counter(word, sentence):
    new_word = list(word)

    for sen_char in sentence:
        index = 0
        for wor_char in new_word:
            if wor_char == sen_char:
                new_word.pop(index)
                break
            else:
                new_word = list(word)
            index += 1
        if len(new_word) == 0:
            return True 
    return False

