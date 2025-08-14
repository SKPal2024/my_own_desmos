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
import matplotlib.pyplot as plt
import numpy as np
import math
import io

def create_plot(expression):
    x = np.arange(-4.0, 4.0, 0.01)
    try:
        y = eval(expression)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
