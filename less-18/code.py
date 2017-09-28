digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

digits2 = digits[2:5]
digits2 = digits[:3]
digits2 = digits[3:11]
digits2 = digits[3:]

#1 3 5 7 9
digits2 = digits[::2]

digits2 = digits[-3]
digits2 = digits[-4:-1]

digits2 = digits[::-1]
digits2 = digits[::-1][::-1]

print( digits2 )

digits2 = range(2, 101)[::2]

# for i in digits2:
# 	print(i)