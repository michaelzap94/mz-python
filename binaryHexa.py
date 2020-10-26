#1 byte = 8 bits. 1 bit can contain 2 values
# 11111111 = octet = 8 bits = 0 to 255 =>>>> 100000000 => 256 values = 8**2 ==> 1 BYTE
for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

my_Bin = 0b010101010

print(my_Bin)

print('='*10)

#Hexadecimals==========================

# Short numbers, closer  to binary than decimal
# base 16
# 16**3, 16**2, 16**1, 16**0
for i in range(17):
    print("{0:>2} in binary is {0:>02x}".format(i))

x = 0x20 # 32 decimal
y = 0x0a # 10 decimal
print(x*y)
