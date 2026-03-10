def fibonacci_ke_n(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def cetak_fibonacci(n):
    a, b = 0, 1
    print("berat fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Masukkan nilai n:"))

print("fibonacci ke-", n, "-", fibonacci_ke_n(n))

cetak_fibonacci(n)
