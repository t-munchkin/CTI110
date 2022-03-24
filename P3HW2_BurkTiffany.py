# CTI-110
# P3HW2 - Pizza Order
# Tiffany Burk
# 3/24/2022
#

import math

# input number of students from user input
num_students = int(input('How many students do you want to order pizza for?'))
# input number of people, 1.5, 2 or 3, per pizza
num_people = float(input('Enter number of people per pizza (1.5, 2 or 3):'))

# if the people per pizza input is valid then calculate number of pizzas and price
if num_people == 1.5 or num_people == 2 or num_people == 3:
    whole_pizza = math.ceil(num_students / num_people)
    price = whole_pizza * 5
    price = price + (price * 0.06)
# display results
    print('------Pizza Order------')
    print('Number of Students:', num_students)
    print('Pizzas Needed:', whole_pizza)
    print('Price: $', price )
    print('-----------------------')
else:
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2 or 3')
    print('Run Program again')

