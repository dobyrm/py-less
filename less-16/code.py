# test = None

# if(test == None):
# 	print('Test');

#Dictionary - словарь

test = {
	"Key_1" : "Value_1",
	"Key_2" : {
		"Key_2_1" : "Value_2_1"
	},
	"Key_3" : "Value_3",
	125 	: "Сто двадцять пять"
}

if 125 in test:
	print("Isset")
else:
	print("No isset")

if 125 not in test:
	print("No isset")
else:
	print("Isset")

try:
	print(test["Key_1"])
except KeyError:
	print("Not key!")

contacts = {
	"Yura" : "+380955455789",
	"Roma" : "+380955587895",
	"Ostap" : "+380955412369"
}

testing = input('Enter name : ')

if testing in contacts:
	print('contact isset ' + contacts[testing])
else:
	print('contact no isset')

print(contacts.get("Yura", "Not nomer!"))
print(contacts.get("Yura1", "Not nomer!"))