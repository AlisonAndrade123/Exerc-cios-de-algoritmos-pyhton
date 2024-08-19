def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1) 

num = int(input())
while num != -1:
    print(fatorial(num))
    num = int(input())
