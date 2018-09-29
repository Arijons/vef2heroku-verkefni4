

from sys import argv

import bottle
from bottle import *
bottle.debug(True)



import json
from bottle import route, run , template

with open("gengi.json", "r") as skra:
    gogn = json.load(skra)



mydict={"Shortname":["value","askValue","bidValue","changeCur","changePer"]}

for r in range(10):
    lina=gogn["results"][r]
    mydict.update({lina["shortName"]:[lina["value"],lina["changeCur"],lina["changePer"]]})

fjöldi = 3

@route('/')
def serve_homepage():
    return template('disp_table',rows = mydict, cases = fjöldi)

bottle.run(host='0.0.0.0', port=argv[1])



