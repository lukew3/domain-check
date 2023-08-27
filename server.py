from flask import Flask, request, send_file
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    domain = request.args.get('domain')
    if not domain:
        return send_file('index.html')
    r = requests.get(f"https://rdap.verisign.com/com/v1/domain/{domain}")
    if r.status_code == 404:
        return "AVAILABLE"
    elif r.status_code == 200:
        return "NOT AVAILABLE"
    else:
        return "SYSTEM ERROR"

if __name__ == "__main__":
    app.run()

