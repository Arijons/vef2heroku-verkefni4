import json
from bottle import route, run , template

with open("gengi.json", "r") as skra:
    gogn = json.load(skra)



mydict={"Shortname":["value","askValue","bidValue","changeCur","changePer"]}

for r in range(10):
    lina=gogn["results"][r]
    mydict.update({lina["shortName"]:[lina["value"],lina["changeCur"],lina["changePer"]]})

fjöldi = 3

@route('/page2')
def serve_homepage():
    return template('disp_table',rows = mydict, cases = fjöldi)

run(host="localhost", port=8080, debug=True)

