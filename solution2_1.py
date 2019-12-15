ker = 3
secret_message = ""
with open("mydata.txt", encoding="utf-8") as my_file:
	while True:
		line = my_file.readline()
		if not line:
            break
		for char in line:
			if char.isalpha():
				char_code = ord(char)
				char_code += key
				if char.isupper():
					if char_code > ord('Z'):
					char_code -= 26
					elif char_code < ord('A'):
					char_code += 26
				else:
					if char_code > ord('z'):
					char_code -= 26
					elif char_code < ord('a'):
					char_code += 26
				secret_message += chr(char_code)
			else:
				secret_message += char
print("Encrypted :", secret_message)