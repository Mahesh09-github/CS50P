import inflect
names=[]
p=inflect.engine()
def main():

    try:
        while True:
            user_input=input("Name: ")
            names.append(user_input)
    except EOFError:
        print("Adieu, adieu, to",p.join(names))

main()  