import csv
import sys
from datetime import date

"""
    This project enables you to track and store your financial transactions in a CSV file. 
    Based on your input, you can update your name, record income, expenses, and other financial activities.
    Para ejecutar el programa debemos hacer lo siguiente. Python projec.py + argumentos
    El primer argumento: -r: Lectura  -w: Escritura
    El segundo argumento: 
        Si estamos en lectura (-r): Full: Ver todo el CSV    yyyy-mm-dd: Fecha concreta para ver desde ahí en adelante
        Si estamos en escritura (-w): En este caso tenemos que añadir 4 argumentos más. El orden es el siguiente:
            -c: concepto  "El concepto que queremos"   -v: valor   "Ingreso/gasto que queremos meter"

        Ejemplo de lectura: python project.py -r Full
                            python project.py -r 2025-08-02 (Muestra el de ese día)
        
        Ejemplo de escritura: python project.py -w -c Nomina -v 2000
"""
#Variables globales
financials = []

def main():
    global financials

    if len(sys.argv) < 2:
        sys.exit("Few arguments")
    else:
        if not sys.argv[1] == "-r" and not sys.argv[1] == "-w":
            sys.exit("First argument is not -r or -w")
        else:
            if sys.argv[1] == "-r" and len(sys.argv) == 3:
                #Check keyword is correct
                Result = Check_reading_values(sys.argv[2].capitalize())

                if Result == True:
                    match sys.argv[2].capitalize():
                        case "Full":
                            Save_CSV() #Save CSV in list of dictionary
                            Show_CSV("Full") #Show CSV
                        case _:
                            Save_CSV()
                            Show_CSV(sys.argv[2])
            elif sys.argv[1] == "-r" and len(sys.argv) != 3:
                sys.exit("argument no valid")


            elif sys.argv[1] == "-w" and len(sys.argv) == 6:
                print("Entre en lectura")
            elif sys.argv[1] == "-w" and len(sys.argv) != 6:
                sys.exit("argument no valid")

    #concept = input("Introduce el concepto: ")
    #valor = input("Introduce ingresos/gastos: ")

    #Comprobamos que el valor introducido es un número
    #Control_input_number(valor)

    #Función para escribir en el CSV
    #Write_CSV(concept, valor)


def Save_CSV():
    global financials
    financials = []

    with open("financial.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            financials.append({"fecha": row["fecha"], "concepto": row["concepto"], "ingresos/gastos": row["ingresos/gastos"], "balance": row["balance"]})
  

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


def Write_CSV(concept, n):
    global financials
    #Primero guardar CSV en lista de diccionarios
    #Read_CSV()
    
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


def Control_input_number(x):
    try:
        numero = int(x)
    except ValueError:
        sys.exit("Value is not a number")


def Check_reading_values(x):
    valid = False

    if x == "Full":
        valid = True
    elif not x == "Full":
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



if __name__ == "__main__":
    main()