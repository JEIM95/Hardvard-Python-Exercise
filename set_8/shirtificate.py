from fpdf import FPDF
from PIL import Image

def main():
    name_user = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    #Select style letters to title
    pdf.set_font("Times", size=50, style="B")
    pdf.text(45, 60, "CS50 Shirtificate")

    #Open and position Image
    with Image.open("shirtificate.png") as im:
        pdf.image(im, 15, 80 , 180)
   
    #Select style letters to logo t-shirt
    pdf.set_text_color(255,255,255) #white color to text
    pdf.set_y(15)
    pdf.set_font("Times", size=25, style="B")
    pdf.cell(0, 250, name_user, border=0, align="C")
    
    pdf.output("shirtificate.pdf")

main()