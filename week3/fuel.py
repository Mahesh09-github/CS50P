def main():
    while True:
        try:
            User_input=input("Fraction: ")
            x,y=User_input.split("/")
            x=int(x)
            y=int(y)
            if y>x>0:
                value=(x/y)*100
                value=round(value)
                if value<=1:
                    print("E")
                    break
                elif 99<=value:
                    print("F")
                    break
                else:
                    print(f"{value}%")
                    break
            else:
                continue
        except (ValueError,ZeroDivisionError):
            print("Invalid Inputs")
            continue
main()


