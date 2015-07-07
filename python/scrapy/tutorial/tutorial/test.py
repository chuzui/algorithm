# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# url = 'https://www.rijksmuseum.nl/en/collection/BK-18305'
#
# driver = webdriver.Firefox()
# driver.get(url)
# print driver.title
#

import urllib
import urllib2, cookielib
import requests, sys

cj = cookielib.MozillaCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r = opener.open("https://www.rijksmuseum.nl/")
urllib2.install_opener(opener)
for cookie in cj:
    print('%s --> %s'%(cookie.name,cookie.value))


data = {
    # '__RequestVerificationToken': cookie.value,
    # '__ios6cachebug': '1428991852032',
    'email': 'chuqi77@gmail.com',
        'password': '123456'
    }
headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Connection' : 'keep-alive',
    'Host' : 'www.rijksmuseum.nl',
    'Referer' : 'https://www.rijksmuseum.nl/en',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
    }
login_data = urllib.urlencode(data)
# opener.open('https://www.rijksmuseum.nl/en/login', login_data)

req = urllib2.Request('https://www.rijksmuseum.nl/en/login', login_data, headers=headers)
response = urllib2.urlopen(req)
url = 'https://www.rijksmuseum.nl/en/download/BK-18305/stap/1'
values ={ '__RequestVerificationToken':cookie.value, 'ObjectNumber':'BK-18305', }

data = urllib.urlencode(values)
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
the_page = response.read()

