#                                                                                       Finance Diary

import csv
import sys
from datetime import date

#Global 
financials = []

def main():
    global financials
    
    if sys.argv[1] == "-h":
        help_fuction()
        sys.exit()

    if len(sys.argv) < 2:
        sys.exit("Few arguments")
    else:
        if not sys.argv[1] == "-r" and not sys.argv[1] == "-w" and not sys.argv[1] == "-a":
            sys.exit("First argument is not -r, -w or -a")
        else:
            #Reading calculate
            if sys.argv[1] == "-r" and len(sys.argv) == 3:
                #Check keyword is correct
                Result_reading = check_reading_values(sys.argv[2].capitalize())

                if Result_reading == True:
                    match sys.argv[2].capitalize():
                        case "Full":
                            save_csv() #Save CSV in list of dictionary
                            show_csv("Full") #Show CSV
                        case _:
                            save_csv()
                            show_csv(sys.argv[2])
            elif sys.argv[1] == "-r" and len(sys.argv) != 3:
                sys.exit("argument no valid")

            #Writing calculate
            elif sys.argv[1] == "-w" and len(sys.argv) == 6:
                Result_writing = check_writing_values(sys.argv[2], sys.argv[4], sys.argv[5])
                if Result_writing == True:
                    write_csv(sys.argv[3], sys.argv[5]) #Concept, value

            elif sys.argv[1] == "-w" and len(sys.argv) != 6:
                sys.exit("argument no valid")
            
            #Average calculate
            elif sys.argv[1] == "-a" and len(sys.argv) == 3:
                Result_average = check_date(sys.argv[2])
                if Result_average == True:
                    average = arithmetic_mean(sys.argv[2])
                    print(f"The arithmetic mean in date: {sys.argv[2]} is: {average}€")
            elif sys.argv[1] == "-a" and len(sys.argv) != 3:
                sys.exit("argument no valid")

#save CSV in list of dictionery
def save_csv():
    global financials
    financials = []

    with open("financial.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            financials.append({"date": row["date"], "concept": row["concept"], "income/expenses": row["income/expenses"], "balance": row["balance"]})
  
#Show CSV
def show_csv(x):
    global financials
    find = False

    if x == "Full":
        for financial in financials:
            print(f"date: {financial["date"]}, Concept: {financial["concept"]}, income/expenses: {financial["income/expenses"]}€, balance: {financial["balance"]}€")
    else:
        for financial in financials:
            if financial["date"] == x:
                find = True
                print(f"date: {financial["date"]}, Concept: {financial["concept"]}, income/expenses: {financial["income/expenses"]}€, balance: {financial["balance"]}€")
        if find == False:
            print(f"No movements this day: {x}")   

#Wite in CSV
def write_csv(concept, n):
    global financials
    #Save CSV in list of dictionary
    save_csv()
    
    try:
        ultimo_balance = financials[-1]["balance"]
    except IndexError:
        total=0
    else:
        total = int(ultimo_balance)

    valor = int(n)  #n es ingresos/gastos

    total = total + valor #Balance

    date_today = date.today() #Fecha de hoy yyyy-mm-dd

    financials.append(
                {
                    "date":date_today, 
                    "concept":concept, 
                    "income/expenses":valor, 
                    "balance":total
                }
            )
    with open("financial.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "concept", "income/expenses", "balance"])
        
        writer.writeheader()
        writer.writerows(financials)

#Checking arguments when you want read CSV
def check_reading_values(x):
    valid = False

    if x == "Full":
        valid = True
    elif not x == "Full":
       valid = check_date(x)
    
    return valid


def check_date(x):
    components = []
    components = x.split("-")
        
    try:
        if len(components[0]) == 4 and len(components[1]) == 2 and len(components[2]) == 2:
            for n in range(0, len(components)):
                components_num = int(components[n])
            valid = True
        else:
            valid = False
            raise ValueError 
    except ValueError:
        sys.exit("Invalid date")
    except IndexError:
        sys.exit("Invalid date")
    
    return valid

#Checking arguments when you want write CSV
def check_writing_values(a, b, c):
    #a -> Have to -c
    #b -> Have to -v
    #c -> Have to a number

    try:
        if a == "-c" and b == "-v":
            value = int(c)
        else:
            sys.exit("Some argument is not correct")
    
    except ValueError:
        sys.exit("Last argument is not a number")
    
    return True

#save in list of dictionary earn/spend money in a date
def values_to_average(a): #a is a date
    global financials
    
    save_csv()

    find = False
    list_money = []

    for financial in financials:
        if financial["date"] == a:
            find = True
            list_money.append(financial["income/expenses"])
    
    if find == False:
        sys.exit(f"No movements this day: {a}") 
    
    return list_money

#Give average earn/money in a date
def arithmetic_mean(x): #x is a date
    list_money = []
    number = 0

    list_money = values_to_average(x)

    for list in list_money:
        number = number + int(list)
    average = number / len(list_money)
    
    return round(average,2)


def help_fuction():
    print("This project enables you to track and store your financial transactions in a CSV file.\n" 
    "\nTo run programm. Python projec.py + argument\n"
    "\nFirst argument: -r: Read  -w: Write  -a: Average -h: help\n"
    "Second argument:\n" 
        "\tWhen we are reading (-r): Full: See all CSV    yyyy-mm-dd: Exactly date to see\n"
        "\tWhen we are wrinting (-w): In this case we add 4 more arguments. The position is:\n"
            "\t\t-c: concept  'Concept'   -v: value   'earn/spend money'\n"
        "\tWhen we are calculating average: yyyy-mm-dd: Exactly date to calculate\n"

    "\nReading example: python project.py -r Full\n"
    "\tpython project.py -r 2025-08-02\n"
        
    "\nWriting example: python project.py -w -c Nomina -v 2000\n"

    "\nAverage example: python project.py -a 2025-08-06\n"
    
    )


if __name__ == "__main__":
    main()