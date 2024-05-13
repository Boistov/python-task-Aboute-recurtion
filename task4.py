n = int(input())
message = str(input())

a = [str(i) + "." for i in range(n, 0, -1)]

num = " ".join(a)
num += f" {message}!"

print(num)


