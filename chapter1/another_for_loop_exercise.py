"""The beer song application starts with 99 bottles of the beer on the wall and counts down until there's no more beer."""

#assign variable "word" to string value "bottles"
word = "bottles"
# for every "beer_num object which is an integer value in range from 99 to 0, loop up counting -1 with each iteration.
for beer_num in range (99,0, -1):
#in new line display on screen value assigned to beer_num variable, value of variable word, and the string:"of beer on..."
#in new line display on screen value assigned to beer_num variable, value of variable word, and the string: "of beer."
#in new line display on screen string "Take one down."
#in new line display on screen string "Pass it around."
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
#if value of beer_num variable is equal 1, display on screen "No more bottles..."
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
#else, to new variable "new_num" assigne value which is result of subtraction: beer_num (value) - 1   
    else:
        new_num =  beer_num -1
#if value of new_num variable is equal 1, assign string value "bottle" to variable "word", then display on screen value of new_num, word, and the string "of beer on..."
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
#display on screen an empty line (print nothing XD)
    print()
    
