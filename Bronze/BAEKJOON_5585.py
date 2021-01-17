def get_coin_num(coins, value):
    value = 1000 - value

    total_coin = 0
    
    for coin in coins:
        total_coin += value // coin
        value = value % coin

    return total_coin

n = int(input())

coins = [500, 100, 50, 10, 5, 1]



print(get_coin_num(coins, n))
