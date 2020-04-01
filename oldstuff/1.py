from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    a = 5
    b = 10
    c = a + b
    c1 = str(c)
    return "Hello World!" + c1

if __name__ == "__main__":
    app.run()