import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    Result = "Mala"
    pattern = r"^(?P<hour1>[0-9]?[0-9]|1[0-2])(:[0-5][0-9])? (?P<ampm1>AM|PM) to (?P<hour2>[0-9]?[0-9]|1[0-2])(:[0-5][0-9])? (?P<ampm2>AM|PM)$"
    
    match = re.search(pattern, s)

    if match:
        if match.group("ampm1") == "PM":
           hour1_24 = twenty_four_hours(match.group("hour1"))
        else:
            if int(match.group("hour1")) < 10:
                hour1_24 = "0" + match.group("hour1")
            else:
                if match.group("hour1") == "12":
                    hour1_24 = "00"
                else:
                    hour1_24 = match.group("hour1")

        if match.group("ampm2") == "PM":
           hour2_24 = twenty_four_hours(match.group("hour2"))
        else:
             if int(match.group("hour2")) < 10:
                hour2_24 = "0" + match.group("hour2")
             else:
                if match.group(5) == "12":
                    hour2_24 = "00"
                else:
                    hour2_24 = match.group("hour2")
        
        if match.group(2):
            minute1 = match.group(2)
        else:
            minute1 = ":00"
        
        if match.group(5):
            minute2 = match.group(5)
        else:
            minute2 = ":00"
    #Combine hours + minutes
        Result = f"{hour1_24}{minute1} to {hour2_24}{minute2}"
    else:
        raise ValueError
    
    return Result


def twenty_four_hours(h):
    h = int(h)
    if h < 12:
        f_hour = h + 12
    else:
        f_hour = "12" 
    return str(f_hour)


if __name__ == "__main__":
    main()