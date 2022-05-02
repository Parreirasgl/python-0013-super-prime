# I saw an exercise on the internet asking you to create a program
# which would take an input from the user (a number from 1 to 9) and
# as output would display a list of super prime numbers (numbers that
# are prime and, at the same time, that all its digits are prime). Those
# super prime numbers must be presented in ascending order, and must
# have a certain number of digits (such number of digits being the number
# entered as input).

list_a = ["3", "5", "7"]
list_b = ["0", "2", "3", "5", "7"]
number = ""

while True:
    for i in list_b:
        number += i
        for i2 in list_b:
            number += i2
            for i3 in list_a:
                number += i3
                print(number)
                number = number[:-1]
            number = number[:-1]
        number = number[:-1]
    break
