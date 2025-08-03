def main():
    time_str=input("Enter the time: ")
    time=convert(time_str)
    if 7<=time<=8:
        print("Breakfast Time")
    elif 12<=time<=13:
        print("Lunch Time")
    elif 18<=time<=19:
        print("Dinner Time")
    else:
        return

def convert(time):
    hours,minutes=map(int,time.split(":"))
    return hours+minutes/60

if __name__ == "__main__":
    main()
