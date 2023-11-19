'''Create a simple calculator program that takes two numbers and an operator (+-*/) as input
and performs the corresponding operation'''

num1 = int(input("enter number1 :"))
num2 = int(input("enter number2 :"))

operator = input("operation : ")

result = str(num1) + operator+ str(num2)

print(num1,operator,num2,"=",eval(result))


# print(num1 ,operator ,num2)
