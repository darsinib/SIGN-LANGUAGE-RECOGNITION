from flask import Flask, render_template, request,Response
from test import get_asl
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_asl')
def asl():

    return Response(get_asl(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    app.run(debug=True)
