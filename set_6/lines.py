import sys

count = 0

#check errors
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
    
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        for line in file:
            correct = line.lstrip()
            if correct !="" and correct[0] != "#":
                count = count + 1

except FileNotFoundError:
    sys.exit("File does not exist")  

print(f"Code lines: {count}")

