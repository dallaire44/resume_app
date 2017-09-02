from flask import Flask,render_template,jsonify,json,request
import os


app = Flask(__name__)


@app.route('/')
def resume():
    return render_template('out.html')



if __name__ == "__main__":
    app.run()
