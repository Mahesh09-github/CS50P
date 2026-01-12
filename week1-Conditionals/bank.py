#creating a main function where all main code is present
def main():
    #asking user to promt a  greet
    greet=input("Greeting : ")
    print(greeting(greet))

def greeting(n):
    n=n.lower().strip()
    if n=="hello":
        return "$0"
    elif n.startswith("h"):
          return "$20"
    else:
         return "$100"

if __name__ == "__main__":
    main()