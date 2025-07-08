import random

Score = 0

def main():
    Level_input = get_level()
    
    for i in range(10):
        sum_1, sum_2 = generate_integer(Level_input)
        
        correct = False
        count = 0
        result = 0

        while correct == False and count < 3:
            result = sum_1 + sum_2
            global Score
            try:
                result_user = int(input(f"{sum_1} + {sum_2} = "))

                if result_user == result:
                    Score = Score + 1
                    correct = True
                else:
                    print("EEE")
                    count = count + 1
            except ValueError:
                print("EEE")
                count = count + 1

        if count == 3:
            print(sum_1, " + ", sum_2, " = ", result)

    print("Score: ", Score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                raise ValueError
    
        except ValueError:
            pass
        else:
            break
    return level

def generate_integer(level):
    if level == 1:
        a = 0
        b = 9
    elif level == 2:
        a = 10
        b = 99
    elif level == 3:
        a = 100
        b = 999

    x = random.randint(a,b)
    y = random.randint(a,b)
    return x,y

if __name__=="__main__":
    main()