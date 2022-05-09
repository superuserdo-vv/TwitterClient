from flask import Flask, make_response, render_template, request
import get

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/tweet")
def main():
    resp = make_response(get.returnHTML())
    # resp.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    # resp.headers["Content-Type"] = "text/plain"
    return resp


@app.route("/get")
def gets():
    get.getData()
    return "<p>{}</p>".format(request.url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
