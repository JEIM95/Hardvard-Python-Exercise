import requests
import sys
import json


def main():
    n_bitcoin = 0
    result = 0
    #Check user introduce correct format
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        try:
            number = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    
    #Call API
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=edaf4182d5c33e661e400a54521ac353707ff59b6d4331b694519f3307714343")
    #print(json.dumps(response.json(), indent=2))

    o = response.json()
    price_bitcoin = o["data"]["priceUsd"]

    n_bitcoin = float(sys.argv[1])
    result = n_bitcoin * float(price_bitcoin)
    print(f"${result:,.4f}")


main()



