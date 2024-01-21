# Write a program to check if the given number is a palindrome number.

# pseudocode

# ask user to enter a number
number = int(input("Enter a number: "))

# write a message on what the user entered
print("The original number is", number)

# reverse the given number
rev_number = 0
while number > 0:
    remainder = number % 10
    rev_number = (rev_number * 10) + remainder
    number = number // 10

# check if the given number is equal to the reversed number

# if yes, return true

# else return false
