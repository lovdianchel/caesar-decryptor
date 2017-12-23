#!/usr/bin/python3

import argparse
import time

print("""
   ___                        __
  / _ \___ __________ _____  / /____  ____
 / // / -_) __/ __/ // / _ \/ __/ _ \/ __/
/____/\__/\__/_/  \_, / .__/\__/\___/_/
                 /___/_/
| Author : Mr. Pixelheartz
| Caesar Decrypter
| 'caesar.py --help' for usage
""")


parser = argparse.ArgumentParser(description="decryptor is a tool to decrypt the caesar chiper or search all key probability.")
parser.add_argument("-k", "--key", type = str, default = "all", help = "the key if you already have it. e.g. [a], [b], or etc.")
# parser.add_argument("--text", metavar = "CHIPERTEXT", type = str, required = True, help = "the chipertext which will decrypted.")
args = parser.parse_args()

a = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA')
b = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB')
c = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC')
d = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'efghijklmnopqrstuvwxyzabcdEFGHIJKLMNOPQRSTUVWXYZABCD')
e = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'fghijklmnopqrstuvwxyzabcdeFGHIJKLMNOPQRSTUVWXYZABCDE')
f = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ghijklmnopqrstuvwxyzabcdefGHIJKLMNOPQRSTUVWXYZABCDEF')
g = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'hijklmnopqrstuvwxyzabcdefgHIJKLMNOPQRSTUVWXYZABCDEFG')
h = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ijklmnopqrstuvwxyzabcdefghIJKLMNOPQRSTUVWXYZABCDEFGH')
i = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'jklmnopqrstuvwxyzabcdefghiJKLMNOPQRSTUVWXYZABCDEFGHI')
j = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'klmnopqrstuvwxyzabcdefghijKLMNOPQRSTUVWXYZABCDEFGHIJ')
k = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'lmnopqrstuvwxyzabcdefghijkLMNOPQRSTUVWXYZABCDEFGHIJK')
l = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'mnopqrstuvwxyzabcdefghijklMNOPQRSTUVWXYZABCDEFGHIJKL')
n = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'opqrstuvwxyzabcdefghijklmnNOPQRSTUVWXYZABCDEFGHIJKLM')
o = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'pqrstuvwxyzabcdefghijklmnoOPQRSTUVWXYZABCDEFGHIJKLMN')
m = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'nopqrstuvwxyzabcdefghijklmPQRSTUVWXYZABCDEFGHIJKLMNO')
p = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'qrstuvwxyzabcdefghijklmnopQRSTUVWXYZABCDEFGHIJKLMNOP')
q = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'rstuvwxyzabcdefghijklmnopqRSTUVWXYZABCDEFGHIJKLMNOPQ')
r = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'stuvwxyzabcdefghijklmnopqrSTUVWXYZABCDEFGHIJKLMNOPQR')
s = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'tuvwxyzabcdefghijklmnopqrsTUVWXYZABCDEFGHIJKLMNOPQRS')
t = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'uvwxyzabcdefghijklmnopqrstUVWXYZABCDEFGHIJKLMNOPQRST')
u = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'vwxyzabcdefghijklmnopqrstuVWXYZABCDEFGHIJKLMNOPQRSTU')
v = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'wxyzabcdefghijklmnopqrstuvWXYZABCDEFGHIJKLMNOPQRSTUV')
w = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'xyzabcdefghijklmnopqrstuvwXYZABCDEFGHIJKLMNOPQRSTUVW')
x = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'yzabcdefghijklmnopqrstuvwxYZABCDEFGHIJKLMNOPQRSTUVWX')
y = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY')
z = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# key_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

key_list = {'a' : a, 'b' : b, 'c' : c, 'd' : d, 'e' : e, 'f' : f, 'g' : g, 'h' : h, 'i'  : i, 'j' : j, 'k' : k, 'l' : l, 'm' : m, 'n' : n, 'o' : o, 'p' : p, 'q' : q, 'r' : r, 's' : s, 't' : t, 'u' : u, 'v' : v, 'w' : w, 'x' : x, 'y' : y, 'z' : z}

text = input("Input the chipertext: ")


def decrypt():
    if args.key == "a":
        key = a
    elif args.key == "b":
        key = b
    elif args.key == "c":
        key = c
    elif args.key == "d":
        key = d
    elif args.key == "e":
        key = e
    elif args.key == "f":
        key = f
    elif args.key == "g":
        key = g
    elif args.key == "h":
        key = h
    elif args.key == "i":
        key = i
    elif args.key == "j":
        key = j
    elif args.key == "k":
        key = k
    elif args.key == "l":
        key = l
    elif args.key == "m":
        key = m
    elif args.key == "n":
        key = n
    elif args.key == "o":
        key = o
    elif args.key == "p":
        key = p
    elif args.key == "q":
        key = q
    elif args.key == "r":
        key = r
    elif args.key == "s":
        key = s
    elif args.key == "t":
        key = t
    elif args.key == "u":
        key = u
    elif args.key == "v":
        key = v
    elif args.key == "w":
        key = w
    elif args.key == "x":
        key = x
    elif args.key == "y":
        key = y
    elif args.key == "z":
        key = z

    result = text.translate(key)
    print("Decrypting...")
    time.sleep(2)
    print('Your plaintext for [{}] is "{}"'.format(args.key, result))

def probability():
    print("Decrypting...")
    time.sleep(5)
    for i in key_list:
        print("{0} ----> {1}".format(i, text.translate(key_list[i])))
        time.sleep(0.1)

def main():
    if args.key == "all" :
        probability()
    elif args.key in key_list.keys() :
        decrypt()
    else:
        print("Wrong key!!! The key must be a lowercase ")

if __name__ == "__main__" :
    main()
