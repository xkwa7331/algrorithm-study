import os


    
def main():
    maxdnm = 99999999
    montant = float(input("Put Amount here: "))
    dnm = float(input("Enter Coin Values, each one separated by a Space: "))
    dy = [maxdnm] * (montant + 1)
    input_list_str = dnm.split()
    dy[0] = 0
    denominations = [float(item) for item in input_list_str]
    for denominations in denominations:
        dy[denominations] = 1
    for i in range(1, montant + 1):
        if dy [i] == 1:
            continue
    count = maxdnm
    for j in range(1, i // 2 + 1):
        if count > dy[i] + dy[i-j]:
            count = dy[j] + dy[i-j]
        dy[i] = count
    print(dy[montant] if count < maxdnm else -1)
    print(dy)
    input("Press Enter to Continue")
    clear()
    
def clear():
    os.system('cls')
    main()

if __name__ == "__main__":
    main()
    os.system('cls')

