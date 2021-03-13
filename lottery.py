from random import randint


# @brief    Pick different numbers randomly (1~45) then make a list with them.
# @param    n   the total numbers of being picked
# @return   random_list     an unsorted list that consists of randomly chosen numbers
def generate_numbers(n):
    random_list = []

    while len(random_list) < n:
        elem = randint(1, 45)  # Pick up a number randomly
        if elem not in random_list:  # Check if the chosen number is in the list
            random_list.append(elem)

    return random_list


# @brief    Return a list that includes winning numbers
# @return   winning_list    a list that includes 7 winning numbers.
#           (6 numbers are ordinary numbers and they are sorted in the list.)
#           (1 number is a bonus number and it exist at the end of the list.)
def draw_winning_numbers():
    winning_list = generate_numbers(6)  # Pick up 6 ordinary numbers
    winning_list.sort()  # Sort the list

    while True:
        elem = randint(1, 45)  # Pick up a bonus number
        if elem not in winning_list:  # Check if the chosen number is in the list
            winning_list.append(elem)
            break

    return winning_list
'''
# More simple way to define 'draw_winning_numbers()'
def draw_winning_numbers():
    winning numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6]
'''

# @brief    Count the number of overlapping elements in two lists
# @param    user_list       a list from a customer
#           winning_list    a list that includes winning numbers
# @return   matching_num    the number of overlapping elements in user_list and winning_list
def count_matching_numbers(user_list, winning_list):
    matching_num = 0

    for num in user_list:
        if (num in winning_list):
            matching_num = matching_num+1

    return matching_num


# @brief    Check how much money the customer can get
# @param    user_list       a list from a customer
#           winning_list    a list that includes winning numbers
# @return   a lottery payout
#           (case 1) whole numbers from the customer == whole ordinary numbers in the winning_list -> 1000000000 won
#           (case 2) 5 numbers from the customer == 5 ordinary numbers in the winning_list
#                    1 number from the customer == a bonus number in the winning_list              -> 50000000 won
#           (case 3) 5 numbers from the customer == 5 ordinary numbers in the winning_list         -> 1000000 won
#           (case 4) 4 numbers from the customer == 4 ordinary numbers in the winning_list         -> 50000 won
#           (case 5) 3 numbers from the customer == 3 ordinary numbers in the winning_list         -> 5000 won
def check(user_list, winning_list):
    intersection7 = count_matching_numbers(user_list, winning_list)  # Including bonus number
    intersection6 = count_matching_numbers(user_list, winning_list[0:6])
    if intersection6 == 6:
        return 1000000000
    elif intersection7 == 6:
        return 50000000
    elif intersection6 == 5:
        return 1000000
    elif intersection6 == 4:
        return 50000
    elif intersection6 == 3:
        return 5000
    else:
        return 0
