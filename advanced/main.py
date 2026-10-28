import operations as o
import utils as u
try:
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the second number"))
except ValueError:
    print("Please enter a number")
if u.get_operation() == "+":
    print(o.add(num1, num2))
elif u.get_operation() == "-":
    print(o.subtract(num1, num2))
elif u.get_operation() == "*":
    print(o.multiply(num1, num2))
elif u.get_operation() == "/":
    print(o.divide(num1, num2))
