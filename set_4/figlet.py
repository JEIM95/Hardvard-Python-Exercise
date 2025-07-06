from pyfiglet import Figlet
import sys

Exist = False

fonts = Figlet().getFonts()

if len(sys.argv) < 2:
    text = input("Input: ")
    f = Figlet(font="slant")
    print(f.renderText(text))
else:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    
    for font in fonts:
        if font == sys.argv[2]:
            Exist = True

    if Exist == True:
        text = input("Input: ")
        f = Figlet(font=sys.argv[2])
        print(f.renderText(text))
    else:
        sys.exit("Invalid usage")

    
    

