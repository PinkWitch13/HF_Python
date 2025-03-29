import random

"""Description:
    Our football team has finished the championship.

    Our team's match results are recorded in a collection 
    of strings. Each match is represented by a string in 
    the format "x:y", where x is our team's score and y 
    is our opponents score.

    For example: ["3:1", "2:2", "0:1", ...]

    Points are awarded for each match as follows:

    if x > y: 3 points (win)
    if x < y: 0 points (loss)
    if x = y: 1 point (tie)
    We need to write a function that takes this collection 
    and returns the number of points our team (x) got in the 
    championship by the rules given above.

    Notes:

    our team always plays 10 matches in the championship
    0 <= x <= 4
    0 <= y <= 4  
"""

results = []
m = random.randint(0, 3)
n = random.randint(0, 3)
metch_result = []
metch_result.append("_"*7)
print(metch_result)

def game_score(metch_result):
    m = random.randint(0, 3)
    n = random.randint(0, 3)
    metch_result.append(str(m))
    metch_result.append(":")
    metch_result.append(str(n))
    return "".join(metch_result)

def game_result_collection(results):
    index= 0
    for g in range(10):
        results.append(game_score(metch_result))
        index += 1
    print(index)
    return results
     

print(game_result_collection(results))
    # for _ in range(11):
    #     metch_result.append(str(m))
    #     metch_result.append(":")
    #     metch_result.append(str(n))
    #     result = "".join(metch_result)
    #     results.append(result)
#     print(result)   
#     return results
    
# print(f"{results_collection(results)=}")

