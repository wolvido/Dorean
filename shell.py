import Dorean

while True:
	text = input('Dorean > ')
	result, error = Dorean.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)