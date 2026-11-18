#wap to create a simple calculator using a switch case and function for very operations.

def calculate(num1,num2,op):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    elif op=="/":
        return num1/num2
    else:
        return "Invalid operator"
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
op=input("Enter operator: ")
print(calculate(num1,num2,op))