from datetime import date
import inflect
import sys

def main():
    components = []
    components_int = []
    p = inflect.engine()

    birth = input("Date of Birth: ")

    #Check and convert date to int
    components = check_date(birth)
    components_int = convert_int(components)

    #Create object date
    object_date = date(components_int[0], components_int[1], components_int[2])
    today = date.today()
    day_of_year_birth = object_date.timetuple() #Da una tupla con información. Interesa puesto 7. Dia del año
    day_of_current_day = today.timetuple() 

    #Primero ver los años completos
    total_year = today.year - object_date.year - 1
    
    #De los completos cuantos son bisiestos
    total_year_leap = 0
    for n in range(1, total_year + 1):
        year = object_date.year + n #Calculamos el año
        year_leap = leap_year(year) #Llamamos a la función 
        if year_leap == True:
            total_year_leap += 1

    #Número total de años no bisiestos        
    No_leap_year = total_year - total_year_leap
    
    #Luego comprobar si año nacimiento es bisiesto y días de ese año
    year_leap_birth = leap_year(object_date.year)
    if year_leap_birth == True:
        n_days_birth = 366 - day_of_year_birth[7]
    else:
        n_days_birth = 365 - day_of_year_birth[7]
    
    #Calculamos el número total de días y los minutos que son
    total_days = (No_leap_year * 365) + (total_year_leap * 366) + n_days_birth + day_of_current_day[7] 
    total_minutes = total_days * 24 * 60
    print(f"{p.number_to_words(total_minutes).capitalize()} minutes")

def check_date(date):
    valid = False
    components = []
    components = date.split("-")
    
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
    
    if valid == True:
        return components

def convert_int(date):
    valor = []
    for n in range(0, len(date)):
        valor.append(int(date[n]))
    return valor

def leap_year(x): #Check if the year is leap year
    leap_year_ok = False
    if (x % 4 == 0 and x % 100 == 0 and x % 400 == 0) or (x % 4 == 0 and x % 100 != 0):
        leap_year_ok = True
    else:
        leap_year_ok = False
    return leap_year_ok



if __name__ == "__main__":
    main()