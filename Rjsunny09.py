#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

if not os.path.isfile('Jutt.so'):

    os.system('curl -L https://raw.githubusercontent.com/RJ-SUNNY/sunny/main/fighter.cpython-310.so > Jutt.so')

    os.system('clear')

if not os.path.isfile('brand.so'):

    os.system('curl -L https://raw.githubusercontent.com/RJ-SUNNY/sunny/main/fighter.cpython-310.so > brand.so')

    os.system('clear')

bit=platform.architecture()[0]

go = requests.get('https://raw.githubusercontent.com/RJ-SUNNY/fighter/main/update.txt').text

if 'Juttbrand' in go:

    if bit == '64bit':

        from sunny import reg

        reg()

    elif bit == '32bit':

        from rjbrand import reg

        reg()

else:

    os.system('rm -rf rj.so sunny.so')

    os.system('curl -L https://raw.githubusercontent.com/RJ-SUNNY/rjbrand/main/sunny.cpython-310.so > sunny.so')

    os.system('curl -L https://raw.githubusercontent.com/RJ-SUNNY/rjbrand/main/rjbrand.cpython-310.so > rjbrand.so')

    if bit == '64bit':

        from sunny import reg

        reg()

    elif bit == '32bit':

        from rjbrand import reg

        reg()

