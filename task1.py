def orders_n(, cost):
    i = []
    for a in n:
        if a > cost:
            i.append(a)
    return orders_n

n = [10, 6, 50, 3, 8]
cost = 5
i = orders_n(n, cost)
print(f"orders greater than ${cost}: {i}")
