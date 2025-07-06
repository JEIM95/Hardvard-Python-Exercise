#Dictionary to check months
months = {"January" : "01",
          "February" : "02",
          "March" : "03",
          "April" : "04",
          "May" : "05",
          "June" : "06",
          "July" : "07",
          "August" : "08",
          "September" : "09",
          "October" : "10",
          "November" : "11",
          "December" : "12"}

def AnnoDomini (Array):
    for i in range(len(DateList)):
        if len(DateList[i]) < 2:
            DateList[i] = "0" + DateList[i]
    FinalDate = Array[2] + "-" + Array[0] + "-" + Array[1]
    print(FinalDate)

def CheckDayMonth (Array):
    CorrectDay = False
    CorrectMonth = False
    CorrectDate = False

    if int(Array[1]) < 32:
        CorrectDay = True
    
    if int(Array[0]) < 13:
        CorrectMonth = True

    CorrectDate = CorrectDay * CorrectMonth

    return CorrectDate

date = ""
DateList = ""

#Ask to introduce date
while True:
    try:
        date = input("Date: ").strip()
         
        if "/" in date:
            DateList = date.split("/")

            Checking = CheckDayMonth(DateList)
            if Checking == True:
                AnnoDomini(DateList)
            else:
                raise KeyError
          
        else:
            DateList = date.split(" ")

            #Change name to number
            DateList[0] = months[DateList[0]]

            #Delete comma
            DateList[1], comma = DateList[1].split(",")

            Checking = CheckDayMonth(DateList)
            if Checking == True:
                AnnoDomini(DateList)
            else:
                raise KeyError
              
    except KeyError:
        pass
    except ValueError:
        pass
    else:
        break


    




