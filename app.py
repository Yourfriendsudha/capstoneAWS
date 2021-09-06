from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, Simple flask api"
app.run(host="0.0.0.0", port=8080, debug=True)
