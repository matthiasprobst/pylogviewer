import logging
import pathlib

from flask import Flask, render_template, request

app = Flask(__name__)


def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)


# Initialize logging and setup the loggers
setup_logging()

# Get a list of available log files
log_files = list(pathlib.Path(r'C:\Users\da4323\AppData\Local\h5rdmtoolbox').rglob('*.log'))
log_files += list(pathlib.Path(r'C:\Users\da4323\AppData\Local\piv2hdf').rglob('*.log'))


@app.route('/')
def index():
    return render_template('index.html', log_files=log_files)


@app.route('/logs/<log_file>', methods=['GET', 'POST'])
def display_logs(log_file):
    # Handle form submission
    if request.method == 'POST':
        log_level = request.form.get('log_level', 'all')

        with open(log_file, 'r') as file:
            logs = file.readlines()

        if log_level == 'all':
            pass
        else:
            logs = [log for log in logs if log_level in log]

        logs.reverse()
        logs = ''.join(logs)

        return render_template('logs.html', log_file=log_file, logs=logs, log_level=log_level)

    # If it's a GET request, show all log messages
    with open(log_file, 'r') as file:
        logs = file.read()

    return render_template('logs.html', log_file=log_file, logs=logs, log_level='all')


def start(debug=False):
    """Start the web server"""
    app.run(debug=debug)


if __name__ == '__main__':
    start(debug=True)
