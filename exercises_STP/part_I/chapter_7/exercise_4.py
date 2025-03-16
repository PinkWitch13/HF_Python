"""4. Write a program with an infinite loop 
   (with othe option to type q to quit) and a list
   of numbers. Each time through the loop ask the user 
   to guess a number on the list and tell them whether 
   or not they guessed correctly. """

numbers_list = list(range(0,100))

while True:
   answer = input("Please type a number(or 'q' to quit): ")
   # Validate data
   if answer == 'q':
       print("Good bye.")
       break
   elif not answer.isnumeric():
       print("Wrong input data")
       continue

   # Process data
   answer = int(answer)
   if answer in numbers_list:
       print(f"Correct! {answer} is the right number.")
   else:
       print(f"Wrong answer! {answer} is not the right number.")
      