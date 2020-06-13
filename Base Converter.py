def converterTO(number, base):
    finished = ""
    mainNum = number

    while mainNum > 0:
        res = mainNum % base
        finished = str(res) + finished
        mainNum = int(mainNum / base)

    print(finished)


def converterFROM(number, base):
    finished = 0
    mainNum = number

    k = 0
    lengths = len(mainNum)
    for i in range(lengths):
        finished = finished + (pow(base, i)*int(mainNum[lengths-i-1]))

    print(finished)


decis = str(input('Enter "TO" or "FROM"'))
based = int(input('Enter base to convert TO or FROM'))
num = str(input('Enter number'))

if decis == "TO":
    num = int(num)
    converterTO(num, based)
elif decis == "FROM":
    converterFROM(num, based)