def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins_list = [100, 25, 50]
coins_dict = {"galleons": 100, "sickles": 25, "knuts": 50}

# print(total(coins[0], coins[1], coins[2]), "Knuts")
print(total(*coins_list), "Knuts")
print(total(**coins_dict), "Knuts")