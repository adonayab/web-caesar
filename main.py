from flask import Flask, request, render_template
from caesar import rotate_string


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    if rot.isdecimal() == False:
      error = '0 - 1000'
      return render_template('index.html', error=error)
    
    if int(rot) > 1000:
      error = '0 - 1000'
      return render_template('index.html', error=error)

    encrypted_text = rotate_string(text, int(rot))

    return render_template('index.html', encrypted_text=encrypted_text)

app.run()
