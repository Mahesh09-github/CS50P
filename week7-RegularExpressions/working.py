import re
import sys


def main():
    print(convert(input("Hours: ")))
    #9:00 AM to 5:00 PM
    #9 AM to 5 PM

def convert(s):
    if match:= re.search(r'^([0-9]|1[0-2]):?([0-9]{2})?\s(AM|PM) to ([0-9]|1[0-2]):?([0-9]{2})?\s(AM|PM)$',s):
        if ((match.group(2) is None or int(match.group(2)) <60)and (match.group(5) is None or int(match.group(5)) <60)):
            return f'{int(match.group(1)) + (12 if match.group(3) == "PM" and match.group(1) != "12" else 0):02}:{match.group(2) if match.group(2) else "00"} to {int(match.group(4)) + (12 if match.group(6) == "PM" and match.group(4) != "12" else 0):02}:{match.group(5) if match.group(5) else "00"}'
        else:
            raise ValueError("Minutes must be less than 60")
    raise ValueError("Invalid format")
        
    


...


if __name__ == "__main__":
    main()