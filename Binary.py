def binOne(number):
    fin = ""
    put = number
    i = 0
    while pow(2, i) <= put:
        i = i + 1
    i = i - 1
    put = put - pow(2, i)
    fin = "1"

    prev = i
    while put > 0:
        sub = prev
        k = 0
        while pow(2, k) <= put:
            k = k + 1
        k = k - 1
        put = put - pow(2, k)

        while sub - 1 > k:
            fin = fin + "0"
            sub = sub - 1
        fin = fin + "1"
        prev = k

    print(fin)


def binTwo(number):
    """"Binary Two Function"""
    put = number
    fin = 0

    k = 0
    lengths = len(put)
    for i in range(len(put)):
        if put[lengths - i - 1] == "1":
            fin = fin + pow(2, k)
        k = k + 1

    print(fin)


decision = str(input('Enter "decimal" or "binary" to convert FROM'))

if decision == "decimal":
    num = int(input())
    binOne(num)
elif decision == "binary":
    num = str(input())
    binTwo(num)
