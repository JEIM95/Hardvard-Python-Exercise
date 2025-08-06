import sys
from PIL import Image, ImageOps

def main():
    correct = check_arguments(sys.argv)
    
    if correct == True:
        try:
            with Image.open(sys.argv[1]) as person, Image.open("shirt.png") as shirt:
                shirt = shirt.convert("RGBA")
                person = person.convert("RGBA")
                
                reescalate_person = ImageOps.fit(person, shirt.size)

                reescalate_person.paste(shirt, shirt)
                reescalate_person = reescalate_person.convert("RGB")
                reescalate_person.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("File does not exist")  

def check_arguments(argument):
    Solution = False
    if len(argument) < 3:
        sys.exit("Too few command-line arguments")

    elif len(argument) > 3:
        sys.exit("Too many command-line arguments")
        
    elif not argument[1].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    
    #Check same extension
    extension1 = argument[1].split(".")[1] #Esto hace que solo guarde la segunda parte
    extension2 = argument[2].split(".")[1]

    if extension1 != extension2:
        sys.exit("Input and output have different extension")
        
    Solution = True
    return Solution   

main()