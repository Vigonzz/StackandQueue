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

four_operators = {'+': 1, '-': 1, '*': 2, '/': 2}


# Helper function
def apply_operator(num_stack, op_stack):
    operator = op_stack.pop()
    right = num_stack.pop()
    left = num_stack.pop()

    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    elif operator == "/":
        if right == 0:
            raise ZeroDivisionError("Can not divide by zero")
        result = left / right
    else:
        raise ValueError("Unknown operator")
    
    num_stack.push(result)
    
def evaluate(expression):
    tokens = tokenize(expression)
    num_stack = Stack()
    op_stack = Stack()

    # Loop over functions
    for token in tokens:
        if isinstance(token, int):
            num_stack.push(token)
        else:
            while not op_stack.is_empty() and four_operators[op_stack.peek()] >= four_operators[token]:
                apply_operator(num_stack, op_stack)
            
            op_stack.push(token)

    while not op_stack.is_empty():
        apply_operator(num_stack, op_stack)
    return num_stack.pop()


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


if __name__ == "__main__":


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

    # Testing evaluating the expression 
    print(evaluate("10 + 20 * 2")) 
    print(evaluate("10 - 5 - 2"))
    print(evaluate("100 / 10 / 2"))
    print(evaluate("10 * -2"))
    print(evaluate("7"))

    # print(evaluate("10/0")) - passed







