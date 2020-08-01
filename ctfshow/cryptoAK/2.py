from decimal import *
for data in range(1,100):
    for key in range(10,1000):
        sign = str(Decimal(data) / Decimal(key))
        for d in range(1,data-2):
            if d == int(sign[d*2:(d+1)*2]):
                print("------")
                print("data:",Decimal(data))
                print("key:",Decimal(key))
                print("d:",d)
                print("int(xx):",int(sign[d*2:(d+1)*2]))
                print("------")

# data = 1
# print(data^0x36d)
# print(int(0x36d))
# print(877^1)
# print(Decimal(data))