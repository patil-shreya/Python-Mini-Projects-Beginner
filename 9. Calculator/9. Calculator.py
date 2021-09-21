import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

operations= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "**":exponent, 
}

def calculator():
    print(art.logo)

    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)

    end_calculation = False

    while not end_calculation:
        operations_symbol = input("Pick an operation: ") 

        num2 = float(input("What is the next number? "))

        selected_function = operations[operations_symbol]
        answer = selected_function(num1,num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        want_to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ").lower()

        if want_to_continue == "y":
            num1 = answer
        elif want_to_continue == "n":
            end_calculation = True
            calculator()

calculator()







