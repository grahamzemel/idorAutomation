import base64
import urllib.parse
from bs4 import BeautifulSoup
import json
import requests

val = input("Enter parameter") #Ex. 'MjQzNDU%3D' from article, without single quotes

base64_encode = val.encode('utf-8')
base64_bytes = base64.b64encode(base64_encode)
final_base64 = base64_bytes.decode('utf-8')
url_encode = urllib.parse.quote_plus(final_base64)

r = requests.get("https://website.com/friend-request/?id={}".format(url_encode))
soup = BeautifulSoup(r.content, "html.parser")
for script in soup.find_all('script'):
    if len(script.contents):
        print(script.contents[0])
        
