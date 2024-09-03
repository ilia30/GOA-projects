def  simple_calculator():
    num1 = float(input("enter your number: "))
    num2 = float(input("enter your number: "))
    operation =   input("enter your operation (+ , - , * , / ) " )

    if operation == "+":
       return num1 + num2
    elif operation == "-":
       return num1 - num2
    elif operation == "*":
       return num1 * num2
    elif operation == "/":
       if num2 != 0:
        return num1 / num2
       else: 
          return "zero division error"
    else:
       return "invalid operation"

result =  simple_calculator()
print(result)   