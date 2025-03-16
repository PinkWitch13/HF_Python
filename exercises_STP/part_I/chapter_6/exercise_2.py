"""2. Write a program that collects two strings from a user, 
   inserts them into the string "Yesterday I wrote a [response_one]. 
   I send it to [response_two]!" and prints a new string.  """

response_one = input('What you want to send: ')
response_two = input('Provide a recipient: ')

sentence = "Yesterday I prepered a {}. I send it to {}!".format(response_one, response_two)
print(sentence)