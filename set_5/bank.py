def main():
    greeting = input("Greeting: ")

    print(value(greeting))


def value(greeting):
    greeting = greeting.strip().capitalize()
    if greeting[0] == "H" and greeting[1] == "e" and greeting[2] == "l" and greeting[3] == "l" and greeting[4] == "o":
        price = "$0"
    else:
        if greeting[0] == "H":
            price = "$20"
        else:
            price ="$100"
    return price

if __name__ == "__main__":
    main()
