#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics
"""


import sys

status_list = [0, 0, 0, 0, 0, 0, 0, 0]
names = ["200", "301", "400", "401", "403", "404", "405", "500"]

count = 0
file_size = 0
if not sys.stdin:
    print("File size: {}".format(file_size))
try:
    for lines in sys.stdin:
        word_list = lines.split()
        if len(word_list) >= 2:
            for i in range(len(names)):
                if names[i] in word_list and word_list[-1] != names[i]:
                    status_list[i] += 1
            file_size += int(word_list[-1])
            count += 1
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for i in range(len(status_list)):
                if status_list[i]:
                    print("{}: {}".format(names[i], status_list[i]))
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for i in range(len(status_list)):
        if status_list[i]:
            print("{}: {}".format(names[i], status_list[i]))
    raise
print("File size: {}".format(file_size))
for i in range(len(status_list)):
    if status_list[i]:
        print("{}: {}".format(names[i], status_list[i]))
