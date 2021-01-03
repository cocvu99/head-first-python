import os

os.getcwd()

try:
	data.open('missing.txt')
	print(data.readLine(), end='')
except IOError as err:
	print('File Error' + str(err))
finally:
	if 'data' in locals():
		data.close()

# This .py file == error occurs. Just learning