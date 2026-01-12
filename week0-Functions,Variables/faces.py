def main():
    #Ask user to prompt about his/her day
    User_input=input("Tell me about  your day: ")
    print(convert(User_input))

def convert(change):
    change=change.replace(":)","🙂")
    change=change.replace(":(","😐")
    return change

main()
