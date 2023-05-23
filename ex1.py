#Write a Python program that takes a number and prints all its integer parts.
number = int(input('Enter a number '))
for i in range(1, number + 1):
    if number % i == 0:
        print(i , end=', ')