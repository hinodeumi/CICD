from flask import Flask
app=Flask(__name__)


@app.route("/")
def do_something():
    return "Hi, this is the CI/CD test."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
