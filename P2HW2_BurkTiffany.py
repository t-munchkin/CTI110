# CTI-110
# P2HW2 - Score Avg
# Tiffany Burk
# 3/2/2022
#

# User input for seven individually listed scores, on different statements.
# Give a descriptive name for the list.
# Lowest score shoule be stored in a variable and drop it from the list.
# After doing the above, calculate average score.
# Display lowest score entered, then display score list after dropping that number, and then display the average of the scores in the above list
#

score_one = float(input('Enter score #1:'))
score_two = float(input('Enter score #2:'))
score_three = float(input('Enter score #3:'))
score_four = float(input('Enter score #4:'))
score_five = float(input('Enter score #5:'))
score_six = float(input('Enter score #6:'))
score_seven = float(input('Enter score #7:'))
scores = [score_one, score_two, score_three, score_four, score_five, score_six, score_seven]
lowest_score = min(scores)
scores.remove(lowest_score)
score_avg = sum(scores)/len(scores)
print('')
print('-------Results-------')
print('Lowest Score :', lowest_score)
print('Modified List:', scores)
print('Scores Average:', score_avg)
print('---------------------')
