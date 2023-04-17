num = 5

for i in range(num, 2, -1):
    div = i -1
    if num % div == 0:
        print(False)
        break
print(True)