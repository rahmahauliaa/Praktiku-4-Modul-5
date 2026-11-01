def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)

a, c, b, d = map(int, input().split())
result = hitung(a, b) + hitung(c, d)
print(mutlak(result))