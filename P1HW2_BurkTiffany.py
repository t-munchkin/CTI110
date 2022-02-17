# Using IDLE to create an example of a pizza order
# 2/17/2022
# CTI-110 P1HW2 - Pizza Order
# Tiffany Burk
#

# BEGIN Pseudocode
    # Make it look like an example pizza order
        # Ask user to input number of students ordering pizza for (num_students), use 25 for example
        # number of pizza slices (num_slices) is num_students multiplied by 3
            # display output
        # number of pizzas needed (num_pizza) is num_slices divided by 2
            #display output
#END pseudocode

num_students = int((25))
num_slices = (num_students * 3)
num_pizzas = (num_slices / 2)
print('How many students would you like to order pizza for?', num_students)
print('------Pizza Order------')
print('Number of Students:', num_students)
print('Pizza Slices Needed:', num_slices)
print('Pizzas Needed:', num_pizzas)
print('-----------------------')
