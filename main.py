def calculator (operation, value1, value2):
  if operation == "+": return value1 + value2
  if operation == "-": return value1 - value2
  if operation == "*": return value1 * value2
  if operation == "/": return value1 / value2

print(calculator("+", 10, 1))
print(calculator("*", 10, 5))
print(calculator("/", 80, 4))
print(calculator("-", 1.1, 0.1))

#my first calculator :) 