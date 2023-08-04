for x in range(0, 10):
    for i in range(x+1, 10):
        if x == 8 and i == 9:
            print(89)
        else:
            print("{}{}".format(x,i), end = ", ")
        