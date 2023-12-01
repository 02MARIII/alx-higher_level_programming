#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    
    num_args = len(sys.argv) - 1
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    operand1 = int(sys.argv[1])
    operand2 = int(sys.argv[3])
    result = operations[operator](operand1, operand2)
    print("{} {} {} = {}".format(operand1, operator, operand2, result))
