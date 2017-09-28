#try:
#	print(7 / 0)
#except ZeroDivisionError:
	#pass
#	print('Poymano isklyuchenie dileniye po nolyu')

#try:
#	print(7 / 0)
#except:
#	print('Poymano isklyuchenie')

#try:
	#eval('print(7 / 4)a') #valid SyntaxError
#	print(7 / 4)
#except ZeroDivisionError:
#	print('Poymano isklyuchenie dileniye po nolyu')
#except SyntaxError:
#	print('Poymano isklyucheniye SyntaxError')
#except NameError:
#	print('Poymano isklyucheniye NameError')
#except:
#	print('Poymano isklyucheniye')

#try:
#	print(num / 0)
#except (ZeroDivisionError, NameError, ValueError, TypeError):
#	print('Poymano ploxoye isklyuchenie ^_^')
#except:
#	print('Poymano isklyuchenie')

#try:
#	print(num / 0)
#except (ZeroDivisionError, NameError, ValueError, TypeError):
#	print('Poymano ploxoye isklyuchenie ^_^')
#except:
#	print('Poymano isklyuchenie')
#finally:
#	 print('end poimki ')

#print('Programm end')

#try:
#	 pogoda = 'bad'
#	 if pogoda == 'bad':
#	 	raise TypeError
#except TypeError:
#	 print('Poymano isklyuchenie TypeError')

#pogoda = 'hot'
#if pogoda == 'hot':
#	raise TypeError('Test')

#try:
#	pogoda = 'colt'
#	if pogoda == 'colt':
#		raise TypeError('Test')
#except:
#	print('Poymano isklyuchenie')

#try:
#	print(5 / 0)
#except:
#	print('Test')
#	raise

class HowdyHoError (Exception):
	pass

raise HowdyHoError('Test')
