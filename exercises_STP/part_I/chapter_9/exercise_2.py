import random

"""2. Write a program that asks a user 
    a question, and saves their answer 
    to a file.  """

rounds = random.randint(1,10)
user_answers = []

def main_ (rounds):
    for _ in range(rounds):
        answers_collector(user_answers)
        final_answer = "".join(user_answers)
    print(str(final_answer))

def answers_collector(user_answers):
    answer = str(f"{input('What is your favorite animal? ')}\n")
    user_answers.append(answer)
    return user_answers

main_(rounds)
print("Finished collecting data from user")

with open('answers.txt', 'w') as file1:
    file1.writelines(user_answers)
    file1.close()



