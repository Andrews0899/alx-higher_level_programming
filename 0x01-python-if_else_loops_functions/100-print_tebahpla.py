#!/usr/bin/python3
for letter in range(90, 64, -1):
    print("{}".format(chr(letter + 32 if letter % 2 == 0 else letter)), end="")
