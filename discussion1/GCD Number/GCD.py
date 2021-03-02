def gcd(x, y):
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)
x =int (input ("Masukkan bilangan pertama : ")) 
y =int (input ("Masukkan bilangan kedua : ")) 
bil = gcd(x, y) 
print("Faktor persekutuan terbesarnya adalah ", bil)
