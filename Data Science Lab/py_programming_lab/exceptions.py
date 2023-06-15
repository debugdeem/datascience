def divide_number(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
print(divide_number(10,0))