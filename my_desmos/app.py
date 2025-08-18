from flask import Flask, render_template, request
import io
import base64
from graph import plot_graph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    graph_url = None
    if request.method == 'POST':
        equation = request.form['equation']
        x_min = float(request.form['x_min'])
        x_max = float(request.form['x_max'])

        graph_url = plot_graph(equation, x_min, x_max)

    return render_template('index.html', graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
