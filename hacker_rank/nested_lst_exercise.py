"""Given the names and grades for each student 
    in a class of N students, store them in a nested 
    list and print the name(s) of any student(s) 
    having the second lowest grade.

    Note: If there are multiple students with the 
    second lowest grade, order their names 
    alphabetically and print each name on 
    a new line.  """

students_scores = []

def sec_sort(each_list):
     return each_list[1]

    
def lowest_score(student_scores):
    checked_scores = []

    student_scores.sort(key=sec_sort)
    i = 0

    for student in student_scores:
        score = student[1]
        if score in checked_scores:
            continue
        checked_scores.append(score)
        i += 1

        if i >= 2:
            return score

    raise ValueError("No smallest student score")

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_scores.append([name, score])
    lowest_score(students_scores)
    



print(lowest_score(students_scores))
    # TO-DO: Find second lowest score among students
    # TO-DO: Find all indexes of sudents matching second lowest score
    # TO-DO: Create new list with student names matching second lowest score
    # TO-DO: Sort new list alphabetically
    # TO-DO: Print each name natching second lowest score
