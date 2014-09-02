__author__ = 'Prasanna'


import mechanize

class formGetter():
    def __init__(self):
        self.counter = 0
    def getForms(self,url):
        browser = mechanize.Browser()
        browser.open(url)
        browser.formz = list(browser.forms())
        for form in browser.formz:
            self.counter+=1
        return (self.counter,list(browser.formz))

    def __del__(self):
        self.counter = 0

