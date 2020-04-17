
n1 = int(input("Enter a 2-digit hexadecimal number: "), 16)
n2 = int(input("Enter another 2-digit hexadecimal number: "), 16)
a = n1 if n1 >= n2 else n2
print(str(hex(a)).upper()[str(hex(a)).find('x') + 1:])