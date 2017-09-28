#test = 'Howdy Ho'

#print to displey
#print(test)

#def howd_ho():
#	'''  Опис функції '''
#	print('Howd Ho!')

#howd_ho()
#print( howd_ho.__doc__ )

#my_var = howd_ho

#my_var()

def howd_ho(name):
	'''  Опис функції '''
	print('Howd Ho, ' + name()  + '!')

def read_name():
	return ':::' + input('Enter name: ') + ':::'

howd_ho( read_name )