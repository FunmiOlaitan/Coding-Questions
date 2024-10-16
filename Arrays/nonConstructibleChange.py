def nonConstructibleChange(coins):
    coins.sort
    current_change = 1
    for coin in coins:
        if coin > current_change:
            break
        current_change += coin
    return current_change