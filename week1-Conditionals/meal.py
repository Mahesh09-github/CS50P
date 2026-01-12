def main():
    time_str=input("Enter the time: ")
    time=convert(time_str)
    print(meal(time))

def meal(time):
    if 7<=time<=8:
        return "Breakfast Time"
    elif 12<=time<=13:
        return "Lunch Time"
    elif 18<=time<=19:
        return "Dinner Time"
    else:
        return "Snack Time"

def convert(time):
    hours,minutes=map(int,time.split(":"))
    return hours+minutes/60

if __name__ == "__main__":
    main()
