file = input("File name: ")

file = file.strip()
file = file.replace(" ", "")
caracters = len(file)

if "." in file:
    valor = 1
    extension = ""
    while file[caracters - valor] != ".":
        extension = file[caracters - valor] + extension
        valor = valor + 1

    extension= extension.lower()

    match extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
