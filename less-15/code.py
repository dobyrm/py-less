#def exc(text):
#	assert text != ''
#	print(str(text) + '!')

#exc('')
###################################
#def test(num):
#	assert num > 0, "Number > 0."
#	print(str(num))

#test(1)
###################################
#file = open('test.txt', 'r')
#print(file.read())
#print(file.read(5)) #перші 5 байтів
#print(file.read(1024 * 100)) #якщо виликий файл то читати по частям
#file.close()
###################################
#filename = input('Enter file name?: ')
#file = open('test.txt', 'r')

#print( 'file size simvol: ' + str(len(file.read())))

#file.close()

#file = open('test.txt', 'w')

#file.write('sss')

#file.close()
###################################
#filename = input('Enter file name?: ')
#text = input('text to file: ');

#file = open(filename, 'w')

#file.write(str(text));

#file.close()

#file = open('test.txt', 'a')

#file.write( ' TEST' * 2 )

#file.close()

#зчітуємо по строкам

#file = open('test.txt', 'r')
#strings = file.readlines()
#print(strings)

#for string in strings:
#	print(string)

#file.close()

################################### WITH

with open('test.txt', 'r') as f:
	print(f.read())

