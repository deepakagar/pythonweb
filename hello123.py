from flask import Flask
app = Flask(__name__)
@app.route("/")
#test
def hello():
        return "Hello COMMIT12345"
if __name__ == "__main__":
    app.run()
