#Write dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.00

def add_zero(x):
    x_str = str(x)
    entero,decimal = x_str.split(".")
    n_number = len(decimal)
    if n_number == 1:
        x_str = x_str + "0"
    return x_str

while True:
    try:
        meal = input("Item: ").title()

        if meal in menu:
            money = menu[meal]
            total = total + money

            total_str = add_zero(total)
            
            print(f"Total: ${total_str}")

    except EOFError:
        break
    except TypeError:
        pass

print("\n")




        
    
