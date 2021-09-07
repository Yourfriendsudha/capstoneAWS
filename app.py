from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome, Simple flask api . this is version 3. Rolling strategy tested</h1>"

@app.route('/home', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run(host="0.0.0.0", port=8080, debug=True)
