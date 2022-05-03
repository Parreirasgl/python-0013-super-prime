# I saw an exercise on the internet asking you to create a program
# which would take an input from the user (a number from 1 to 9) and
# as output would display a list of super prime numbers (numbers that
# are prime and, at the same time, that all its digits are prime). Those
# super prime numbers must be presented in ascending order, and must
# have a certain number of digits (such number of digits being the number
# entered as input).

list_a = ["3", "5", "7"]
list_b = ["0", "2", "3", "5", "7"]
digits = 3
number = ""

possible_digits = []
hundreds = 0
tens = 0
units = 0

for i in range(digits):
  if i == (digits-1):
    possible_digits.append(list_a)
  else:
    possible_digits.append(list_b)

print(possible_digits)

counter = 3 * (5**(digits-1))

while hundreds < 5:
  print(str(possible_digits[0][hundreds]) + str(possible_digits[1][tens]) + str(possible_digits[2][units]))
  units += 1
  if units == 3:
    tens += 1
    units = 0
  if tens == 5:
    if hundreds == 0:
      hundreds += 1
      tens = 1
    else:
      hundreds += 1
      tens = 0