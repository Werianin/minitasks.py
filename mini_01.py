
n = int(input())
count = 0
value = 1
if (n < 0):
    count += 1
    n = -n - 1
    value = 0
while (n > 0):
    if (n % 2 == value):
        count += 1
    n //= 2
print(count)
