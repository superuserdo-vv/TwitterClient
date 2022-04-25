from flask import Flask, request
import get

app = Flask(__name__)

@app.route("/")
def users():
    get.main()
    return "<p>{}</p>".format(request.method)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)