#!/usr/bin/python
# -*- coding: utf-8 -*-
#PhoneInfog
#Phonenumber Information gathering
#=====================================
#-==] Aunthor : TheMentor
#-==] Team : TheMentor
#-==] Date : 17 JULI 2019
#-==] Github : https://github.com/TheMentor-Script
#-==] YouTube : Still in Progres
#=====================================

#module
import requests
import os
import sys
import urllib
import json

#color
k = '\033[93m'
u = '\033[95m'
n  = '\033[94m'
m = '\033[91m'
h = '\033[92m'
p = '\033[00m'

os.system ('clear')

#banner

print n+"………….(0 0) "
print n+".—oOO–(_)—–."
print n+"╔═════════════════╗ "
print n+"║   Phone - Info    ║ "
print n+"╚═════════════════╝ "
print k+"‘———————-oOO "
print k+"……...|__|__| "
print k+"……….. || || "
print k+"…….. ooO Ooo"
print k+"https://github.com/TheMentor-Script"
print

#input number
number = raw_input(m+"["+k+"#"+m+"]"  +h+"phone number : ")
print
#data
key = "9810ba5ae4fe74c2930842025d11bc58"
url = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=&format=1"
output = requests.get(url)
result = output.text
js = json.loads(result)
#running
country_code = js['country_code']
country_name = js['country_name']
location = js['location']
carrier = js['carrier']
line_type = js['line_type']

print m+"["+k+"#"+m+"]"  +h+"phonenumber information gathering"  +m+"["+k+"#"+m+"]"
print
print k+"["+m+"+"+k+"]"  +h+"Information Output"
print k+"--------------------------------------"
print k+" ~" +h+"Phone number: " +str(number)
print k+" ~" +h+"Country: " +str(country_code)
print k+" ~" +h+"Country Name: " +str(country_name)
print k+" ~" +h+"Location: " +str(location)
print k+" ~" +h+"Carrier: " +str(carrier)
print k+" ~" +h+"Device: " +str(line_type)