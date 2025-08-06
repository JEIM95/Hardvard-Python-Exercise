import csv
import sys
from datetime import date

"""
    This project enables you to track and store your financial transactions in a CSV file. 
    Based on your input, you can update your name, record income, expenses, and other financial activities.
    Para ejecutar el programa debemos hacer lo siguiente. Python projec.py + argumentos
    First argument: -r: Read  -w: Write  -a: Average
    Second argument: 
        When we are reading (-r): Full: See all CSV    yyyy-mm-dd: Exactly date to see 
        When we are wrinting (-w): In this case we add 4 more arguments. The position is:
            -c: concept  "Concept"   -v: value   "earn/spend money"
        When we are calculating average: yyyy-mm-dd: Exactly date to calculate

        Reading example: python project.py -r Full
                         python project.py -r 2025-08-02 (Muestra el de ese día)
        
        Writing example: python project.py -w -c Nomina -v 2000

        Average example: python project.py -a 2025-08-06
"""
#Variables globales
financials = []

def main():
    global financials

    if len(sys.argv) < 2:
        sys.exit("Few arguments")
    else:
        if not sys.argv[1] == "-r" and not sys.argv[1] == "-w" and not sys.argv[1] == "-a":
            sys.exit("First argument is not -r, -w or -a")
        else:
            #Reading calculate
            if sys.argv[1] == "-r" and len(sys.argv) == 3:
                #Check keyword is correct
                Result_reading = Check_reading_values(sys.argv[2].capitalize())

                if Result_reading == True:
                    match sys.argv[2].capitalize():
                        case "Full":
                            Save_CSV() #Save CSV in list of dictionary
                            Show_CSV("Full") #Show CSV
                        case _:
                            Save_CSV()
                            Show_CSV(sys.argv[2])
            elif sys.argv[1] == "-r" and len(sys.argv) != 3:
                sys.exit("argument no valid")

            #Writing calculate
            elif sys.argv[1] == "-w" and len(sys.argv) == 6:
                Result_writing = Check_writing_values(sys.argv[2], sys.argv[4], sys.argv[5])
                if Result_writing == True:
                    Write_CSV(sys.argv[3], sys.argv[5]) #Concept, value

            elif sys.argv[1] == "-w" and len(sys.argv) != 6:
                sys.exit("argument no valid")
            
            #Average calculate
            elif sys.argv[1] == "-a" and len(sys.argv) == 3:
                Result_average = Check_date(sys.argv[2])
                if Result_average == True:
                    average = arithmetic_mean(sys.argv[2])
                    print(f"The arithmetic mean in date: {sys.argv[2]} is: {average}")
            elif sys.argv[1] == "-a" and len(sys.argv) != 3:
                sys.exit("argument no valid")

    #Función para escribir en el CSV
    #Write_CSV(concept, valor)

#save CSV in list of dictionery
def Save_CSV():
    global financials
    financials = []

    with open("financial.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            financials.append({"fecha": row["fecha"], "concepto": row["concepto"], "ingresos/gastos": row["ingresos/gastos"], "balance": row["balance"]})
  
#Show CSV
def Show_CSV(x):
    global financials
    find = False

    if x == "Full":
        for financial in financials:
            print(f"fecha: {financial["fecha"]}, Concepto: {financial["concepto"]}, ingresos/gastos: {financial["ingresos/gastos"]}, balance: {financial["balance"]}")
    else:
        for financial in financials:
            if financial["fecha"] == x:
                find = True
                print(f"fecha: {financial["fecha"]}, Concepto: {financial["concepto"]}, ingresos/gastos: {financial["ingresos/gastos"]}, balance: {financial["balance"]}")
        if find == False:
            print(f"No movements this day: {x}")   

#Wite in CSV
def Write_CSV(concept, n):
    global financials
    #Save CSV in list of dictionary
    Save_CSV()
    
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
                    "fecha":date_today, 
                    "concepto":concept, 
                    "ingresos/gastos":valor, 
                    "balance":total
                }
            )
    with open("financial.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=["fecha", "concepto", "ingresos/gastos", "balance"])
        
        writer.writeheader()
        writer.writerows(financials)

#Checking arguments when you want read CSV
def Check_reading_values(x):
    valid = False

    if x == "Full":
        valid = True
    elif not x == "Full":
       valid = Check_date(x)
    
    return valid


def Check_date(x):
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
def Check_writing_values(a, b, c):
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
    
    Save_CSV()

    find = False
    list_money = []

    for financial in financials:
        if financial["fecha"] == a:
            find = True
            list_money.append(financial["ingresos/gastos"])
    
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



if __name__ == "__main__":
    main()