import os

def main():
    maxdnm = 99999999
    montant = int(input("Enter the amount: "))
    dnm = input("Enter coin values, separated by spaces: ")
    dy = [maxdnm] * (montant + 1)
    dy[0] = 0
    denominations = list(map(int, dnm.split()))

    for denomination in denominations:
        for i in range(denomination, montant + 1):
            dy[i] = min(dy[i], dy[i - denomination] + 1)

    if dy[montant] < maxdnm:
        print(f"Minimum number of coins required : {dy[montant]}")
    else:
        print("Minimum number of coins required : -1")

    input("Press Enter to Continue")
    clear()


def clear():
    os.system("cls" if os.name == "nt" else "clear")
    main()


if __name__ == "__main__":
    main()
