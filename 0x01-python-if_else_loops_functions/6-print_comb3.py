#!/usr/bin/python3

for digi1 in range(0, 10):
    for digi2 in range(digi1 + 1, 10):
        if digi1 == 8 and digi2 == 9:
            print("{}{}".format(digi1, digi2))
        else:
            print("{}{}".format(digi1, digi2), end=", ")
