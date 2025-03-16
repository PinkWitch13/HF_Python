"""10. Slice the string "It was a bright cold day in April, 
   and the clocks were striking thirteen." to only include 
   the characters before the comma.  """

sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
changed_sentence = list(sentence)
changed_sentence.pop()
changed_sentence = "".join(changed_sentence)
print(changed_sentence)