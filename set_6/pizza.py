import sys
import csv
from tabulate import tabulate

def main():
    #List where save dictionary come from .csv
    pizza = []

    correct = check_arguments(sys.argv)

    if correct == True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pizza.append(row)
        except FileNotFoundError:
            sys.exit("File does not exist")

        print(tabulate(pizza, headers="keys", tablefmt="grid"))

def check_arguments(argument):
    Solution = False
    if len(argument) < 2:
        sys.exit("Too few command-line arguments")

    elif len(argument) > 2:
        sys.exit("Too many command-line arguments")
        
    elif not argument[1].endswith(".csv"):
        sys.exit("Not a csv file")
        
    Solution = True
    return Solution   

main()
