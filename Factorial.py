
put = int(input("Enter Number (to be Factorialed)"))

a = 1
b = 1

for x in range(1, put):
    a = a*b
    b += 1

print(a)