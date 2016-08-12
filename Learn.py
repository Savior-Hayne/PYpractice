#coding=utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#获取url的Title
def getTitle(url):
        try:
            html = urlopen(url)
        except HTTPError as e:
            return None
        try:
            bsObj = BeautifulSoup(html.read(),"html.parser")
            title = bsObj.body.h1
        except AttributeError as e:
            return None
        return title



title = getTitle("http://www.pythonscraping.com/TestFourse")
# Test url（T）：http://www.pythonscraping.com/pages/page1.html
# Test url（F）：http://www.pythonscraping.com/TestFourse

if title == None:
    print("Title could not be found")
else:
    print(title)