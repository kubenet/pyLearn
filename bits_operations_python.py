# -25.0
num1=0b11100111
num2=0b00000000

# -0.5
num1=0b11111111
num2=0b10000000


# 33.70
p1=0b10100001
p2=0b10110010

# -55.5
num1=0b11001001
num2=0b10000000

# +128.0
#num1=0b01111111
#num2=0b11111111


negRez=0
rez = (num1 << 8) | (num2)
print(bin(rez))

if rez >> 15 & 1:
	print('negative')
#	print(bin(num1))
	num1 = (~num1 & 0xff)
	num1 = num1+0b00000001
#	print(bin(num1))
	negRez = (num1 << 8) | (num2)
#	print(bin(negRez))
	print((float(negRez) * -0.00390625),'C')
# 	#print('negRez')
# 	#print(bin(negRez))	

else:
	print('positive')
	rez *= 0.00390625
	print(rez,'C')


