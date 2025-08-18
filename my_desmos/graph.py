# import numpy as np
# import matplotlib.pyplot as plt
# import math
# from matplotlib.widgets import TextBox

# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.2) # Adjust layout to make space for the textbox

# x = np.arange(-4.0, 4.0, 0.01)
# line, = ax.plot(x, np.zeros_like(x), lw=2)

# def submit(expression):
#     try:
#         ydata = eval(expression)
#         line.set_ydata(ydata)
#         ax.relim()
#         ax.autoscale_view()
#         plt.draw()
#     except Exception as e:
#         print(f"Error evaluating expression: {e}")

# axbox = plt.axes([0.1, 0.05, 0.8, 0.075]) # Position of the textbox
# text_box = TextBox(axbox, 'Plot: ')
# text_box.on_submit(submit)

# plt.show()



# graph.py
import matplotlib
matplotlib.use('Agg')  # For running without GUI
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import math

def plot_graph(equation, x_min, x_max):
    x = np.linspace(x_min, x_max, 500)

    try:
        # Safely evaluate equation
        y = [eval(equation, {"x": val, "math": math,  "np": np,"__builtins__": {}}) for val in x]
    except Exception as e:
        return None

    fig, ax = plt.subplots()
    ax.plot(x, y, label=equation)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    ax.grid(True)

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"

