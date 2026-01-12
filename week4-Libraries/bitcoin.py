import requests
import json
import sys
def main ():
    try:
        num=sys.argv[1]
        num=float(num)
        request=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e8944ab9eec87dde6e0fa4fda7aa27beda8754dae3ec4fc1412054c0fe818c0b")
        content=request.json()
        price=float(content["data"]["priceUsd"])
        cost=num*price
        print("Present Price/bitcoin: ",price)
        print(f"${cost:,.4f}")  
    except ValueError:
        sys.exit("Command-Line Argument can't be converted to Float")
    except IndexError:
        sys.exit("Missing Command-Line Argument")
    except requests.RequestException:
        print("Sorry,request not met")

main()