num = 5

for i in range(2, num//2):
    if num % i == 0:
        print(num, 'is not prime')
        break
else:
    print(num, 'is prime')

for i in range(1, 20):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
