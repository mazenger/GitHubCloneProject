num1 = int(input("Enter 'x' "))
num2 = int(input("Enter 'y' "))
calc = input("choose operation(+, -, *, /)")
total = 0
if calc == "+":
    total = (num1 + num2)
elif calc == "-":
    total = (num1 - num2)
elif calc == "*":
    total = (num1 * num2)
elif calc == "/":
    total = (num1 / num2)
else:
    print("sorry u entered smth wrong")

print("your sum is " + str(total))