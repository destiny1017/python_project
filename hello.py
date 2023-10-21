from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/batch")
def execute():
    os.system(r'D:/test.bat')
    return "OK"


if __name__ == '__main__':
    app.run()
