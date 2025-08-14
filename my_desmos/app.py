from flask import Flask, request, render_template, send_file
from graph import create_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/plot', methods=['POST'])
def plot():
    expression = request.form['expression']
    try:
        buf = create_plot(expression)
    except ValueError as e:
        return str(e), 400
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
