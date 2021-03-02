bil = int(input("Masukkan bilangan : "))
if bil > 1:
    for i in range(2, bil):
        if (bil % i) == 0:
            print(bil, "bukan bilangan prima")
            break
    else:
        print(bil,"adalah bilangan prima")
else:
    print(bil, "bukan bilangan prima")
