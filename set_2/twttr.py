element = input("Input: ")

vowels = ("aeiouAEIOU")

solution = ""

for n in element:

    letter = False

    for x in vowels:
        if n == x:
            letter = True

    if letter == False:
        solution = solution + n
    else:
        solution = solution + ""


print ("Output:", solution)
