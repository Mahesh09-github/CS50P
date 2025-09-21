import random
import sys
def main():
    try:
        while True:
            user_input=int(input("level: "))
            if user_input>0:
                num=random.randint(1,user_input)
                print(num)
                guess=int(input("Guess: "))
                if guess>0:
                    if guess == num:
                        print("Right!!")
                        sys.exit()
                    elif guess < num:
                        print("Too small!")
                    elif guess > num:
                        print("Too Big!")
            
    except ValueError:
        pass

main()