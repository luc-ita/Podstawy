def f(n):
    a = 0
    b = 1

    for i in range(1,n):
        c = a
        a = b
        b = a+c
    return a

print(f(5))
print(f(9))