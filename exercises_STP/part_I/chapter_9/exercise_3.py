import csv

"""3. Take the items in this list of lists: [['Top Gun',
    'Risky Business', 'Minority Report'], ['Titanic', 
    'The Revenant', 'Inception'], ['TrainingDay', 
    Man on Fire', 'Flight']] and write them to a CSV file. 
    The data from each list should be a row in the file, 
    with each item in the list separated by a coma.  """

movie_titles = [['Top Gun','Risky Business', 'Minority Report'], \
               ['Titanic', 'The Revenant', 'Inception'], \
               ['TrainingDay', 'Man on Fire', 'Flight']]

with open('movies.csv', 'w', newline='') as movies:
    w = csv.writer(movies, delimiter=',')
    for film_list in movie_titles:
        w.writerow(film_list)
        

