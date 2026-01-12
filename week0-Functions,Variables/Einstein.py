def main():
    m=int(input("Enter the mass m: "))
    print(f"E:{energy(m)}")

def energy(m):
    c=300000000
    E=(m*(c**2))
    return E
