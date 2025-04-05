import os
import getpass
import subprocess
from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Divya Roopa Ramesh"

    
    username = getpass.getuser()

    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    html_response = f"""
    <h1>Name: {full_name}</h1>
    <p>User: {username}</p>
    <p>Server Time (IST): {current_time_ist}</p>
    <pre>{top_output}</pre>
    """
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
