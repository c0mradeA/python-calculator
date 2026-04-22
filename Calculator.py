#This is a Github project
print("This is a python calculator")
while True:
    try:
        x = int(input("Enter the first integer: "))
        y = int(input("Enter the second integer: "))
        break
    except ValueError:
        print("ERROR! Please enter a valid number.")

# Inputs for the operators
op = input("Choose your operator (+, -, *, /, %): ")

# Logic
if op == "/":
    # Checking for division by zero(preventing crash)
    if y == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {x / y}")

elif op == "+":
    print(f"Result: {x + y}")

elif op == "-":
    print(f"Result: {x - y}")

elif op == "*":
    print(f"Result: {x * y}")

elif op == "%":
    print(f"Result: {x % y}")

else:
    print("The Operator isn't supported")