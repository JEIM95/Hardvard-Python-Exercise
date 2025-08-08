greeting = input("Greeting: ")

greeting = greeting.strip().capitalize()

if greeting[0] == "H" and greeting[1] == "e" and greeting[2] == "l" and greeting[3] == "l" and greeting[4] == "o":
    print("$0")
else:
    if greeting[0] == "H":
        print("$20")
    else:
        print("$100")