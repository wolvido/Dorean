import old

while True:
	text = input('old > ')
	result, error = old.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)