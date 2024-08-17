def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        temp_insert = int(input("Insert Coin: "))
        if temp_insert == 25 or temp_insert == 10 or temp_insert == 5:
            amount_due -= temp_insert
    print("Change Owed:", amount_due*-1)

main()