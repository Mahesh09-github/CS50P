def main():
    print(f"Amount due: 50")
    due()


def due():
    amount_due=50
    cents=[25,10,5]
    while amount_due>0:
            insert_coin=int(input("Insert Coin: "))
            if  insert_coin in cents:
                amount_due-=insert_coin
                if amount_due>0:
                     print(f"Amount Due: {amount_due}")
            else:
                print(f"Amount due: {amount_due}")
    if amount_due<0:
         print(f"Change Owed: {abs(amount_due)}")
    else:
         print("Change owed: 0")
     
main()