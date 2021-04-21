B = int(input())
T = int(input())

if (160-T)*(160-B) > B*T:
    print(2)
elif (160-T)*(160-B) < B*T:
    print(1)
else:
    print(0)