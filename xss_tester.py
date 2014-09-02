__author__ = 'Prasanna'


import automate
import mechanize
import bs4
import re

a = automate.formGetter()
url = "http://testphp.vulnweb.com"
searchTerm = "0xdeadbeef"
sd = a.getForms(url)
browser = mechanize.Browser()
browser.open(url)
print "Forms in this Page : ", sd[0],"\n"
forms = sd[1]
for i in range(0,len(forms)):
    browser.form = sd[1][i]
    for control in browser.form.controls:
        if control.type == "text":
            browser.form[control.name] = "0xdeadbeef"+" "+control.name
    Response = browser.submit()
    soup = bs4.BeautifulSoup(Response.read())
    result = soup.find_all("h2",text=re.compile(searchTerm))
    if len(result) > 0:
        print "The Url : ", url," Could be vulnerable for XSS. Payload in Response :  ",result
