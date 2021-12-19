# this is an age calculator
# you enter your age
# it calculates your age in decades and days

age = int(input('How old are you:\n'))

decades = age // 10     # the // divides as whole numbers, so you don't get a floating type answer
years = age % 10

print('You are ' + str(decades) + ' decades and ' + str(years) + ' years old.')
