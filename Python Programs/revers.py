num = int(input())
temp = num
reverse = 0
while (num > 0):
    remain = num % 10
    reverse = (reverse*10) + remain
    num =num // 10

print(reverse)
