# Example usage:
a = [3, 4, 5, 3, 6, 7, 8, 6, 9]

n = 0

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        n += 1

print(n)
