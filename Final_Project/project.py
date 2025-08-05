import csv
import sys
from datetime import date

"""
    This project enables you to track and store your financial transactions in a CSV file. 
    Based on your input, you can update your name, record income, expenses, and other financial activities.
"""
#Variables globales
financials = []

def main():
    global financials

    #Función para guarda CSV en una lista de diccionarios
    Read_CSV()

    for financial in financials:
        print(f"fecha: {financial["fecha"]}, Concepto: {financial["concepto"]}, ingresos/gastos: {financial["ingresos/gastos"]}, balance: {financial["balance"]}")

    concept = input("Introduce el concepto: ")
    valor = input("Introduce ingresos/gastos: ")

    #Comprobamos que el valor introducido es un número
    Control_input(valor)

    Write_CSV(concept, valor)

def Read_CSV():
    global financials
    financials = []

    with open("financial.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            financials.append({"fecha": row["fecha"], "concepto": row["concepto"], "ingresos/gastos": row["ingresos/gastos"], "balance": row["balance"]})
  

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


def Control_input(x):
    try:
        numero = int(x)
    except ValueError:
        sys.exit("Value is not a number")
       


if __name__ == "__main__":
    main()