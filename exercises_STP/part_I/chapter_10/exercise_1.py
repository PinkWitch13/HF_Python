import random
"""1. Modify the Hangman game, so the word is 
    selected randomly.  """

def letter_provider():
    user_character = input("Guess a letter: ")
    return user_character    

def password_to_guess(words_collection):
    left_words = words_collection
    for w in range(0, len(words_collection)):
        index = random.randint(0, len(left_words))
        word = left_words.pop(index)
        return word
    
def another_hangman(word):
    wrong = 0
    stages =["", \
             "______________             ", \
             "|              |           ", \
             "|              |           ", \
             "|              O           ", \
             "|             /|\          ", \
             "|             / \          ", \
             "|                          "]
    
    right_letters = list(word)
    board = ["__"] *len(word)
    win = False
    print("Welcome to Hangman!")
    
    while wrong < len(stages) -1:
        print("\n")
        user_character = letter_provider() 
        if user_character in right_letters:
            character_index = right_letters.index(user_character)
            print(character_index)
            board[character_index] = right_letters[character_index]
            right_letters[character_index] = "$"
            print("Correct! ")
            print(board)
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))












words_collection = ["cat", "cow", "crow", "whale", "penguin", "armadillo", \
                      "jellyfish", "giraffe", "lion", "tiger", "magpie", \
                      "mouse", "dog", "badger", "wolverine", "swan", "foal", \
                      "horse", "parrot", "robin", "mantis", "kiwi", "cancer", \
                      "snake", "dolphin", "octopus", "wasp", "ant", "tick", \
                      "mosquito", "spider", "fly", "hamster", "pig", \
                      "deer", "muse", "bat", "toad", "frog", "trout", \
                      "catfish", "elk", "butterfly", "moth", "beetle", \
                      "camel", "eagle", "falcon", "sparrow", "rhinoceros", \
                      "pidgeon", "owl", "ape", "gorilla", "viper", "ostrich", \
                      "lizzard", "turtle", "squid", "shrimp", "rabbit", \
                      "volture", "shrike", "caterpillar", "bee", "wolf", \
                      "bumblebee", "fox", "bobcat", "jaguar", "zebra", \
                      "baboon", "shark", "crocodile", "aligathor", "cameleon", \
                      "woodpecker", "cheetha", "hyena", "hippo", "salmon", \
                      "seal", "walrus", "narwhal", "warthog", "gazelle", \
                      "toucan", "hawk", "penguin", "puma", "axelotl", \
                      "raven", "heron", "duck", "seagull", "pelican", "kite", \
                      "needlefish", "chimpanzee", "macaque", "bison", "jay", \
                      "kangaroo", "koala", "hare", "platypus", "anteater", \
                      "newt", "salamander", "scorpion", "boa", "anaconda", \
                      "hornet", "marten", "weasel", "boar", "goat", "goose", \
                      "hen", "rooster", "dove", "crane", "squirell", "groundhog", \
                      "mouflon", "panther", "coyote", "porcupine", "geco", \
                      "tuna", "pike", "carp", "cockroach", "dragon", "unicorn", \
                      "phenix", "pegasus", "thunderbird", "pony", "swallow", \
                      "nightingale", "lark", "nightjar", "termite", "puffin", \
                      "snail", "microbe", "virus", "bacteria", "stingray", \
                      "pufferfish", "bass", "marmoset", "antelope", "headhog", \
                      "jackal", "sparrowhawk", "cardinal", "tit", "warbler", \
                      "flamingo", "blackbird", "stork", "condor", "jaguar", \
                      "ibis", "fennec", "cobra", "rattlesnake", "scalar", \
                      "mouserabbit", "lemur", "orangutan", "donkey", "lamb", \
                      "sheep", "ram", "calf", "puppy", "kitten", "chick"]
    
if __name__ == "__main__":
    another_hangman(password_to_guess(words_collection))