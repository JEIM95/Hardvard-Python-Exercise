#Make funtions
def main():
    #Check correct values
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x_num = int(x)
            y_num = int(y)
           
            number = percentage(x_num, y_num)

            if number <= 1:
                print("E")
            elif number >=99 and number <=100:
                print("F")
            elif number > 1 and number < 99:
                print(str(number)+"%")
            else:
                raise Exception
                
        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except Exception :
            pass
        else:
            break

def percentage(x,y):
    result = round(float((x/y)*100))
    return result

main()