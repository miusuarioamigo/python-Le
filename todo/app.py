#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

#just test data
sngs =[
    {
        'id':0,
        'title' : 'Coffee and TV',
        'author': 'Blur',
        'first_sentence': 'Do you feel like a chain store',
        'year_published': '1998'
    },
    {
        'id':1,
        'title' : 'Lazarus',
        'author': 'Porcupine Tree',
        'first_sentence': 'As the cheerless towns pass my window',
        'year_published': '2005'
    },
    {
        'id':2,
        'title' : 'Diamonds',
        'author': 'Echosmith',
        'first_sentence': 'She just wants to come alive, alive',
        'year_published': '2020'
    },
    {
        'id':3,
        'title' : 'Everyone Cries',
        'author': 'Echosmith',
        'first_sentence': 'Do you feel invisible?',
        'year_published': '2020'
    }
]

#fist page
@app.route('/')
def index():
    return "<h1>Life is a bunch of shit</h1><p>But I could be dead</p>"

#api example shows all info of test data
@app.route('/api/v1/songs/all',methods=['GET'])
def api():
    return jsonify(sngs)

#api exaple show test data accoding to id ##
@app.route('/api/v1/songs',methods=['GET'])
def api_id():
    #if there's a query parametes ?id=# assign it to a variable
    #if not the show Error message
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "<h2>Error: No id field provided.</h2>"
    
    results=[]
    
    #match provided id with our "catalog"(test data)
    for i in sngs:
        if i['id'] == id:
            results.append(i)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)