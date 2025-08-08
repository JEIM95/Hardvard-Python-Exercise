def main():
    moment = input("What time is it?")

    time = convert(moment)

    if 7.0 <= time <= 8.0:
        print("Breakfast time")
    elif 12.00 <= time <= 13.00:
        print("Lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(x):
    hour, minute = x.split(":")
    #Convert to float
    num_hour = float(hour)
    num_minute = float(minute)

    #Change format 59-99
    m = (100*num_minute)/60

    time = num_hour + (m / 100)
    return time

if __name__== "__main__":
    main()
