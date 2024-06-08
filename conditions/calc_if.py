
import sys

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "add":
    output = (num1 + num2)
    print(output)
else:
    print("valid input")