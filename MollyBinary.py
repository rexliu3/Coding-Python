msg = 'This is a binary-decimal converter.'
msg += ' Please specify what kind of number you have.\n'
msg += 'There should be two lines of input in the following format:\n'
msg += '\tnumber\n\tbinary or decimal'
print(msg)
num = input()
numType = input().lower()


def bindec(number, numberType):
    n = number
    t = numberType
    if t == 'binary':
        r = 0
        l = len(n) - 1
        sep = []

        for i in n:
            sep.append(i)

        for i in sep:
            if l >= 0:
                if i == "1":
                    r += 2 ** l
                    l -= 1
                elif i == '0':
                    l -= 1
        print(str(r) + ' is its decimal counterpart!')

    if t == 'decimal':
        r = ''
        b = []
        n = int(n)
        active = True
        while active:
            if n > 0:
                rem = int(int(n) % 2)
                n /= 2
                b.insert(0, str(rem))

            if int(n) <= 0:
                active = False
        for i in b:
            r += i

        print(r + ' is its binary counterpart!')


bindec(num, numType)

