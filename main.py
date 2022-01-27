import art
print(art.logo)

def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    return (a/b)
operations = {"+": add,"-" : subtract,"*" : multiply,"/" : divide}

def calculator():
    n1 = float(input("What's the first number?:\n"))
    should_continue = True

    while should_continue:
        for i in operations:
            print(i)
        op = input("Pick an operation from the list above.:\n")
        n2 = float(input("What's the next number?:\n"))
        calculation_fun = operations[op]
        answer = calculation_fun(n1, n2)
        print(f"{n1}{op}{n2}={answer}")
        if input(f"Type 'y' to type calculating with {answer}:\n") == 'y':
            n1 = answer
        else:
            should_continue = False
            if input(f"Do you want to go again?:\n")== 'y':
                calculator()
            else:
                print("Okay Bye!!!")
calculator()
