# written by aadit kapoor, on 26.4.16
# a program to to fetch the remaining gb from airtel page, using requests
# and to show messages based on that.

# ver:1.0.0


import requests
from bs4 import BeautifulSoup
from time import sleep


url = "http://122.160.230.125:8080/planupdate/"
messages = ["stop using the internet, gb is about to finish soon!", "please stop using!", "THAT'S ENOUGH!"]

def fetch():
     c = requests.get(url)
     soup = BeautifulSoup(c.content,"html5lib")

     gb = str(soup.findAll("div" , {"class":"description"})[1].find("span").getText())
     a = gb.strip("  GB")

     a = float(a)

     return a
    

try:
    a = fetch()
except:
    print 'I THINK THE SERVER IS NOT LETTING US IN! TRYING AGAIN  IN 5 SECS'
    sleep(5) ; a = fetch()




print a # PRINTING THE RETURNED GB
if a > 90:
    print messages[0]
elif a > 100:
    print  messages[1]
else:
    print messages[2]
