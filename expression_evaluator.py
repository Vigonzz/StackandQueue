# Violet Gonzalez, Oct 21, 2026
# SWE 240P Assignment 2: Stack and Queue

# Task 2:
# Given a string str that represents an arithmetic expression, 
# evaluate the arithmetic expression.  The arithmetic expression 
# can only include any arithmetic operators (i.e., +, -, /, *) and 
# numeric operands, i.e., any positive or negative integer from  
# (-2^31) to (2^31-1).  There may be one or more white spaces between 
# an operand and an operator. You should ignore the white spaces while 
# scanning. For an invalid expression, i.e., any operand other than 
# numeric values, invalid operator, or division by 0, either return NaN 
# or throw an exception. You have to use the stack you implemented in 
# Task-1 of the assignment. Write sample test cases to validate your implementation.


# Note:
# Exception handling will be through raising an error
# I am going to follow true division, meaning using / instead of // thus not having to round negatives down
# The sign for digits indicating a negative will be touching the actual number 


from stack_db import Stack

# I needed more reading and examples on flags in python:
# Working with flags in Python. (n.d.). https://code.mu/en/python/book/prime/loops/flags/# 
def tokenize(expression):
    tokens = []
    index = 0
    expect_number = True

    # Walks through the whole string
    # Once index reaches the length , every character handled
    while index < len(expression):
        character = expression[index]

        if character ==  " ":
            index += 1
            continue

        if expect_number:
            sign = 1
            if character == "-":
                sign = -1
                index += 1 
            if index >= len(expression) or not expression[index].isdigit():
                raise ValueError("Should be a number")

            digits = ""
            # Reads one number and placing the characters into the digits string
            while index < len(expression) and expression[index].isdigit():
                digits += expression[index]
                index += 1

            number = int(digits) * sign

            if number < -(2 ** 31) or number > 2 ** 31 - 1:
                raise ValueError(f"Invalid operator {number}")
            
            tokens.append(number)
            expect_number = False
        else:
            if character in "+-*/":
                tokens.append(character)
                index += 1
                expect_number = True
            else:
                raise ValueError(f"Invalid operator: '{character}' at position: {index}")
                


    if expect_number:
        raise ValueError("Expression is empty or ends with an operator")
    
    return tokens


# Test prints for checking the operator and overall input
print(tokenize("42"))
print(tokenize("  7 "))
print(tokenize("-15"))
# print(tokenize("2147483648"))

# Testing the arithmetic operator 
print(tokenize("10 + 20 * 2"))
print(tokenize("3 + 4"))
print(tokenize("10 * -2"))
print(tokenize("10 - -5"))

# Check for error handling
# print(tokenize("foo / 30 + 7")) - passed
# print(tokenize("10 % 3")) - passed
# print(tokenize("10 20")) - passed
# print(tokenize("5 +")) - passed
# print(tokenize("")) - passed




