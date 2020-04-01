from flask import Flask
app = Flask(__name__)

@app.route("/<int:s1>")
def hello(s1):
    
    return "valor igual a: %d" %s1

if __name__ == "__main__":
    app.run()