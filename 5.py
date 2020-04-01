from flask import Flask, jsonify
app = Flask(__name__)

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

@app.route("/")
def hello():
    return jsonify({"": ""})

if __name__ == "__main__":
    app.run(debug=True)