def main():
    #Asking the user to prompt total bill
    Dollar=dollar_to_float(input("Enter the Total Bill: "))
    #Asking the user to promt percentage of Tip 
    percent=percent_to_float(input("Enter the percent of Tip: "))
    Tip=Dollar*percent
    print(f"Leave ${Tip:.2f}")

def dollar_to_float(x):
    x=float(x.replace("$","").strip())
    return x

def percent_to_float(y):
    y=float(y.replace("%",""))
    y=y/100
    return y

main()