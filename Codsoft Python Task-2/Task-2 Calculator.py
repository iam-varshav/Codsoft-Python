#TASK 2 (CALCULATOR)
operator =input("Enter the operator (+,-,*,/): ")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if operator == "+":
    result=num1+num2
    print(result)
elif operator == "-":
    result= num1-num2
    print(result)
elif opeartor == "*":
    result = num1*num2
    print(result)
else:
    result =num1 / num2
    print(result)
