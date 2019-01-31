from flask import Flask, request, render_template
from caesar import rotate_string


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    encrypted_text = rotate_string(text, rot)

    return render_template('index.html', encrypted_text=encrypted_text)

app.run()
