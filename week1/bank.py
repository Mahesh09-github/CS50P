#creating a main function where all main code is present
def main():
    #asking user to promt a  greet
    greet=input("Greeting : ")
    check(greet)

def check(n):
    n=n.lower().strip()
    if n=="hello":
        print("$0")
    elif n.startswith("h"):
          print("$20")
    else:
         print("$100")

main()