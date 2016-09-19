#prototype
#boolean

#bit = boolean
# True
# False

from random import *

def generate_quiz():
    num1 = 0
    num2 = 0
    sign = ""
    answer = ""

    #Logic

    # 1: Generate random operands and operator
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    sign = choice(["+", "-", "*", "/"])

    # 2:
    error = choice([1, 0, -1])

    # 3: Caculate the actual (real) result
    answer = calculate(num1, num2, sign)
    
    # Add error
    answer = answer + error


    return [num1, num2, sign, answer]

def calculate(x, y, sign):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    else:
        return x / y

def check_answer(num1, num2, sign, answer, user_choice):
    if answer == calculate(num1, num2, sign): # answer is True
        return user_choice
    else: # answer is False
        return (not user_choice)















