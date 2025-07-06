def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    Check_1 = False
    Check_2 = False
    Check_3 = False
    Check_4 = False

    caracters = len(s)

    #Check if start with at least two letters
    if caracters == 1:
        Check_1 = False
    else:
        if s[0].isalpha() and s[1].isalpha():
            Check_1 = True
        else:
            Check_1 = False

    #Number of caracters

    if caracters > 1 and caracters < 7:
        Check_2 = True
    else:
        Check_2 = False

    #Number not start 0 and End number or all letters and numbers in middel
    numbers = "0123456789"
    valor_number = ""

    for n in s:
        for x in numbers:
            if n == x:
                valor_number = valor_number + n


    if valor_number == "":
        Check_3 = True
    elif s[caracters - 3].isalnum() == True and s[caracters - 2].isalpha() and s[caracters - 1].isalnum():
        Check_3 = False
    elif s[caracters - 1].isalpha() == True or valor_number[0] == "0":
        Check_3 = False
    else:
        Check_3 = True

    #punctuation marks
    if s.isalnum():
        Check_4 = True
    else:
        Check_4 = False

    #Check results
    if Check_1 == True and Check_2 == True and Check_3 == True and Check_4 == True:
        Valid = True
    else:
        Valid = False

    return Valid

main()