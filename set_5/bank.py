def main():
    try:
        greeting = input("Greeting: ")

        if not isinstance(greeting, str):
            raise AttributeError("You have to introduce string value")
        if greeting == "":
            raise EOFError
        
        print(value(greeting))
    except EOFError:
        pass
    except AttributeError:
        pass

def value(greeting):
    if not isinstance(greeting, str):
        raise AttributeError("You have to introduce string value")
    
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        price = "$0"
    elif greeting.startswith("h"):
        price = "$20"
    else:
        price ="$100"
    return price

if __name__ == "__main__":
    main()
