# from art import logo
#
# print(logo)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def start():
    global answer
    global repeat_choice
    for key in operations:
        print(key)
    choice = str(input("Pick an operation: "))
    num2 = int(input("What's your second number: "))
    calc_function = operations[choice]
    answer = calc_function(num1, num2)
    print(f"{num1} {choice} {num2} = {answer}")
    repeat_choice = str(input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit.: "))

num1 = int(input("What's your first number: "))
start()
while repeat_choice == "y":
    num1 = answer
    start()
