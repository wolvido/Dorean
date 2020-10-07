import MyLang

while True:
	text = input('MyLang > ')
	result, error = MyLang.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)