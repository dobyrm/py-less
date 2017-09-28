#app copy file backup data

fileName1 = input('enter name file copy: \n')
fileName2 = 'backup_' + fileName1

file1 = open(fileName1, 'rb')
file2 = open(fileName2, 'wb')

file2.write( file1.read() )

file1.close()
file2.close()

print('backup data success')