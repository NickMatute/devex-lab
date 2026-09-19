from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return "Application is healthy", 200

app.run(port=8000)