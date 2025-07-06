variable = input("camelCase: ")

if variable.islower() == True:
    print(variable)
else:
    result = ""

    for x in variable:
        if x.isupper() == True:
            result = result + "_" + x.lower()
        else:
            result = result + x

    print (result)


