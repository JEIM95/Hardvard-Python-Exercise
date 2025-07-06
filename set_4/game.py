import random

Value = 0
Level = -1

while Level < 0:
    try:
        Level = int(input("Level: "))
    except ValueError:
        pass

number = random.randint(1, Level)

while number != Value:
    Value = -1
    while Value < 0:
        try:
            Value = int(input("Guess: "))
        except ValueError:
            pass
    
    if number < Value:
        print("Too large!")
    elif number > Value:
        print("Too small!")

if number == Value:
    print("Just Right!")