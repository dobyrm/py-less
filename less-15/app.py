#app copy file

fileName1 = input('enter name file copy: \n')
fileName2 = input('enter core file: \n')

file1 = open(fileName1, 'r')
file2 = open(fileName2, 'w')

file2.write( file1.read() )

file1.close()
file2.close()

print('copy data success')