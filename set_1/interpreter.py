operation = input("Expression: ")
x, y, z = operation.split(" ")

#Convert str to double
num_1 = float(x)
num_2 = float(z)

match y:
    case "+":
        result = num_1 + num_2
    case "-":
        result = num_1 - num_2
    case "*":
        result = num_1 * num_2
    case "/":
        result = num_1 / num_2
    case _:
        print("Error")

print(result)
