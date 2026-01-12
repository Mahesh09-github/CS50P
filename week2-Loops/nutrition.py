fruits={
    "Apple":130,
    "Avocado":50,
    "Banana":110,
    "Cantaloupse":50,
    "Grapefruit":60,
    "Grapes":90,
    "Honey Melon":50,
    "kiwifruit":90,
    "Lemon":15,
    "Lime":20,
    "Nectarine":60,
    "Orange":80,
    "Peach":60,
    "Pineapple":100,
    "Pines":50,
    "Plum":70,
    "Strwberries":50,
    "Tangerien":100,
    "Sweet Cherries":50,
    "Watermelon":80
    }
def main():
    item=input("ITEM: ")
    item=item.title()
    calories(item)

def calories(v):
    if v in fruits:
        print("CALORIES:",fruits[v])
    else:
        return
main()