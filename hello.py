from flask import Flask
app = Flask(__name__)
@app.route("/")
# HELLO  COMMENTS
def hello():
        return "Hello Dev"
if __name__ == "__main__":
    app.run()
