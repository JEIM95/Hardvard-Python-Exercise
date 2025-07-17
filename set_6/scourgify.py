import sys
import csv

def main():
    #List where save dictionary come from .csv

    correct = check_arguments(sys.argv)

    if correct == True:
        try:
            with open(sys.argv[1], "r") as first, open(sys.argv[2],"w", newline = "") as second:
                reader = csv.DictReader(first)
                writer = csv.DictWriter(second, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    lastName, Name = row["name"].split(",")
                    writer.writerow(
                        {
                            "first": Name.strip(),
                            "last": lastName.strip(),
                            "house": row["house"]
                        }
                    )

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def check_arguments(argument):
    Solution = False
    if len(argument) < 3:
        sys.exit("Too few command-line arguments")

    elif len(argument) > 3:
        sys.exit("Too many command-line arguments")
        
    elif not argument[1].endswith(".csv"):
        sys.exit("Not a csv file")
        
    Solution = True
    return Solution   

main()