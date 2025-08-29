months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            User_input=input("Date: ")
            if " " in User_input:
                User_input=User_input.replace(" ",",")
            else:
                pass
            # 08/09/1636
            # August 9,1636
            if "/" in User_input:
                month,day,year=User_input.split("/")
                if month.isdigit():
                    month=int(month)
                    if month<13:
                        pass
                    else:
                        continue
                else:
                    month=month.capitalize()
                    month=months.index(month)+1
                    month=int(month)
                day=int(day)
                if day<31:
                    print(f"{year}-{month:02}-{day:02}") # year/month/day
                else:
                    pass
            else:
                month,day,year=User_input.split(",")
                if month.isdigit():
                    month=int(month)
                else:
                    month=month.capitalize()
                    month=months.index(month)+1
                    month=int(month)
                    if month<13:
                        pass
                    else:
                        continue
                day=int(day)  
                if day<31:
                    print(f"{year}-{month:02}-{day:02}") # year/month/day
                else:
                    pass 
                
        except (ValueError,KeyError):
            continue
main()