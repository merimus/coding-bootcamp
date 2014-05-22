
coins = [200, 100, 50, 20, 10, 5, 2, 1]

def change(value, coin):
    if coin == 7:
        return 1
    possible = value / coins[coin]
    sum = 0
    for i in range(0, possible+1):
        sum += change(value - coins[coin]*i, coin+1)
    return sum

print change(200, 0)
