def reverse(n):
    hasil = 0
    while n > 0:
        hasil = hasil * 10 + (n % 10)
        n //= 10
    return hasil

A, B = map(int, input().split())
A = reverse(A)
B = reverse(B)
C = A + B
print(reverse(C))