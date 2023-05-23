# Write a program that accepts positive numbers from the user until the user types a negative number
#For each number the received serial number will be displayed. The sum of the numbers and the current average.
sum = 0
avg = 0
count = 0
number = (int(input('Enter a number #1: ')))
while number >= 0:
    count += 1
    sum += number
    avg = sum / count
    number = (int(input(f'Enter a number #{count+1} (avg={avg},sum={sum}): ')))
print('Yalla bye.')

