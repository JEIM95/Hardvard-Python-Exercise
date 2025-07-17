def main():
   
    value = input("Fraction: ")

    try:
        value_percen = convert(value)
        text = gauge(value_percen)
        print(text)

    except ValueError:
        print("ValueError")
        
    except ZeroDivisionError:
        print("ZeroDivisionError")

          
                                  
def convert(fraction):
    x, y = fraction.split("/")
    x_num = int(x)
    y_num = int(y)
    result = round(float((x_num/y_num)*100))
    return result

def gauge(percentage):
    if percentage <= 1:
        text_percen = "E"
    elif percentage >=99 and percentage <=100:
        text_percen = "F"
    elif percentage > 1 and percentage < 99:
        text_percen = str(percentage)+"%"

    return text_percen

if __name__ == "__main__":
    main()