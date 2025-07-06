import inflect
p = inflect.engine()

name = []

while True:
    try:
        name.append(input("Name: "))
    except EOFError:
        break

print("Adieu, adieu, to ", p.join((name), final_sep=""))









