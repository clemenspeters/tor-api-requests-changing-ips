from stem import Signal
from stem.control import Controller
import requests
import time
from random import randint
import json

import subprocess
import cfscrape

# # signal TOR for a new connection
def switchIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        seconds = controller.get_newnym_wait()
        print('Wait for %i seconds.' %(seconds))
        time.sleep(seconds)
        print('New IP available: %s' %(controller.is_newnym_available()))


for x in range(10):
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5h://localhost:9050'
        session.proxies['https'] = 'socks5h://localhost:9050'
        url = 'http://httpbin.org/ip'
        r = session.get(url)
        print(r.text)
        switchIP()
