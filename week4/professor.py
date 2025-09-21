import random
def main():
    x,y=0,0
    while True:
        score=0
        try:
            life=3
            level=get_level()
            for num in range(1,11):
                x=generate_integer(level)
                y=generate_integer(level)
                while True:
                    solution=int(input(f"{x} + {y} = "))
                    if  solution == sum(x,y):
                        score+=1
                        break
                    elif solution != sum(x,y):
                        life-=1
                        print("EEE")
                        if life == 0:
                            print(f"{x} + {y} = {sum(x,y)}")
                            break
                print("Score:",score)
        except EOFError:
            print("Score:",score)

def get_level():
    while True:
        level=int(input("Level: "))
        if level in (1,2,3):
            return level

def generate_integer(n):
    if n == 1:
        return int(random.randint(1,10))
    elif n == 2:
        return int(random.randint(1,50))
    elif n == 3:
        return int(random.randint(1,100))

def sum(a,b):
    c=0
    c=int(a+b)
    return c


if __name__ == "__main__":
    main()