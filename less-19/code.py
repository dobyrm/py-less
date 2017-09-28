# Форматування строк

name = 'Jessy'
age = 21

# %
# .format()

#print ( 'Hi, %s!\nTibe uge %d god!' % (name, age) )

# %s - Плейсхолдер строки
# %d - Плейсхолдер числа
# %f - Плейсхолдер дроби

#print( 'Hi, {}! \nTebe uge {} god!' . format( name, age ) )
#print( 'Hi, {0}! \nTebe uge {1} god!' . format( name, age ) )
#print( '{0}{1}{0}' . format( 'ХАБР', 'A' ) )

# person_name = 'Jesi'
# person_age = 21
# print( 'Hi, {name}! \nTebe uge {age} god!' . format( name = person_name, age =  person_age) )

# human = {
# 	'name'	: 'Jessy',
# 	'age'  	: 21
# }

# print( 'Hi, {person[name]}! \nTebe uge {person[age]} god!' . format( person = human ) )

input_str = 'Jessy'

# Jessy***** <
# *****Jessy <
# **Jessy*** ^

#print( '{0:*^15}' . format( input_str ) )

length = 10

if ( len(input_str) % 2):
	length += 1

print( ('{0:*^'+str(length)+'}') . format( input_str ) )

