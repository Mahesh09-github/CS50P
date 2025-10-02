def main():
    User_input=input("Enter a fraction: ")
    print(guage(convert(User_input)),"%",end="")

def convert(fraction):
    x,y=fraction.split("/")
    x=int(x)
    y=int(y)
    if y>x>0:
        return x/y
    
def guage(percentage):
    percentage*=100
    percentage=round(percentage)
    if percentage<=1:
        return "Empty!!"
    elif 99<=percentage:
        return "Full!!"
    else:
        return percentage
    
if __name__ == "__main__":
    main()