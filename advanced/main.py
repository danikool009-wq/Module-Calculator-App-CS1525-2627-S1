import operations as o
import utils as u
try:
    number1 = int(input("enter the first number"))
    number2 = int(input("enter the second number"))
except ValueError:
    print("Please enter a number")
if u.get_operation() == "+":
    print(o.add(number1, number2))
elif u.get_operation() == "-":
    print(o.subtract(number1, number2))
elif u.get_operation() == "*":
    print(o.multiply(number1, number2))
elif u.get_operation() == "/":
    print(o.divide(number1, number2))

print("answer calculated")
