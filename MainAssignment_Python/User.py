import Bms
e = {}
l = []

def user():
    print("welcome {}".format(Bms.name))
    l = 1
    p = []
    for k in e:
        print("{} : {}".format(l, k))
        p.append(k)
        l += 1
        f = int(input("Enter Movie: "))
        h = p[f - 1]
        for b in e[h]:
            print(b)