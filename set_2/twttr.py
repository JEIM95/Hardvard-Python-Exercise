def main():
    element = input("Input: ")
    
    solution = ""

    solution = shorten(element)
    print ("Output:", solution)

def shorten(word):
    solution = ""
    vowels = ("aeiouAEIOU")

    for n in word:
        letter = False

        for x in vowels:
            if n == x:
                letter = True

        if letter == False:
            solution = solution + n
        else:
            solution = solution + ""
    
    return solution

if __name__ == "__main__":
    main()









