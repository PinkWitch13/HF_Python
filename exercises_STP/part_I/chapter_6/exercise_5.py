"""5. Take the list ["The", "fox", "jumped", "over", "the",
    "fence", "."] and turn it into a grammatically correct string.
    There should be a space between each word, but no space between 
    the word fence and period that follows it. (Don't forget, you learned 
    a method that turns a list of strings into a single string). """

words = ["The", "fox", "jumped", "over", "the","fence", "."]

sentence = " ".join(words)

print(sentence)