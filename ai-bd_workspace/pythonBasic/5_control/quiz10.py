for i in range(5):
    for j in range(5):
        print("%3d"%(i * 5 + j + 1), end=" ");
    print();

for i in range(5):
    for j in range(5):
        if i%2 == 0:
            print("%3d"%(i * 5 + j + 1), end=" ");
        else:
            print("%3d"%(i * 5 + 5 - j), end=" ");
    print();
        