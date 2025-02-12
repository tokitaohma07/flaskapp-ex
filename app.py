from flask import Flask

app = Flask(__name__)

@app.route("/wish")
def pleaseWish():
    return "Hello, Jenkin"

if __name__ == "__main__":
    app.run(host="0.0.0.0")