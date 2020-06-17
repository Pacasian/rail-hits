from flask import Response
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, Response
import json
from requests import get

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    with open('static/data.json') as json_file:
        data = json.load(json_file)
        temp = data['ip']
    return render_template("index.html", showIp=temp)


@app.route('/manage_ip', methods=['POST'])
def manage_game():
    submit = request.form['action'] == 'Submit'
    ip = request.form['ipAddress']
    with open('static/data.json', 'w') as f:
        #ip = get('https://api.ipify.org').text
        #print('My public IP address is:', ip)
        y = {"ip": ip,
             }
        json.dump(y, f)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
