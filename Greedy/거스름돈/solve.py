a = int(input())
an = 0

if (a >= 500):
    n = a // 500
    a = a - (n * 500)
    an = an + n

if (a >= 100):
    n = a // 100
    a = a - (n * 100)
    an = an + n

if (a >= 50):
    n = a // 50
    a = a - (n * 50)
    an = an + n

if (a >= 10):
    n = a // 10
    a = a - (n * 10)
    an = an + n

print(an)