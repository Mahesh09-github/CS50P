'''In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
 formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
 Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
   Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.'''
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