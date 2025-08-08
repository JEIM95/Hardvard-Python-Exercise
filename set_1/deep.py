result = input("what is the Answer to the Grat Question of Life, the Universe,and Everything?")

result = result.replace(" ", "")
if result == "42":
    print("Yes")
else:
    result = result.strip().title()

    if result == "Forty-Two":
        print("yes")
    elif result == "Fortytwo":
        print("yes")
    else:
        print("No")
    

