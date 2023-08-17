from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    return render_template('index.html', cpu_percent=cpu_percent, memory_info=memory_info)

if __name__ == '__main__':
    app.run(debug=True)
