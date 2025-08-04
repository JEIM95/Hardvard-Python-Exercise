prize_coke = 50

print ("Amaunt Due: ", prize_coke)

while prize_coke > 0:
    coin = int(input())

    match coin:
        case 25:
            prize_coke = prize_coke - 25
        case 10: 
            prize_coke = prize_coke - 10
        case 5:
            prize_coke = prize_coke - 5   
    
    if prize_coke <= 0:
        print("Change Owed:", abs(prize_coke))
    else:
        print("Amount Due:", prize_coke)


#Insert Coin: 