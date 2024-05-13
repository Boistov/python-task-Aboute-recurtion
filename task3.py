a = input ()

words = a.split()

num = []
for word in words:
    if len(word) > 4:
        num.append('*' * len(word))
    else:
        num.append(word)

num = ' '.join(num)
print(num)
